import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
from pathlib import Path
from datetime import date

# -----------------------------
# Configuration
# -----------------------------
st.set_page_config(
    page_title="Gym Workout Logger",
    page_icon="🏋️‍♂️",
    layout="wide",
)

st.title("🏋️‍♂️ Gym Workout Logger")
st.write(
    "Log your workouts, track weekly volume, and visualize your progress over time."
)

# -----------------------------
# Sidebar Controls
# -----------------------------
st.sidebar.header("⚙️ Settings")

storage_type = st.sidebar.selectbox(
    "Data storage method",
    ["CSV", "SQLite"],
    index=0,
    help="Choose where your workout logs will be saved.",
)

default_csv = "workout_logs.csv"
default_db = "workout_logs.db"

if storage_type == "CSV":
    storage_path = st.sidebar.text_input(
        "CSV file path",
        value=default_csv,
        help="Workout data will be saved to this CSV file.",
    )
else:
    storage_path = st.sidebar.text_input(
        "SQLite DB path",
        value=default_db,
        help="Workout data will be saved to this SQLite database file.",
    )

graph_mode = st.sidebar.radio(
    "Graph mode",
    ["Total weekly volume", "Per-exercise weekly volume"],
    help="Choose how you want to visualize your weekly progress.",
)

graph_style = st.sidebar.radio(
    "Graph style",
    ["Bar", "Line"],
    help="Choose the chart style.",
)

# -----------------------------
# Data Storage Helpers
# -----------------------------
COLUMNS = [
    "date",
    "exercise",
    "sets",
    "reps",
    "weight",
    "weight_unit",
    "total_volume",
]

def init_empty_df():
    return pd.DataFrame(columns=COLUMNS)


def load_data(storage_type: str, path: str) -> pd.DataFrame:
    """Load workout data from CSV or SQLite."""
    if storage_type == "CSV":
        p = Path(path)
        if not p.exists():
            return init_empty_df()
        df = pd.read_csv(p)
    else:
        # SQLite
        conn = sqlite3.connect(path)
        try:
            df = pd.read_sql_query("SELECT * FROM workouts", conn)
        except Exception:
            # Table may not exist yet
            df = init_empty_df()
        finally:
            conn.close()
    if not df.empty:
        df["date"] = pd.to_datetime(df["date"]).dt.date
    return df


def save_row(storage_type: str, path: str, row: dict) -> None:
    """Append a single row to CSV or SQLite."""
    if storage_type == "CSV":
        p = Path(path)
        df_row = pd.DataFrame([row])
        if p.exists():
            df_existing = pd.read_csv(p)
            df_all = pd.concat([df_existing, df_row], ignore_index=True)
        else:
            df_all = df_row
        df_all.to_csv(p, index=False)
    else:
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS workouts (
                date TEXT,
                exercise TEXT,
                sets INTEGER,
                reps INTEGER,
                weight REAL,
                weight_unit TEXT,
                total_volume REAL
            )
            """
        )
        conn.commit()
        cur.execute(
            """
            INSERT INTO workouts (date, exercise, sets, reps, weight, weight_unit, total_volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                row["date"],
                row["exercise"],
                int(row["sets"]),
                int(row["reps"]),
                float(row["weight"]),
                row["weight_unit"],
                float(row["total_volume"]),
            ),
        )
        conn.commit()
        conn.close()


def add_week_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Add week_start and week_label columns for aggregation."""
    if df.empty:
        return df
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    # week_start = Monday of that week
    df["week_start"] = df["date"] - pd.to_timedelta(df["date"].dt.weekday, unit="D")
    df["week_label"] = df["week_start"].dt.strftime("%Y-%m-%d")
    return df


# -----------------------------
# Load existing data
# -----------------------------
df = load_data(storage_type, storage_path)

# -----------------------------
# Input Form
# -----------------------------
st.subheader("➕ Log a new workout")

with st.form("workout_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        workout_date = st.date_input("Date", value=date.today())
        exercise = st.text_input("Exercise name")
    with col2:
        sets = st.number_input("Sets", min_value=1, step=1, value=3)
        reps = st.number_input("Reps", min_value=1, step=1, value=10)
    with col3:
        weight = st.number_input("Weight", min_value=0.0, step=1.0, value=20.0)
        weight_unit = st.selectbox("Weight unit", ["kg", "lbs"])

    submitted = st.form_submit_button("Add workout")

    if submitted:
        # Validation
        errors = []
        if not exercise.strip():
            errors.append("Exercise name is required.")
        if sets <= 0:
            errors.append("Sets must be greater than 0.")
        if reps <= 0:
            errors.append("Reps must be greater than 0.")
        if weight < 0:
            errors.append("Weight cannot be negative.")

        if errors:
            for e in errors:
                st.error(e)
        else:
            total_volume = sets * reps * weight
            new_row = {
                "date": workout_date.isoformat(),
                "exercise": exercise.strip(),
                "sets": int(sets),
                "reps": int(reps),
                "weight": float(weight),
                "weight_unit": weight_unit,
                "total_volume": float(total_volume),
            }
            try:
                save_row(storage_type, storage_path, new_row)
                st.success(
                    f"Added: {exercise} — {sets} x {reps} @ {weight} {weight_unit} "
                    f"(volume: {total_volume:.1f})"
                )
                # Reload data after saving
                df = load_data(storage_type, storage_path)
            except Exception as exc:
                st.error(f"Failed to save workout: {exc}")

# -----------------------------
# Weekly Progress Graph
# -----------------------------
st.subheader("📊 Weekly Progress")

if df.empty:
    st.info("No workout data yet. Add some workouts to see your weekly progress.")
else:
    df_week = add_week_columns(df)

    if graph_mode == "Total weekly volume":
        agg = (
            df_week.groupby("week_label", as_index=False)["total_volume"]
            .sum()
            .sort_values("week_label")
        )
        if graph_style == "Bar":
            fig = px.bar(
                agg,
                x="week_label",
                y="total_volume",
                labels={"week_label": "Week starting", "total_volume": "Total volume"},
                title="Total Weekly Training Volume",
            )
        else:
            fig = px.line(
                agg,
                x="week_label",
                y="total_volume",
                markers=True,
                labels={"week_label": "Week starting", "total_volume": "Total volume"},
                title="Total Weekly Training Volume",
            )
    else:
        # Per-exercise weekly volume
        agg = (
            df_week.groupby(["week_label", "exercise"], as_index=False)["total_volume"]
            .sum()
            .sort_values("week_label")
        )
        if graph_style == "Bar":
            fig = px.bar(
                agg,
                x="week_label",
                y="total_volume",
                color="exercise",
                barmode="stack",
                labels={
                    "week_label": "Week starting",
                    "total_volume": "Total volume",
                    "exercise": "Exercise",
                },
                title="Per-exercise Weekly Training Volume (stacked)",
            )
        else:
            fig = px.line(
                agg,
                x="week_label",
                y="total_volume",
                color="exercise",
                markers=True,
                labels={
                    "week_label": "Week starting",
                    "total_volume": "Total volume",
                    "exercise": "Exercise",
                },
                title="Per-exercise Weekly Training Volume",
            )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Workout Log Table & Export
# -----------------------------
st.subheader("📄 Workout Log")

if df.empty:
    st.info("No logs yet. Once you add workouts, they will appear in this table.")
else:
    # Sort by date descending
    df_display = df.copy()
    df_display["date"] = pd.to_datetime(df_display["date"]).dt.date
    df_display = df_display.sort_values("date", ascending=False)

    st.dataframe(
        df_display,
        use_container_width=True,
    )

    # CSV export (always exportable as CSV even if stored in SQLite)
    csv_bytes = df_display.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download log as CSV",
        data=csv_bytes,
        file_name="workout_logs_export.csv",
        mime="text/cv",
    )

# -----------------------------
# Optional: Example Data Loader
# -----------------------------
with st.expander("👉 Need some example data?"):
    st.write(
        "Click the button below to load a few example workout entries. "
        "This is useful to quickly see how the charts and tables look."
    )
    if st.button("Load example data"):
        example_rows = [
            {
                "date": (date.today()).isoformat(),
                "exercise": "Bench Press",
                "sets": 3,
                "reps": 8,
                "weight": 60.0,
                "weight_unit": "kg",
                "total_volume": 3 * 8 * 60.0,
            },
            {
                "date": (date.today()).isoformat(),
                "exercise": "Squat",
                "sets": 5,
                "reps": 5,
                "weight": 80.0,
                "weight_unit": "kg",
                "total_volume": 5 * 5 * 80.0,
            },
            {
                "date": (date.today()).isoformat(),
                "exercise": "Deadlift",
                "sets": 3,
                "reps": 5,
                "weight": 100.0,
                "weight_unit": "kg",
                "total_volume": 3 * 5 * 100.0,
            },
        ]
        for row in example_rows:
            try:
                save_row(storage_type, storage_path, row)
            except Exception as exc:
                st.error(f"Failed to insert example data: {exc}")
                break
        st.success("Example data loaded. Scroll up to see the updated chart and table.")

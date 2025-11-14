from flask import Flask

app= Flask(__name__)

@app.route('/')
def hello():
    return("Hello Abdul.! I want to appriciate your efforts.!")

if __name__== '__main__':
    app.run(debug=True)

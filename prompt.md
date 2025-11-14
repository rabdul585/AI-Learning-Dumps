# Prompt Engineering Practice Templates

A comprehensive collection of prompt templates for various AI interactions and use cases.

## A. Basic Prompt Templates

### 1. General Inquiry
**Template:** Ask a general question about a topic
**Example:**
> What is AI Agent explain in simple terms?.

### 2. Summarization
**Template:** Summarize text in specific format/length
**Example:**
> Write about the history of AI in 3 bullet points within 30 words


### 3. Paraphrasing
**Template:** Rewrite text while maintaining meaning
**Example:**
> Rewrite this idoms in your own words:
>
> "Let the cat out of the bag"

### 4. Definition Request
**Template:** Ask for meaning/definition
**Example:**
what is semantic search and expaing with proper definition?.

### 5. Comparison
**Template:** Compare items based on specific criteria
**Example:**
> Compare GPT-4o(mini) models with the GPT3.5 on the bechmark

## B. Persona-Based Prompt Templates

### 6. Role + Explanation
**Template:** `You are a [role]. Explain [concept] to [audience].`
**Example:**
> You are an aeronautical engineer. Explain what are the routine checks happening before the takeoff of the flight and the steps taken during the emergency

### 7. Style Mimicry
**Template:** Write in the style of a specific person/author
**Example:**
> Write a famous fantasy storybook like Harry Potter.

### 8. Professional Writing
**Template:** `You are a [job title]. Write a [document type] about [topic].`
**Example:**
> You are an AI Engineer. Write a list of components/tools used to fine-tune a model

## C. Few-Shot Prompt Templates

### 9. Classification Template
**Template:** Provide examples and ask for classification
**Example:**
```
The film was excellent. → Positive
More voilence in the film. → Negative
Comedy scenes are good, but there is no continuity. → Neutral
```

### 10. Translation Template
**Template:** Provide translation examples and request new translation
**Example:**
```
Translate to Tamil:
What is LLM in tamil? - பெரிய மொழி மாதிரி
```

### 11. Question Answering Template
**Template:** Show Q&A pattern and request completion
**Example:** 
```
What is the current AI market value?
what is the next project designed by Elon Musk?______
```

## D. Chain-of-Thought (CoT) Templates

### 12. Step-by-Step Reasoning
**Template:** Break down complex problems into steps
**Example:**
>Let's think step by step. If you planning to purchase a laptop. what are the thing you need check before buying a laptop?.
For eample, first check the processor i7 or Mac 4 pro, high memory RAM16GB, storage 512 SSD and graphic card.

### 13. Math Problem Solving
**Template:** Show detailed mathematical reasoning
**Example:**
> Solve step by step: (2+3)-2(6*8) / 2

### 14. Logical Puzzle
**Template:** Break down logic puzzles with reasoning
**Example:**
> A farmer needs to cross a river with a wolf, a goat, and a cabbage. He has a boat, but it can only carry himself and one other item at a time. If left alone, the wolf will eat the goat, and the goat will eat the cabbage. How can he get all three across safely?

## E. Instruction Tuning/Format Control

### 15. Output Formatting
**Template:** Request specific output format
**Example:**
> List down the best performing stocks in NSE. Show the stocks which pay high divident into bullent points.

### 16. Table Generation
**Template:** Request structured comparison
**Example:**
> Compare [iPhone 15], [iPhone 17], and [Samsung] based on [Camera quality, performance, battery life]

### 17. Email Writing
**Template:** Generate professional communication
**Example:**
> You are an expert criket coach. Write an email to all the trainees with the rules and regulations of the cricket academy. 

## F. Contextual Prompts

### 18. Tailored Explanation
**Template:** `Explain [complex topic] to [age group] with [background knowledge]`
**Example:**
> Explain about the quantum computing to a college student with simple understandable format.

### 19. Industry-Specific Context
**Template:** `As a [expert], explain [topic] impact on [industry]`
**Example:**
> As a CEO of the Software company, explain how AI will impact in the current industry

## G. Creative Writing Prompts

### 20. Story Writing
**Template:** `Write about [character] who [goal] but faces [obstacle]`
**Example:**
> write a story about pilot who travel lot but faces struggles during the flying time.

### 21. Poem Writing
**Template:** Create poetry with specific parameters
Write a poem in [style/poetic form] about [theme].
**Example:**
> Write a poem about life with fantasy. 

### 22. Dialogue Writing
Write a realistic dialogue between [Person A] and [Person B] discussing [topic].
**Example:**
> Write a realistic dialogue between a Father and a Son discussing about the cars.

## H. Code & Technical Prompts

### 23. Code Generation
Write a [language] function that [does something].
**Example:**
> Write a Python function to calucate age.

### 24. Debugging Help
Here is some code. Find and fix any errors:
**Example:**
> for i in range(1,10)
    print(i+j)

### 25. API Documentation
Explain how to use the [API name] with an example request and response.
**Example:**
> Explain how to use whoisxml api with an example request and response

## I. Marketing & Business Prompts

### 26. Ad Copywriting
Write a compelling ad for [product/service] targeting [audience].
**Example:**
> You are a politican preparing for a vote campign so create an attractive ad to address the youth.

### 27. Product Description
Write a persuasive product description for [product name].
**Example:**
> You are a product manager. Team has created a stock market analyst application. Write a product description for the Application with the details insight about the product should attract the customers.

### 28. Social Media Post
Create a social media post promoting [event/product/idea] in a friendly tone.
**Example:**
>You are an event manager organizing a event to promote a new shoe brand. Write a casual and friendly description for the event.

## J. Customer Support & Service Prompts

### 29. Response to Complaint
Respond professionally to this customer complaint: [Customer message here]
**Example:**
> You are a manager at a restaurant. The customer had a complaint about the bad service during the visit. Write an email in a polite and professional manner to address the issue.

### 30. FAQ Generator
Generate 5 common FAQs and answers for [topic/product]
**Example:**
> Generate 5 common FAQs and answers for a AI product.

## K. Education & Tutoring Prompts

### 31. Lesson Plan Creation
You are a maths master, so you are going to teach a step-by-step procedure to learn fractions in maths.
**Example:**
> You are a maths master, so you are going to teach a step-by-step procedure to learn Algebra in maths.

### 32. Quiz Generation
Generate a 5-question quiz about [subject/topic].
**Example:**
> You are a computer science teacher. Planning to set up a competition for the students of the class, prepare a quiz with 5 questions and answers for the 12th grade students on the Python programming language. 

### 33. Homework Help
Explain how to solve this [math/science] problem:
**Example:**
> A car travels 150 kilometers at a constant speed of 75 km/h.
How much time does it take to complete the journey?

### L. Advanced Framework-Based Templates

### 34. ReAct Framework
Create a running procedure using the same format:
Thought: model thinks about what to do next
Action: model takes an action
Observation: result of the action
Answer: final answer
**Example:**
> Simulate agent behavior manually for running:

Thought: Set up a meeting with my team to discussion about the project progress.
Action: Kindly check the calendar availability of the team members and choose the available time which works for all.
Observation: Find that the team is available on Wednesday and Thurdays with works for everyone.
Answer: Completed setting up the meeting with the team.

### 35. Tree of Thoughts (ToT)
Generate 3 possible solutions to [problem]. Evaluate each and choose the best one.
**Example:**
> Generaet three possible ways to learn AI, evaluate each method, and choose the best for one.
For example: Learn through youtube channels, self-learning, join AI course.
Determine which method is most effective.

### 36. Self-Consistency Prompting
Solve the following question in 3 different ways and pick the
most consistent answer:
**Example:**
> Which is the best method to invest for savings?. 

## M. Prompt Optimization & Evaluation

### 37. Prompt Refinement
Improve this prompt: "[Original prompt]" Make it clearer, more specific, and structured.
**Example:**
You are a expert prompt engineer. Create a marketing stratagy for the real estate company to prompte the company to increase the sales.
For example: create a ad to promote in social media, live campaings and attractive posters.

### 36. Self-Consistency Prompting
Solve the following question in 3 different ways and pick the
most consistent answer:
**Example:**
> You are a expert product manager. Provide step by step process to create a common product for the social media marketing which handles different products. Choose the best one to promote the product.

### 38. Prompt Grading Rubric
Rate this output based on the following criteria (1-5):
Relevance: Task should directly address the specific prompt.
Accuracy: Create accurate 
Clarity:
Fluency:
Creativity:
Final Score: Evaluate the Final score
The prompt Grading template to from the list of mobile product.
Output: Find the best product with different mobiles: iPhone, Samsung, Redmi Note, Motorola, Nokia.

Clarity: clearly worded and easy to understand? Ambiguity should be minimal.	
Fluency: Does the prompt focus on one or more of the mentioned mobile brands (iPhone, Samsung, Motorola, Nokia)?	
Accuracy: Is the prompt accurate and tailored to the features, models, or unique aspects of the selected brand(s)?	
Creativity:	Is the prompt action-oriented, giving clear instructions or objectives (e.g., compare, analyze, review, etc.)?	
Format and Structure: Is the prompt well-structured (e.g., uses bullets, proper grammar, concise phrasing)?

### 39. Prompt Iteration Challenge
Take this weak prompt: "[Prompt]"
Now rewrite it 3 times to improve clarity and effectiveness.
**Example:**
> You are a expert stock analyst. List down the best stocks which has high probability to increase up 50% in next 10 years.  

## N. Real-World Application Prompts

### 40. Job Posting Creation
Write a job posting for [position] at [company]. Include responsibilities, requirements, and benefits.
**Example:**
>Write a job posting for a Project Manager at Apple. Include responsibilities, requirements, and benefits.

### 41. Resume Summary Builder
Create a professional summary for a resume based on the following details:
[Experience, skills, achievements]
**Example:**
>Create a resume for a Technology Lead with 13 years of experience, specializing in python and certified AI architect.

### 42. Business Proposal
Write a proposal for [project idea] to [client/investor]. Include objectives, methodology, and benefits
**Example:**
>Write a proposal to train an AI model for the Health care syatem. Include objectives, methodology, and benefits.

## O. Miscellaneous Useful Templates

### 43. Opinion Writing
Write an opinion piece on [topic]. Use persuasive arguments and examples.
**Example:**
> Write an opinion piece on AI vs Human

### 44. Debate Preparation
Prepare arguments for both sides of the debate: "[Debate topic]"
**Example:**
> Prepare arguments for both parties of Russia and Ukraine

### 45. Travel Planning
Plan a 5-day trip to [destination] for [type of traveler]. Include activities, budget, and tips.
**Example:**
> You are a leading expert travel planner company. Create a 5-day travel plan to Bangkok including budget and activities.

### 46. Book/Movie Review
Write a review of [book/movie]. Include plot summary, strengths, weaknesses, and recommendation.
**Example:**
> You are a expert movie reviewer. Write a detailed review of the F1 moive, Include plot summary, strengths, weaknesses, and recommendation.

### 47. Personal Development
Give me actionable advice on how to [goal], including daily habits and mindset shifts.
**Example:**
> Write an article on future investment planning and how to consistently improve investment based on the income.

## P. Prompt Chaining Examples

### 48. Multi-step Research Task
Step 1:
Find out the top 5 causes of AI revolution.

Step 2:
Based on those causes, suggest 5 partical solutions can adopt quicly to be on the AI race.

### 49. Idea to Execution
Pick 5 small-scale digital businesses and evaluate which one has performed the best in recent years, specifically in 2025.

Example:

Stock Market Analyzer Service

Online AI agent Development for business needs.

Web Site development using AI 

Online Learning platform

Content Development for blogs

Evaluate their recent performance and pick the best-performing business in 2025.

## Q. Prompt Template Generator

### 50. Universal Prompt Builder

[Role] + [Task] + [Context] + [Example]+ [Format]
**Example:**
> Role: You are a excellent story writer for the children. 
Task: Create a bedtime story for the kids with polite words and in well explained manner.
Context: Write a story for children's under age of 10 in well understandable format. Include special animal and natural images which explain the story. 
Example: Fictional and Non-Fictional stories.
Format: Story should be within 50 words with images.

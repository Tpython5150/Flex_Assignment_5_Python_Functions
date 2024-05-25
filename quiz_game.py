'''
The Quiz game 4 Task 1,2,3

The aim of this assignment is to create a qui game that asks questions and checks answers.

Task 1: Develop a list of questions and answers.
Task 2: Write a function that quizzes the user and takes their answers.
Task 3: Score the quiz and five the user feedback on their performance.

'''
import math
questions = ["What is the price of the new baseball bat?",
             "What is the price of the VW Bug?",
             "What is the price of the Windows tablet?",
             "What is the price of the wireless mouse?"]

correct_answers = [125.00, 12000.00, 175.00, 12.99]
             
def quiz():
    score = 0
    
    for i in range(len(questions)):
        user_answer = (float(input(questions[i] + " ")))
        
        if user_answer == correct_answers[i]:
            print("Correct")
            score += 1
        else:
            print("Try Again!")
            print(f"Your score is {score}/{len(questions)}.")
        
    print(f"Your final score is {score}/{len(questions)}.")
    
quiz()



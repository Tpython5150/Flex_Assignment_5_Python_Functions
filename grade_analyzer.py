'''
The Grade Anayzer 3 Task 1,2,3

Objective: The aim f this assignment is to analyze a set of grades and provide statistics.

Task 1: Code a function to calculate the average grade.

Task 2: Implement a functon to find the highest and lowest grade.

Task 3: Create a feature that categorizes grades into letter grades. (A, B, C, D, etc.)
'''
import math

grades = [88.8, 70.00, 91.4, 79.5, 90.00, 65.00]
letter_grades = []
number_grades =len(grades)

def calculate_average_grade():
    total_grades = sum(grades)
    #print(round(total_grades, 2))
    average = total_grades/number_grades
    #print(round(average, 2))
    print(f"The averages of all grades {average:.2f}")
    
def highest_lowest_grades():
    highest = max(grades)
    lowest = min(grades)
    print(f"Highest grade: {highest}")
    print(f"Lowest grade: {lowest}")

def list_grades():
    for grade in grades:
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        elif grade >= 60:
            letter_grades.append('D')
        else:
            letter_grades.append('F')
    print(f"Letter Grades: {letter_grades}")
        #how do I get them to print once instead of going through each iteration?
    
        
calculate_average_grade()
highest_lowest_grades()
list_grades()
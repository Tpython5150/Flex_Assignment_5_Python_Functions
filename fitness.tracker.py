'''
The Fitness Tracker 5 Task 1,2,3

The aim of this assignment is to create a program that tracks fitness activities and calories
burned.

Task 1: Develop a function to log different fitness activities and their duration. For instance,
        actvities = ['Dancing', 'Swimming', 'Biking'] and duration = [ 10, 20, 15] where Dancing
        corresponds to 10 minutes, Swimming corresponds to 20 minutes,  and Biking corresponds
        to 15 minutes.
        
Task 2: Write a simple function that estimates calories burned based on the activity and dur-
        ation.  For instance, Total Calories burned = Duration (in minutes)*3.5
        
Task 3: Create a summary function that provides a report of all activities and total calories 
        burned for the day.        


'''

activities = ['Dancing', 'Swimming', 'Biking']
duration_time = [10, 25, 15]

def activities_duration():
    for i in range(len(activities)):
      print(f"Activity: {activities[i]} - Duration: {duration_time[i]} minutes.")
      
def calories_burned():
    for i in range(len(duration_time)):
        calories = float(duration_time[i]) * 3.5
        print(f"Calories burned during {activities[i]}: {calories:.2f} calories")
def summary():
    print("Active Summary")
    for i in range(len(activities)):
        calories = float(duration_time[i]) * 3.5
        print(f"Activities: {activities[i]}, Duration: {duration_time[i]}, Calories burned: {calories:.2f}")  
        
activities_duration()
calories_burned()
summary()
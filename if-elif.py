#1. Grade Classification
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")

#2. Determine the Day Type
day = "Saturday"

if day == "Monday":
    print("Start of the work week.")
elif day in ["Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("It's a weekday.")
elif day in ["Saturday", "Sunday"]:
    print("It's the weekend!")
else:
    print("Invalid day.")
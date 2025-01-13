workinDays = int(input("Enter number of working days : "))
absentDays = int(input("Enter number of absent days : "))

totalDays = workinDays + absentDays

percentage = (workinDays / totalDays) * 100
print("Attendance : ", percentage, "%")

if percentage <75:
    print("You are not eleigible to sit for exam.")
else: 
    print("You are eligible to sit for exam.")
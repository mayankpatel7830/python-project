student={
    "Ravi": 67,
    "Raja": 72,
    "Rash": 52
}
highest=0
topper=""

for key in student:
    print(key,student[key])

    if student[key]>60:
       print("Fail:" , key)

    if student[key]<60:
       print("Pass:" , key)

    if student[key]>highest:
       highest=student[key]
       topper=key



print("Topper:" , topper,highest)

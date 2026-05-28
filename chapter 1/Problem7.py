marks={
    "X" : 10,
    "Y" : 50,
    "Z" : 30
}
for key in marks:print(key,marks[key])

highest=0
topper=""

for key in marks:
    if marks[key]>highest:
        highest=marks[key]
        topper=key
print("Topper",topper,highest)

total=0
average=""

for key in marks:
    total=total+marks[key]
average=total/len(marks)
print("Total:",total,"Average",average)
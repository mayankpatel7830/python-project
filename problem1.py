marks={
    "Ravi" : 72,
    "Rash" : 65,
    "Raja" : 83
}

for key in marks:print(key,marks[key])


def function_topper(marks):
    highest=0
    topper=""

    for key in marks:
        if marks[key] > highest:
         highest=marks[key]
         topper=key


    return topper,highest   

name,score = function_topper(marks)
print("Topper",name,score)

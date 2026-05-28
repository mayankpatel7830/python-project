marks ={
    "Ravi" : 62,
    "Raja" : 95,
    "Rash" : 42
}

for key in marks : print(key ,marks[key])

highest = 0

for key in marks : 
    if marks[key] > highest:  

     highest = marks[key]

print(highest)


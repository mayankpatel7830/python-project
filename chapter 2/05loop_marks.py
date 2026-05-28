# marks ={         # marks is my directory
#  #  "keys"  :value 
#     "Rahul" : 45, 
#     "Raja"  : 85,
#     "Rajesh": 93
# }
# total = 0
# print(marks)

# for key in marks : total = total + marks[key]

# print(total)

marks = {
    "Ravi" : 53,
    "Raja" : 62,
    "Rash" : 83
}
total = 0
for key in marks :total = total + marks[key]
    
average = total/ len(marks)

print("Total :",total)
print("Average :",average)
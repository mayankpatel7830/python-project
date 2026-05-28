employee = [
    {"Name" : "Ravi", "City" : "Delhi"},
    {"Name" : "Aman", "City" : "Mumbai"},
    {"Name" : "Neha", "City" : "Pune"}
]
print(employee[0]["Name"])
print(employee[2]["City"])


employee[1]["City"]="Chennai"
employee[0]["Skill"]="Python"

print(employee[1]["Name"],employee[1]["City"])
print(employee[0]["Name"],employee[0]["Skill"])
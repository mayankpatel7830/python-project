employee=[
    {"Name":"Ravi" ,"City":"Delhi"  ,"Salary":25000},
    {"Name":"Aman" ,"City":"Mumbai" ,"Salary":40000},
    {"Name":"Raj"  ,"City":"Chennai","Salary":32000},
    {"Name":"Karna","City":"Kolkata","Salary":50000},
    {"Name":"Ankit","City":"Mysore" ,"Salary":28000}
]
# employee[2]["City"]="Kolkata"
    
for key in employee:
    if ((key["Salary"]>30000) and (key["Name"][-1] in ["a","A"]) 
        and (key["City"][0] in ["M"]) or (key["City"][-1] in ["a"])):

     print(key["Name"],key["City"],key["Salary"])
# print(employee)

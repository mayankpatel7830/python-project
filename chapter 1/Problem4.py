marks={"Adii":50,"Adii":83,"Back":80,"Caat":63}

def show_all():
 for key in marks:
      print(key,marks[key])

def add_student():
   name=input("Enter name:")
   score=int(input("Enter marks:"))
   marks[name]=score

for i in range(3):
   add_student()

show_all()


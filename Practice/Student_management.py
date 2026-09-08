students=[{"id":1, "name": "Aarav Sharma", "course": "Python Core", "marks":88.50, "grade":"A"},
          {"id":2, "name": "Diya Patel", "course": "Data Science", "marks":74.00, "grade":"B"},
          {"id":3, "name": "Rohan Nair", "course": "Web Architecture", "marks":45.00, "grade":"F"},
          {"id":4, "name": "Sneha Kulkarni", "course": "Python Core", "marks":92.00, "grade":"A"},
          {"id":5, "name": "Amit Verma", "course": "Data Science", "marks":63.50, "grade":"C"}]
id_counter=5
def menu():
    menu="""    1. Enroll Student
    2. Cohort Directory
    3. Query Records
    4. Revise Evaluation           
    5. Purge Record
    6. Save to json
    7. Load from json
    8. Terminate"""

    print(menu)
    a=int(input("Enter your choice: "))
    return a

def enroll(name, course, marks):
    global id_counter
    if(name==" "):
        print("Enter valid name")
        return
    if course==" ":
        print("Enter valid course name")
        return
    if marks<0 and marks>100:
        print("Enter valid marks")
        return

    if(marks>85.0):
        grade="A"
    elif marks>70.0 and marks<=85.0:
        grade="B"
    elif marks>50.0 and marks<=70.0:
        grade="C"
    else:
        grade="F"

    students.append({"id":id_counter,"name":name, "course":course, "marks":marks, "grade":grade})
    id_counter+=1

    print("Student added successfully")


def search():
    try:
        s="""1. Search by id
        2. Search by name
        3. Search by course name"""
        print(s)

        inp=int(input("Enter how you want to search: "))

        if inp==1:
            i=int(input("Enter the id: "))
            search_by_id(i)
        elif inp==2:
            n=input("Enter the name to search: ")
            search_by_name(n)
        elif inp==3:
            c=input("Enter the course to search: ")
            search_by_coursename(c)
        else:
            print("Enter valid input")
    except:
        print("Try again with integer input.")

def cohort(students):
    display_student(students)
    # print("-"*80)
    # print(f'{"Id":<5}{"Candidate Name":<20}{"Course/Module":<20}{"Marks(100)":<20}{"Awarded Grade":<10}')
    # print("-"*80)
    # for i in students:
    #     id,name,course,marks,grade=i.values()
    #     print(f'{id:<5}{name:<20}{course:<20}{marks:<20}{grade:<10}')
    # print("-"*80)
    
def search_by_id(id):
    
    res=[a for a in students if a['id']==id]
    if(res):
        print("Student found")
        display_student(res)

    else:
        print("Student not found")

    return res

def search_by_name(name):
    res=[a for a in students if a["name"]==name]
    if(res):
        display_student(res)
    else:
        print("Student not found")

def search_by_coursename(course):
    res=[a for a in students if a["course"]==course]
    if res:
        display_student(res)
    else:
        print("Student not found")

def display_student(res):
    print("-"*80)
    print(f'{"Id":<5}{"Candidate Name":<20}{"Course/Module":<20}{"Marks(100)":<20}{"Awarded Grade":<10}')
    print("-"*80)
    for i in res:
        id,name,course,marks,grade=i.values()
        print(f'{id:<5}{name:<20}{course:<20}{marks:<20}{grade:<10}')
    print("-"*80)

def purge_record():
    try:
        id=int(input("Enter the id for which you want to delete: "))
        a=search_by_id(id)
        ans=input("Are you sure you want to delete (y/n): ").lower()
        if ans=="y":
            del a['id'] 
            print("Entry deleted successfully.")
            display_student(students)
        else:
            print("Okayy continue with next process!!!")
    except:
        print("Enter valid input as mentioned.")


def update():
    id=int(input("Enter the id for which you want top update the details: "))
    a=search_by_id(id)
    if a:
        n=input("Enter the name to update: ")
        c=input("Enter the course to update: ")
        m=int(input("Enter the marks to update: "))

        a[0].update({"name":n, "course":c, "marks":m})

        print("Updation done successfully!!!")

    else:
        print("Record not found try adding first.")



def main():
    while True:
        m=menu()
        match m:
            case 1:
                name=input("Enter name: ")
                course=input("Enter the course: ")
                marks=int(input("Enter the marks: "))
                enroll(name, course, marks)
            case 2:
                cohort(students)
            case 3:
                search()                #query records
            case 4:
                update()                #revise evaluation
            case 5:
                purge_record()          #purge record i.e. delete
            case 6:
                ...
            case 7:
                ...
            case 8:
                break
            case _:
                print("Enter valid input")

    # print(students)
main()

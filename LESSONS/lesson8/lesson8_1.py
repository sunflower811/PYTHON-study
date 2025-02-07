import random
def get_names(nums:int=2)->list[str]:
    with open('names.txt',encoding='utf-8',mode='r') as file:
        names_str=file.read()
    names:list[str]=names_str.split(sep='\n')
    names=random.choices(names,k=nums)
    return names
def generate_students(names:list[str])->list[dict]:
    students:list[dict]=[]
    for name in names:
        #print(name)
        chinese=random.randint(50,100)
        English=random.randint(50,100)
        Math=random.randint(50,100)
        student={'name':name,'chinese':chinese,'english':English,'math':Math}
        students.append(student)
    return students

nums=int(input("students num(max=10)"))
students_names:list[str]=get_names(nums=nums)
students=generate_students(names=students_names)
print(students)
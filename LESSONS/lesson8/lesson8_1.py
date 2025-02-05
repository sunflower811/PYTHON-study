import random
def get_names(nums:int=2)->list[str]:
    with open('names.txt',encoding='utf-8',mode='r') as file:
        names_str=file.read()
    names:list[str]=names_str.split(sep='\n')
    names=random.choices(names,k=nums)
    return names
nums=int(input("students num(max=10)"))
students_names:list[str]=get_names(nums=nums)
for name in students_names:
    print(name)
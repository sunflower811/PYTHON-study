import random
def name_G(n:int=2)->list[str]:
    with open('names.txt',encoding='utf-8',mode='r') as file:
        name_str=file.read()
    names:list[str]=name_str.split(sep='\n')
    Names=random.choices(names,k=n)
    return Names
    
class BMI():
    def __init__(self,Names,height:int,weight:int):
        self.name=Names
        self.weight=weight
        self.height=height

    def get_BMI(self)->float:
        return round(self.weight/(self.height/100)**2,ndigits=2)
    
    def get_status(self)->str:
        B=self.get_BMI()
        if B<18.5:R='tooo light'
        elif 24>B>=18.5:R='normal'
        else :R='tooo heavy'
        return R

def G_state(Names:list[str])->[BMI]:
    students:list[BMI]=[]
    for name in Names:
        H=random.randint(140,190)
        W=random.randint(50,110)
        B=W/(H*H)*10000
        student_status=BMI(name,H,W)
        students.append(student_status)
    return students

if __name__=='__main__':
    n=int(input("Gine me a num(<10): "))
    names:list[str]=name_G(n=n)
    students:list[BMI]=G_state(names=names)
    for student in students:
        print(f'Name:{student.name}')
        print(f'Height:{student.height}')
        print(f'Weight:{student.weight}')
        print(f'BMI:{student.get_BMI()}')
        print(f'State:{student.get_status()}')
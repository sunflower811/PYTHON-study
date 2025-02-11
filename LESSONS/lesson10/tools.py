import random
def name_G(nums:int=2)->list[str]:
    with open('names.txt',mode='r',encoding='utf-8') as file:
        names_str=file.read()
    names:list[str]=names_str.split(sep='\n')
    names=random.choices(names,k=nums)
    return names
    
class BMI():
    def __init__(self,name:str,height:int,weight:int):
        self.name=name
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

def G_state(names:list[str])->[BMI]:
    students:list[BMI]=[]
    for name in names:
        H=random.randint(140,190)
        W=random.randint(50,110)
        student_status=BMI(name,H,W)
        students.append(student_status)
    return students
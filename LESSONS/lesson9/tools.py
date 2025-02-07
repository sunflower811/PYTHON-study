import random #module
def name_G(n:int=2)->list[str]:
    with open('names.txt',encoding='utf-8',mode='r') as file:
        name_str=file.read()
    names:list[str]=name_str.split(sep='\n')
    Names=random.choices(names,k=n)
    return Names
    
def G_state(Names):
    A:list[dict]=[]
    for name in Names:
        H=random.randint(140,190)
        W=random.randint(50,110)
        B=W/(H*H)*10000
        if B<18.5:b='tooo light'
        elif 24>B>=18.5:b='normal'
        else :b='tooo heavy'
        state={'name':name,'Height(cm)':H,'Weight(kg)':W,'BMI':f'{B:.4f}','Status':b}
        A.append(state)
    return A
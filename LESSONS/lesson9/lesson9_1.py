import tools

if __name__ =='__main__':
    n=int(input("Gine me a num(<10): "))
    names=tools.name_G(n)
    State:list[dict]=tools.G_state(names)
    for people in State:
        for key,value in people.items():
            print(f'{key}:{value}')
        print("----------------")

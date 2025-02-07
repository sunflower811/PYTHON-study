from gear import widget

if __name__ =='__main__':
    n=int(input("Gine me a num(<10): "))
    names=widget.name_G(n)
    State:list[dict]=widget.G_state(names)
    for people in State:
        for key,value in people.items():
            print(f'{key}:{value}')
        print("----------------")

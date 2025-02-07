from gear.widget import name_G,G_state
#import tools

if __name__ =='__main__':
    n=int(input("Gine me a num(<10): "))
    names=name_G(n)
    State:list[dict]=G_state(names)
    for people in State:
        for key,value in people.items():
            print(f'{key}:{value}')
        print("----------------")

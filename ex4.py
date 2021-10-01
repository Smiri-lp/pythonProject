
# Need fixing
name = str(input("Write your name here: "))

def capitalize(name):
    nr_kapitaleve = 0
    for x in name[:4]:
        if x.upper() == x:
            nr_kapitaleve +=1
            if nr_kapitaleve >= 2:
                print(name.upper())
            else:
                print(name)
# print(capitalize(name))
capitalize(name)
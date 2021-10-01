# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# n = int(input("enter the number: "))
#
# def ex_1(n):
#     if (n % 2)==0:
#         print('True')
#     else:
#         print('False')
# ex_1(n)

# num = int(input("Choose your number: "))
# store_num = num
# rev_num = 0
#
# while(num>0):
#     dig = num%10
#     rev_num=rev_num*10+dig
#     num = num // 10
#
# if(store_num==rev_num):
#     print(f"This is what you are looking for {rev_num}")
# else:
#     print("Noo so sad :(")


# import math
#
# num = int(input("Let us know your number: "))
#
# def power(num):
#     if (num>0 and math.log2(num).is_integer()):
#         print(f"{num} ky plotpjestohet")
#     else:
#         print(f"{num} sbohet gjo")
# power(num)


#
# # Nuk funksionon mire
# name = str(input("Write your name here: "))
#
# def capitalize(name):
#     nr_kapitaleve = 0
#     for x in name[:4]:
#         if x.upper() == x:
#             nr_kapitaleve +=1
#             if nr_kapitaleve >= 2:
#                 print(name.upper())
#             else:
#                 print(name)
# # print(capitalize(name))
# capitalize(name)


# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# for x in list1:
#     if x > 150:
#         break
#     elif x % 5 == 0:
#         print(x)


# words = ['Lorem', 'ele', 'sit', 'incididunt', 'a', 'su', 'dom', 'ouch', 'ipsum']
#
# length_wor = 'hello'
# for x in words:
#     if len(x) == len(length_wor):
#         print(x)

# def n_letter(my_string):
#     sample_dictionary={}
#     for word in my_string:
#         words=len(word)
#         if words in sample_dictionary:
#             sample_dictionary[words].add(word)
#         else:
#             sample_dictionary[words] = {word}
#     print(sample_dictionary)
#     return sample_dictionary
# n_letter(['Lorem', 'ele', 'sit', 'incididunt', 'a', 'su', 'dom', 'ouch', 'ipsum'])

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
# it = Person('Accul', 'Otal')
# full_name = it.get_full_name()
# print(f"{full_name}")
#
# class Student(Person):
#     pass
# new = Student("Mike", "Olsen")
# full_name = new.get_full_name()
# print(f"{full_name} -st")
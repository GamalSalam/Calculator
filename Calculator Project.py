
''' calculator project'''

# add function
def add(n1,n2):
    return n1+n2

# substract function
def subtract(n1,n2):
    return n1-n2

# multiply function

def multiply (n1,n2):
    return n1*n2

# divid fuction

def divid(n1,n2):
    return n1/n2

dic_operation={'+':add, '-': subtract, '*': multiply, '/':divid}

from sys import exit

def calculator():
    num1=float(input('enter the first number; '))
    continue_operation=True
    while continue_operation:
        for sign in dic_operation:
            print(sign)
        ask_operation= input('which operation do you wnat? ')
        num2=float(input('enter the second number; '))

        answer = dic_operation[ask_operation](num1,num2)
        print(f'{num1} {ask_operation} {num2} = {answer}')

        ask_again=input(f'do you want to contiue operation with {answer} type y, or start new calcualtion type n, or type e to exit ')
        if ask_again== 'y':
            num1=answer
        elif ask_again=='e':
            exit()
        else:
            continue_operation=False
            calculator()
calculator()



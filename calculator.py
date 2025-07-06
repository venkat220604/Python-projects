a=int(input())
b=int(input())
c=input("enter the symbol + - * / % ** //")
match c:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '%':
        print(a%b)
    case '**':
        print(a**b)
    case '//':
        print(a//b)
    case _:
        print("the given symbol is not avalible")



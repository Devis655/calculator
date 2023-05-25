print('''
+ add
- subtract
* multiplication
/ divide
''')
a = int(input("Enter the value : 1 ="))
b = int(input("Enter the value : 2 ="))
opr = input("Enter the Opr..")
if opr == "+":
    print(a+b)
elif opr == "-":
    print(a-b)
elif opr == "*":
    print(a*b)
elif opr == "/":
    print(a/b)
else:
    print("invalid opr...")
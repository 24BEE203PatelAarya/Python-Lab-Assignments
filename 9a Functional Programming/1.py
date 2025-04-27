#1.Define three functions fun(), disp() and msg(). Store them in a list and call them one by one in a loop.

def fun():
    print('Function fun() is called')

def disp():
    print("Function disp() is called")

def msg():
    print("Function msg() is called")

lst = [fun, disp, msg]

for func in lst:
    func()
    


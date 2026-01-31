def hello_world():
    print("Hello World!")

hello_world() # cara print fungsi nya

def sum(num1=0, num2=0): # ini itu default value nya
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum(7, 2)
print(total)

def multiple_items(*args): # "*" itu maksudnya bisa menerima banyak input (args itu bisa diganti")
    print(args) 
    print(type(args))

multiple_items("Dzaky", "Dapa", "Ripak")

def mult_named_items(**kwargs): # kwargs = keyword arguments, "**" bisa menerima banyak input yang PAKAI NAMA
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Abduh", last="Dzaky")



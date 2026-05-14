# funkcja wewnętrzna, funkcja zagnieżdzona
# uzywane w dekoratorach
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    # fun2()
    return fun2  # zwrócenie adresu funkcji (referencji)


fun1()  # To jest fun1
xfun = fun1()  # zwraca adres fun2
print(xfun)  # <function fun1.<locals>.fun2 at 0x000001EF605C7270>
print(type(xfun))  # <class 'function'>

xfun()
# To jest fun2
# print(fun1()())
xfun()
xfun()
xfun()
xfun()
xfun()

yfun = fun1()
print(yfun())

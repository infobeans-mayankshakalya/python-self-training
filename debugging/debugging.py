from mydebugmodule import fun2
def fun1(n):
    print('fun1', n)
    fun2(n)
n = int(input('Enter the number'))
fun1(n)
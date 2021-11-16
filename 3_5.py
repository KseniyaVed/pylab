Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#посчитать произведение чисел, кратных 3 и 5

числа=[1,2,3,4,5,6,5,4,55,4,155,6,7]

произведение=1
for x in числа:
    if x //5 == x/5:
        произведение *= x
    if x //3 == x/3:
        произведение *= x
        
print(произведение)
SyntaxError: multiple statements found while compiling a single statement

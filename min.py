Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
A = [3,4,2,1,0,8,9,-1,100,0]
min = A.pop()
while A:
    a = A.pop()
    if a < min:
        min = a
        print(min)
        
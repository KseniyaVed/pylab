Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# заменить все буквы с х на у

исходная_строка ="rtyui zxcv xxx yyy"
новая_строка =""

for a in исходная_строка:
    if a == "x":
        новая_строка +="y"
    else:
        новая_строка += a
        
print(исходная_строка)
print(новая_строка)

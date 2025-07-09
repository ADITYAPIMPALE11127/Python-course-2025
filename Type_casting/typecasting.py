a = 24423
print(a)
print(type(a)) # type is int 
b = "24423"
print(b)
print(type(b)) # type is string 

# converting int to string 
c = str(a)
print(c)
print("c is of type",type(c))

# converting str to int 
b = int(b)
print(b)
print(type(b))

# converting str to float
string1 = "12233"
print(type(string1))
string1 = float(string1)
print(string1)


#converting int to bool
num = 2123
print(num,type(num))
num = bool(num)
print(num,type(num))
x = 4
y = "Pudge"

print(x)
print(y)

a = str(3)
b = int(3)
c = float(3)
print(a, b, c)

d = 5
e = "John"
print(type(x))
print(type(y))

myvar = "Invoker"
my_var = "Lina"
_my_var = "Axe"
myVar = "IO"
MYVAR = "Enigma"
myvar2 = "Puck"
print(myvar, my_var, _my_var, myVar, MYVAR, myvar2)

f, g, h = "Orange", "Banana", "Cherry"
print(f)
print(g)
print(h)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
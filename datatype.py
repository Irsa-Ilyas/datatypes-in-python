# python data types
# A Numeric data type(3)
# 1.integer(0-9 both positove nad negitive positive and negitive both)
x:int=10
print(type(x))


y:int=-0
print(type(y))

# 2.Float(0.00-0.99 both positove nad negitive positive and negitive both )
a:float=10.00
print(type(a))


b:float=-0.99
print(type(b))

# 3.Complex (a+bj imaginary part should be j otherwise it will give error)
c:complex=2+0j
print(type(c))

d:complex=2+1j
print(type(d))

num_complex: complex = 2 + 3j

print(type(num_complex), " num_complex = ", num_complex) 

# B boolean
am_i_learning_puthon:bool=True
# print(type(am_i_learning_puthon ) , am_i_learning_puthon , " i am learning python")//comma will generate a space

#  C Sequense Data type
# 1.string
single_colon:str='"hello irsa"'
double_colon:str="hello irsa"

triple_colon:str="""'hello irsa'"""
multi_colon:str='''hello
 irsa
 how are you
      have you completed your assignment?
                            are you enjoyning working on python?
      '''
print(type(single_colon), single_colon)
print(type(double_colon), double_colon)
print(type(triple_colon), triple_colon)
print(type(multi_colon), multi_colon)
# output
# <class 'str'> "hello irsa"
# <class 'str'> hello irsa
# <class 'str'> 'hello irsa'
# <class 'str'> hello
#  irsa
#  how are you
#       have you completed your assignment? 
#                             are you enjoyning working on python?

# 2.List  
# An ordered, mutable collection.
array_types:list=[1,2,3,4.55,2+3j,"helllo"]
print (type(array_types))

#  a.tuples are immutable, meaning their contents cannot be changed after creation,
#  while lists are mutable and can be modified.
# b.syntex diffrence
# c.performance tuple ki ziada huty hai q k content change nahin huta 
# 3 tuple
# An ordered, immutable collection.
array_tuple:tuple=(1,2,3,4.55,2+3j,"helllo")
print (type(array_tuple))

# 4 Range
# Represents a sequence of numbers.
values:range=range(1,10,3)
print(type(values),values)
# output <class range > range( 1,2,3)


values:range=range(1,10,3)
print(type(values), values.step)//3
for i in range(1,10,3):
  print(i)
# output 
# 1
# 4
# 7
# D SETTYPES
#1. SET
# IMMUTABLE UNORDDERED AND CONTAIN UNIQUE VLAUES
my_pet_set:set={1,2,3,4}
print(type(my_pet_set),my_pet_set)
# set is mutable can add delete update values and low performing
# syntax difference in set and frozenset


#2. FROZENSET
# IMMUTABLE UNORDDERED AND CONTAIN UNIQUE VLAUES
my_fruit_set=frozenset([1,2,3,4])
print(type(my_pet_set),my_pet_set)

# frozenset is immutable and high performig cannot add delete or update values

# E None
# None represents the absence of a value or a null object reference.
x=None
print(type(x))
print(id(x))

x=None
y=None
print(type(x))
print(type(y))
print(id(x)==id(y))
print()
# == x or y ki values ko compare krraha haii jab k is momory mein address ko compare krraha haii
#  or memory mein har elemnt ki id diifferent huty hai
# == values ko comoare krta haii
# is memory mei location ko compare krta haii
# print(id(x) is id(y)) ///yeh false return krega 
print(x is y)

# F id


# id returns unque memory address
# Python optimizes memory by reusing small integers (-5 to 256), so their id() might be the same:
# is mein bhi yahib huga
a = 100
b = 100
print(id(a) == id(b)) 
e=257
f=257
print(id(e) == id(f)) 


c = 1000
d = 1000
print(id(c) == id(d)) 
# F id



# Integer Interning in Python 
# 🔹 What is Integer Interning?
# In Python, integers between -5 to 256 are interned (cached), 
# meaning they are pre-stored in memory and reused.

# Whenever you create an integer within this range, Python does not create a new object; 
# instead, it reuses the same object from its interned pool.
x = -6
y = -6
z = x

print("Value of x = " + str(x) + ", and id(x) = " + str(id(x)))
print("Value of y = " + str(y) + ", and id(y) = " + str(id(y)))
print("Value of z = " + str(z) + ", and id(y) = " + str(id(z)))

print("\n ===================== \n")

a = 257
b = 257
c = a

print("Value of x = " + str(a) + ", and id(a) = " + str(id(a)))
print("Value of y = " + str(b) + ", and id(b) = " + str(id(b)))
print("Value of z = " + str(c) + ", and id(c) = " + str(id(c)))
shark1_age = 300
shark2_age = 300

print("Value of shark1_age = " + str(shark1_age) + ", and id(shark1_age) = " + str(id(shark1_age)))
print("Value of shark2_age = " + str(shark2_age) + ", and id(shark2_age) = " + str(id(shark2_age)))

if(shark1_age == shark2_age): 
  print("shark1_age & shark2_age have same age")
else:
  print("shark1_age & shark2_age have different age")

print(" ===================== ")

if(id(shark1_age) == id(shark2_age)):
  print("shark1_age & shark2_age have same id")
else:
  print("shark1_age & shark2_age have different id")

# G Type Casting
# Type casting meAns aik data type ko dosry data type mein convert krna
# implicit casting jo python khud sy kta haii
# explicit jo hum khud krty hain usiing bultin function'
x = 10   # Integer
y = 2.5  # Float

z = x + y  # Python automatically converts 'x' to float
print(type(z), z)  # <class 'float'> 12.5
# Agar + operator use karna ho to string aur number ka type match karna zaroori hai, jaise:
print("Age: " + str(25))  
# aik string direct integer mein conver nahin husakta
# A string with a decimal number must first be converted to float before converting to int.
s: str = 25
f2: float = float(s)
print("Value of f2 = " + str(f2) + ",  Type of i = " + str(type(f2)))
i2 = int(float(s))  # First convert to float, then to int
print("Value of i2 = " + str(i2) + ", Type of i = " + str(type(i2)))






# H isinstance

# The isinstance() function in Python is used to check if an object (first argument)
#  is an instance of a class (second argument). It returns `True` if the object is an instance of
#   the class, and `False` otherwise.

# The syntax of the isinstance() function is as follows:

# isinstance(object, classinfo)
# object is the object to be checked.
# classinfo is the class or a tuple of classes to check against.

a=1
b=[1,2,3]
c="hello"
d=12.20
print("check " + str(isinstance(a,int)))
print("check " + str(isinstance(b,list)))
print("check " + str(isinstance(c,str)))
print("check " + str(isinstance(d,float)))
# retuens true
a=1
b=[1,2,3]
c="hello"
d=12.20
print("check " + str(isinstance(a,float)))
print("check " + str(isinstance(b,str)))
print("check " + str(isinstance(c,list)))
# print("check " + str(isinstance(d,int)))returns false
# isinstance multiple data types bhi check krsakta ahii
x=2
print(isinstance(x,(float,int)))
# returns true

print("hello \"world\"")
# //syntax/"/" agr koii cheez ""string mein print krwani haii

# Truthy andFalsy Vlaues

if 2 :
  print(True)
else:
  print(False)
  # true
  if 0 :
       print(True)
    
  else:
    print(False)
  # false
# print("check: bool(\"55\")             = ", bool("55"))//true
# print("check: bool(\"\")               = ", bool(""))//false
# print("check: bool([1, 2, 3])        = ", bool([1, 2, 3]))//true
# print("check: bool({\"key\", \"value\"}) = ", bool({"key", "value"}))//true
# print("check: bool([])               = ", bool([]))//false 
# print("check: bool({})               = ", bool({}))//false









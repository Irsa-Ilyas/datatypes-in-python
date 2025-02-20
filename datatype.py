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
print(type(am_i_learning_puthon ) , am_i_learning_puthon , " i am learning python")//comma will generate a space

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

# froxenset is immutable and high performig cannot add delete or update values





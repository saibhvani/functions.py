#String Transform Functions

#capitalize
#Syntax:variable.capitalize()

name="saibhavani"
print(name.capitalize())

#Title
#syntax:variable.title()

name="sai bhavani"
print(name.title())

#upper
#syntax:variable.upper()

name="saibhavani"
print(name.upper())

#lower
#syntax:variable.lower()

name="SAI BHAVANI"
print(name.lower())

#casefold
#syntax:variable.casefold()

name="SAI BHAVANI"
print(name.casefold())

#swapcase
#syntax:variable.swapcase()

name="saibhavani"
print(name.swapcase())


#String Check Functions

#isnumeric
#syntax:variable.isnumeric()
number="124"
print(number.isnumeric())

#isalphanumeric
#syntax:variable.ialnum()

num="Saibhavani123"
print(num.isalnum())

#isdecimal
#syntax:variable.isdecimal()

num="Saibhavani"
print(num.isdecimal())

#isdigit
#syntax:variable.isdigit()

num="12333"
print(num.isdigit())

#isascii
#syntax:variable.isascii()

num="abc"
print(num.isascii())

#isupper
#syntax:variable.isupper()

num="saibhavani"
print(num.isupper())

#islower
#syntax:variable.islower()

num="SAI BHAVANI"
print(num.islower())

#isspace
#syntax:variable.isspace()

num=" "
print(num.isspace())

#isidentifier
#syntax:variable.isidentifier()

num="@"
print(num.isidentifier())

#isprintable
#syntax:variable.isprintable()

num="Saibhavani"
print(num.isprintable())

#istitle
#syntax:variable.istitle()

num="sai bhavani"
print(num.istitle())


#String Search Functions

#index
#syntax:variableName.index(string/char)

email="saibhavani@gmail.com"
print(email.index("@"))

#rindex
#syntax:variableName.rindex(string/char)

email="saibhavani@gmail@.com"
print(email.rindex("@"))

#rfind
#syntax:variableName.rfind(string/char)

email="saibhavani@gmail@.com"
print(email.rindex("@"))

#startswith
#syntax:variableName.startswith(string/char)

name="Saibhavani"
print(name.startswith("Saibhavani"))

#endswith
#syntax:variableName.endswith(string/char)

name="Saibhavani"
print(name.endswith("Saibhavani"))


#list methods

#Append
#syntax:lst.append()

l=[]
print(l.append("Saibhavani"))
print(l)

#insert
#syntax:lst.insert(index,item)

l=["Saibhavani","Sravya"]
print(l.insert(1,"Saibhavani"))
print(l)

#Extend
#syntax:lst.extend(lst1)

name=["chinni","Sravya"]
name1=["bhavani","saibhavani"]
name.extend(name1)
print(name)

#count
#syntax:lst.count(item)

name=["sravya","chinni"]
print(name.count("Saibhavani"))

#index
#syntax:lst.index(item)

name=["Bhavani","Sravya"]
print(name.count("Saibhavani"))

#pop
#syntax:lst.pop()

name=["chinni","bhavani"]
print(name.pop())

#remove
#syntax:lst.remove()

name=["bhavani","chinni"]
print(name.remove("chinni"))
print(name)

#clear
#syntax:lst.clear(item)

name=["bhavani","sravya","Chinni"]
print(name.clear())
print(name)

#sort
#syntax:lst.sort()

a=[1,2,5,3]
a.sort()
print(a)

#reverse
#syntax:lst.reverse()

a=[1,2,5,3]
a.reverse()
print(a)


#Tuple Methods

#count
#syntax:tpl.count(item)

tpl=tuple((1,4,3,5,4))
print(tpl.count(4))

#index
#syntax:tpl.index(item)

tpl=tuple((1,2,3,))
print(tpl.index(1))

#set methods

#add
#syntax:variable.add()

a={'a','v','s'}
a.add('y')
print(a)

#update
#syntax:variable.update(setvariable)

a={'a','b','c'}
b={'b','c','d'}
a.update(b)
print(a)

#remove
#syntax:variableName.remove(item)

a={'a','b','c'}
a.remove('b')
print(a)

#discard
#syntax:variableName.discard(item)

a={'a','b','c'}
a.discard('c')
print(a)

#pop
#syntax:variableName.pop()

a={'a','b','c'}
a.pop()
print(a)


#frozenset methods

#union
#syntax:variableName.union(variable)

a={'a','b','c'}
b={'b','c','d'}
print(a.union(b))

#intersection
#syntax:variableName.intersection(variable)

a={'a','b','c'}
b={'b','c','d'}
print(a.intersection(b))

#intersection update
#yntax:set1.intersection_update

a={'a','b','c'}
b={'b','c','d'}
print(a.intersection_update(b))
print(a)
print(b)

#isdisjoint
#syntax:set1.isdisjoint(set2)

a={'a'}
b={'b'}
print(a.isdisjoint(b))

#difference
#syntax:set1.difference(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.difference(b))

#symmetric difference
#syntax:set1.symmetric difference(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.symmetric_difference(b))

#symmetric difference update
#syntax:set1.symmetric difference update(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.symmetric_difference_update(b))
print(a)
print(b)

#issubset
#syntax:set1.issubset(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.issubset(b))

#issuperset
#syntax:set1.issuperset(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.issuperset(b))
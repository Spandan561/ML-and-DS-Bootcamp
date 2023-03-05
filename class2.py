a = 5
b = 10.6
print(a,b)

print(b/a) #float return
print(b//a) #integer return
print(b%a)#modulus
print(b**2) #exponent

##comparison Operator
print(a==b)
print(a!=b)
print(a<b)
print(a>b)

#Logical Operator
x=4
y=4
z=6
print(x==y and y==z)
print(x==y or y==z)
print(not x==y)

##membership operator

print("desh" in "Bangladesh")

#Identity operator
print(a is b)

                                      ##Data Structure
#List
lst_1 = ['BUET','RUET','EWU','BRAC']
lst_2 = [1,2,3,4]
print(lst_1[1],lst_1[2]) #indexing
print(lst_1[0:3]) #slicing
print(lst_1[1:3])
lst_1.append('NSU')
print(lst_1)
lst_1.insert(2,'KUET')
print(lst_1)
lst_1.extend([10,20])
print(lst_1)
lst_1.extend(lst_2)
print(lst_1)
lst_1+lst_2
print(lst_1+lst_2)
#Remove
del lst_1[7:]
print(lst_1)
del lst_1[-2]
print(lst_1)
lst_1.remove('BRAC')
print(lst_1)
lst_1 += ['RUET','RUET']
print(lst_1)
print(lst_1.count('RUET'))
lst_3 = ['b','c','e','a']
print(sorted(lst_3))

##Tuple
tup = ('a','b','c','d')
#Dictionary
dict = {'b':'BUET','r':'RUET','e':'EWU','n':'NSU'}
print(dict['e'])

#String
string = 'Bangladesh is love'
print(string)
n = 147570
string_2 = "Area of BD is: "
print(string_2,n,"sq.km.")
print(f"{string_2}{n} sq.km.")


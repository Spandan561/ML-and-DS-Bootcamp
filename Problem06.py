def is_P(a):
    flag=0
    for i in a:
        if i=='P':
            flag=1
    if flag==1:
        return True
def is_not_p(a):
    flag = 0
    #print(a)
    for i in a:
        if i == 'P':
            flag = 1
    if flag == 0:
        a+='P'
    return a
        #return True

lst = ["ux1P5", "rt0", "ft3", "z1aP"]
## Filter
print("Output after Filterring--> ")
f = filter(is_P,lst)
print(list(f))
##Map
print("Output after Mapping--> ")
m = map(is_not_p,lst)
print(list(m))

##Reduce function
import functools
num = [1,2,3,4,5,6]
print("The Summation of list is--> ")
sum = functools.reduce(lambda a,b:a+b,num)
print(sum)


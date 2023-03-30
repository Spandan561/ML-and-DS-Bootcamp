class calculators:
    def __init__(self,a,b):#class constructor
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def seb(self):
        return self.a-self.b

calc = calculators(11,20)
s = calc.add()
print(s)
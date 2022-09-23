class OurClass:
    def __init__(self, ankit):
        self.bruno = ankit
    
    def square(self):
        self.bruno = self.bruno ** 2

    def div2(self):
        self.bruno = self.bruno // 2

o = OurClass(4)

o.square()
o.div2()
print(o.bruno)

o.square()
o.div2()
print(o.bruno)
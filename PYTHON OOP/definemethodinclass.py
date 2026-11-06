class wolf:

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def auu(self):
        print("auuuuuuu ,auuuuu , wrawww!")

    def wolfinfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

ozzy = wolf("Ozzy", 2)
skippy = wolf("Skippy", 12)
filou = wolf("Filou", 8)

ozzy.wolfinfo()
skippy.wolfinfo()
filou.wolfinfo()
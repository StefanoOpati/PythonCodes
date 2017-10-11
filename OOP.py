#modelling a typical human being
"""class HumanBeing():
    pass

opati=HumanBeing()
opati.height=5.2
opati.colour= "black"
jane.height=5.2
jane.colour= "black"

print(opati.height)
print(opati.colour)
print(jane.height)
print(jane.colour

print(opati)
print(jane)"""


class Humanbeing():
      #class constructor.Human beings has
      def __init__(self,name="Person",gender="human",age=20,colour="black",height=5.6,MPESAPIN=1234,MPESABal=22000):
        """class attributes"""
        self.name=name
        self.gender=gender
        self.age=age
        self.colour=colour
        self.height=height
        self.__pin=MPESAPIN
        self.__bal=MPESABal

    #Class methods
      def speak(self):
          return "I'm {}. Aged{}. Skin colour {}. {}".format(self.name,self.age,self.colour,self.gender)
      def grow(self):
          self.age+=1
#getter and setters
      def getBalance(self):
          enteredPin=int(input("Enter pin:"))
          if enteredPin==self.__pin:
              print("Balance is: ",self.__bal)
          else:
              print("Get out of here.")


class man(Humanbeing):
    def __init__(self,name="Person",age=20,colour="black",height=5.6,MPESAPIN=1234,MPESABal=22000,beared=True):
       super().__init__(name=name,gender="Male",age=age,height=height,MPESAPIN=MPESAPIN,MPESABal=MPESABal)
       self.beared=beared

    def maturity(self):
        if beared:
            print("Matured male")
        else:
            print("Not male")


Janet=Humanbeing()

Janet.name="Janet W"
Janet.gender="female"
Janet.colour="light"
print(Janet.name)
print(Janet.speak())
Janet.grow()
print(Janet.speak())

print(Janet.speak())
Janet.getBalance()
print(Janet.speak())
#print(Janet__pin)
#This is encapsulated
Nderitu= man("Nderitu",20,"black",5.2)
print(Nderitu.speak())
      

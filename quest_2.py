 #Explain overloading and overriding by writing a sample program?

# overriding

class Vehicle():
    def __init__(self):
        self.model="Model"

    def show(self):
        print(self.model)

class Car(Vehicle):
    def __init__(self):
        self.model="new Model"

    def show(self):
        print(self.model)

veh_1 = Vehicle()
car_1 = Car()

veh_1.show()
car_1.show()

# overloading
# print(1+3) # 4
# print("2"+"5") # 25

class ClassName():
    def funcNname(self,name = None):
        if name is not None:
            print("Hai"+name)
        else:
            print("Hai")

obj = ClassName()
obj.funcNname()
obj.funcNname(" Ganesh") 


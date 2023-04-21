# OOP project 
# classes
class RentCar:
    def __init__(self,stockk):
        self.stock = stockk
    def rent_a_car(self,quan):
        if self.stock==0:
            print("\t\t\t No more stock is available now")
        elif quan>self.stock:
            print("\t\t\t Limited stock available is : ",self.stock)
        else:
            self.stock = self.stock - quan
            self.price = 95*quan
            print("\t\t\tTotal Price --> ",self.price)
            print("\t\t\tTotal Stock available now --> ",self.stock)
    def show_car(self):
        print("\n\t\t Total stock --> ",self.stock)
# object
obj = RentCar(200)
while 1:
    uc = int(input("""\n\n\t<---- Welcome to the shop ---->
    1. Rent a car
    2. Display stock of car
    3. Exit\n"""))
    
    if uc==1:
        q = int(input("\n\t\t Enter the quantity -->  "))
        obj.rent_a_car(q)
    elif uc==2:
        obj.show_car()
    elif uc == 3:
        break
    else:
        print("\n\t\t<-- Invalid Choice -->")
# end of code        
#define class
class shoe:
    # contstructor function - initial instance method always needs __init__ and self
    def __init__(self, brand, shoe_type, price):
        #instance variables
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True

    #instance method, always needs self
    def discount_percent(self, percent_off):
        self.price = self.price * (1-percent_off/100)

#object of class/ object instance
skater_shoe = shoe("Vans", "low-top", 59.99) #first argument is 'skater_shoe' which gets passed to self
dress_shoe = shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)

#call instance method
dress_shoe.discount_percent(50)

print(dress_shoe.price)
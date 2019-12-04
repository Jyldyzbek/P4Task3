class Car:
    def __init__(self, make, model, year, km):
        self.make = make
        self.model = model
        self.year = year
        self.km = km
        self.odometr = 0
        self.fuel = 70
        
    def Drive(self):
        self.distans_fuel()
        if (self.km/10) <= self.fuel:
            self.__add_distans()

    def __add_distans(self):
        self.odometr += self.km

    def distans_fuel(self):
        if (self.km/10) <= self.fuel:
            self.fuel -= (self.fuel/10)
            print('Nu che, trogay')
        else:
            print('Benzin jok')

Mers = Car('Mers', 'E-class', 2015, 600)
Mers.Drive()
print(Mers.odometr, Mers.fuel)

class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    
    def increase_mileage(self, miles):
        if miles > 0:
            self.mileage += miles
            print(f"Total miles are {self.mileage} miles after increasing {miles} miles")
    
    def print_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Miles: {self.mileage}")

Car1 = Car("Car1", "Delta", "2023", 1000)

Car1.print_info()

Car1.increase_mileage(200)

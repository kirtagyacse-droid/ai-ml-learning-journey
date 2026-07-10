class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def honk(self):
        return f"beep beep"
    
    @property
    def make(self):
        return self._make
    @make.setter
    def make(self, make):
        self._make = make
        
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, model):
        self._model = model
    
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, year):
        if year < 1886:
            raise ValueError("not a valid car")
        self._year = year
    
    @classmethod
    def get(cls):
        make = input("Make: ")
        model = input("Model: ")
        year = input("Year: ")
        return cls(make,model, year)
def main():
    car = Car("Toyota", "Corolla", 2020)
    print(car)
    print(car.honk())

    
if __name__ == "__main__":
    main()
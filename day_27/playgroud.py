# creating a function with *args
def add_func(*arg):
    sum= 0
    for i in arg:
        sum+= i

    return sum

addition = add_func(1, 5, 12, 15)
print(addition)


# creating a class using **kwargs
class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]


car_1 = Car(make="Toyota", model="Corolla")
print(car_1.make)

# problem that exist with the above is all args must be specified at
#  instantiation. Option is to use .get method of a dictionary

class Car2:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


car_2= Car2()
print(car_2.make)
class Car:        #creating class
    attr1 = "Audi"
    attr2 = "Benz"

    def names(self):  #creating function
        print("The carname is:",self.attr1)
        print("The carname is:",self.attr2)

MyCar = Car()  #creating object -MyCar is object and car is class
print(MyCar.attr1)
MyCar.names()

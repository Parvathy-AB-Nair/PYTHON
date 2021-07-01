#Animal pgm
class Animal:
    def __init__(self,Eng_name,Lat_name,color,age):
        self.Eng_name=Eng_name
        self.Lat_name = Lat_name
        self.color = color
        self.age = age
    def display(self):
        print("English Name of animal:",self.Eng_name)
        print("Latin Name of animal:", self.Lat_name)
        print("color:", self.color)
        print("age:", self.age)
goat=Animal('Goat','Capra aegagrus hircus','Brown',4)
goat.display()
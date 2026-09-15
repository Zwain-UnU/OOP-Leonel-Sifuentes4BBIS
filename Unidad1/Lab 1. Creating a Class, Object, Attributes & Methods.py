class monitor:
  def __init__(self, brand, screenSize, resolution):
    self.brand = brand
    self.screenSize = screenSize
    self.resolution = resolution

  def turnOn(self):
    print("The monitor is turn On in this moment :D")

  def turnOff(self):
    print("The monitor is turn Off in this moment D:")

  def describe(self):
    print(f"\nThis monitor is brand {self.brand},\nThe screenSize is {self.screenSize}, \nand the Resolution is {self.resolution}")


#Self: Se utiliza para decirle a python a que objeto pertenecen los atributos
#Create an instance using the class monitor C:

monitor1 = monitor("HP", "15 inch", "1920 x 1080p")
monitor2 = monitor("Acer", "24 inch", "1920 x 1080p")

#We acces to the object(Intance) "monitor1" to call its data
print(monitor1.brand)
print(monitor2.screenSize)
monitor1.turnOn()
monitor2.describe()

#Instance "monitor2"
print(monitor2.brand)


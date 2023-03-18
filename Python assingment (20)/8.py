class Laptop:
    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def showConfig(self):
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram}GB")
        print(f"CPU: {self.cpu}")
        print(f"HDD: {self.hdd}GB")

laptop1 = Laptop("Dell", 16, "Intel Core i7", 512)
laptop2 = Laptop("Lenovo", 8, "Intel Core i5", 256)
laptop3 = Laptop("HP", 12, "Intel Core i7", 1)

laptops = [laptop1, laptop2, laptop3]

sorted_laptops = sorted(laptops, key=lambda laptop: laptop.ram)

for laptop in sorted_laptops:
    laptop.showConfig()
    print("-----------")

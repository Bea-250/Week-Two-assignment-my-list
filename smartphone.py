# Step 1: Define the base class first
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self._battery = 100  # encapsulated attribute

    def charge(self, amount):
        self._battery = min(100, self._battery + amount)
        print(f"{self.model} charged to {self._battery}%.")

    def use(self, hours):
        drain = hours * 10
        self._battery = max(0, self._battery - drain)
        print(f"{self.model} used for {hours}h. Battery: {self._battery}%.")

    def info(self):
        return f"{self.brand} {self.model} ({self.storage}GB)"


# Step 2: Now define the inherited class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    # Override use() for gaming mode
    def use(self, hours):
        drain = hours * 20
        self._battery = max(0, self._battery - drain)
        print(f"{self.model} (Gaming Mode) used for {hours}h. Battery: {self._battery}%.")


# Step 3: Test it
phone1 = Smartphone("Samsung", "Galaxy S24", 256)
phone1.use(3)
phone1.charge(20)

rog = GamingPhone("Asus", "ROG Phone 8", 512, "Liquid Cooling")
rog.use(2)

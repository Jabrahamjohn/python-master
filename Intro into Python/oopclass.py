# Class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, price, battery_life):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_life = battery_life

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def get_info(self):
        return f"Smartphone: {self.brand} {self.model}, Price: ${self.price}, Battery Life: {self.battery_life} hours"

# Class representing a GamingSmartphone (inherits from Smartphone)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, battery_life, gpu, cooling_system):
        super().__init__(brand, model, price, battery_life)
        self.gpu = gpu
        self.cooling_system = cooling_system

    def play_game(self, game_name):
        return f"Playing {game_name} on {self.brand} {self.model} with {self.gpu} GPU and {self.cooling_system} cooling system."

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, GPU: {self.gpu}, Cooling System: {self.cooling_system}"

# Example usage
if __name__ == "__main__":
    phone = Smartphone("Samsung", "Galaxy S21", 799, 24)
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 999, 18, "Adreno 660", "Advanced Vapor Chamber")

    print(phone.get_info())
    print(phone.make_call("123-456-7890"))
    print(phone.send_message("123-456-7890", "Hello!"))

    print(gaming_phone.get_info())
    print(gaming_phone.play_game("PUBG Mobile"))
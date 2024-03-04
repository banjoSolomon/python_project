class Gun:
    def __init__(self, caliber, capacity):
        self.caliber = caliber
        self.capacity = capacity
        self.bullets_loaded = 0

    def load_bullets(self, num_bullets):
        if self.bullets_loaded + num_bullets <= self.capacity:
            self.bullets_loaded += num_bullets
            print(f"Loaded {num_bullets} bullets. Total bullets loaded: {self.bullets_loaded}")
        else:
            print(f"Cannot load {num_bullets} bullets. Capacity exceeded.")

    def shoot(self):
        if self.bullets_loaded > 0:
            self.bullets_loaded -= 1
            print("Boom!!! One bullet fired.")
        else:
            print("Click!! No bullet left bro. Reload MTF!!")

    def display_info(self):
        print(f"Caliber: {self.caliber}")
        print(f"Capacity: {self.capacity}")
        print(f"Bullets Loaded: {self.bullets_loaded}")


my_gun = Gun(caliber="9mm", capacity=17)
my_gun.display_info()
my_gun.load_bullets(10)
my_gun.display_info()

for _ in range(12):
    my_gun.shoot()

my_gun.display_info()
my_gun.load_bullets(8)
my_gun.display_info()


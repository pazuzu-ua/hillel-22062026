
# # empty class
# class MyClass: ...

# # конструктор класу -> створює об'єкти
# my_class_object = MyClass()

# my_class_object.name = "Test"

# print(my_class_object.name)

# ---------------------------------------
# nickname, breed, fur_colour
# class Dog:
#     # magic (dunder = double underscore) methods
#     def __init__(self, nickname, breed, fur_colour) -> None:
#         self.nickname   = nickname
#         self.breed      = breed
#         self.fur_colour = fur_colour

#     def get_dog_info(self) -> str:
#         return f"Dog '{self.nickname}' ({self.breed}; {self.fur_colour}) "

# my_dog = Dog("Test", "syberian husky", "white")
# # Dog.__init__( my_dog, "Test", "syberian husky", "white" )

# print( my_dog.get_dog_info() )

# -----------------------------------------------
# class Animal:
#     def __init__(self, nickname, breed) -> None:
#         self.nickname   = nickname
#         self.breed      = breed

# class Dog(Animal):
#     # magic (dunder = double underscore) methods
#     def __init__(self, nickname, breed, fur_colour) -> None:
#         self.fur_colour = fur_colour
#         super().__init__(nickname, breed)

#     def get_dog_info(self) -> str:
#         return f"Dog '{self.nickname}' ({self.breed}; {self.fur_colour}) "

# class Cat(Animal):
#     # magic (dunder = double underscore) methods
#     def __init__(self, nickname, breed, fur_colour) -> None:
#         self.fur_colour = fur_colour
#         super().__init__(nickname, breed)

#     def get_dog_info(self) -> str:
#         return f"Cat '{self.nickname}' ({self.breed}; {self.fur_colour}) "

# class Fish(Animal):

#     def get_dog_info(self) -> str:
#         return f"Fish '{self.nickname}' ({self.breed}) "

# my_fish = Fish("test", "test")
# my_cat = Cat("test", "test", "test")





# ---------
# class Weapon:
#     def __init__(self, name, damage) -> None:
#         self.name = name
#         self.damage = damage

# class Warrior:
#     def __init__(self, name, level=1) -> None:
#         self.name = name
#         self.level = level
#         self.weapon = None

#     def wield( self, weapon: Weapon ):
#         self.weapon = weapon

#     def attack(self):
#         if not self.weapon:
#             print("Cannot attack")
#         else:
#             power = self.level * self.weapon.damage
#             print(f"{self.name} attacks with '{self.weapon.name}' and deals {power} damage...")


# soldier = Warrior("Gilgamesh", 20)
# soldier.attack()

# knife = Weapon("knife", 0.25)
# soldier.wield( knife )
# soldier.attack()


# -----
# class BankAccount:
#     def __init__(self) -> None:
#         self.__money = 0

#     def deposit(self, money):
#         if money > 0:
#             self.__money += money
#             print(f"ADDED {money}")
#         else:
#             print("CANNOT ADD")

#     def withdraw(self, money):
#         if ( self.__money - money ) >= 0:
#             self.__money -= money
#             print(f"WITHDRAWN {money}")
#         else:
#             print("CANNOT WITHDRAW")

#     def get_balance(self):
#         return self.__money


# wallet = BankAccount()
# wallet.deposit(-500)
# wallet.deposit(500)
# wallet.withdraw(1000)
# wallet.withdraw(100)
# print( wallet.get_balance() )

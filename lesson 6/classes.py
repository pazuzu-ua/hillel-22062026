# class MyClass:
#     ...

# class MyClassv2:
#     # obj = MyClassv2( ... )
#     def __init__(self, name, *args, **kwargs) -> None:
#         if not name:
#             raise ValueError("name should be provided")
#         self.name = name
#         self.random_test = "..."



# class Dog:
#     dog_count = 0

#     # default method -> приймає self (об'єкт)
#     def __init__(self, name, age, breed) -> None:
#         Dog.dog_count += 1
#         self.name = name
#         self.age = age
#         self.breed = breed

#     # class method -> приймає cls (сам клас)
#     # classmethod(from_dict)
#     @classmethod
#     def from_dict(cls, data):
#         if not isinstance(data, dict):
#             raise ValueError("data should be dict")
#         # .... validate
#         return cls( data["name"], data["age"], data["breed"] )  # Dog( ... )

#     @classmethod
#     def default_dog(cls):
#         return cls( "Bobik", 1, "sosis" )

#     @staticmethod
#     def age_to_human(age):
#         return age * 7

#     @staticmethod
#     def validate_dog_breed(breed):
#         return breed in ( "sosis", "husky" )

# # DateTime -> now(), from_timestamp(2445495945), from_str("2020-08-08 11:11:11")

# # obj = Dog()
# # obj.__init__()    ---->    __init__(obj)
# # obj.from_dict()   ---->    from_dict(Dog)
# dog = Dog("test", 11, "")
# print( dog.dog_count )

# dog2 = Dog("test", 11, "")
# print( dog2.dog_count )

# dog3 = Dog.default_dog()
# print( dog2.dog_count )

# dog_breed = "sosis"
# if Dog.validate_dog_breed( dog_breed ):
#     dog4 = Dog("test", 11, dog_breed)
# else:
#     print("oops")

# # from utils import a, b, c
# # Utils.a(), ...



# -------------------------------------
class SecretClass:
    def __init__(self, secret) -> None:
        ...
        # self.secret = secret        # public
        # self._secret = secret         # private
        # self.__secret = secret          # protected

# s = SecretClass("secret")
# print( s.secret )
# s.secret = "secret2"
# print( s.secret )

# s = SecretClass("secret")
# print( s._secret )
# s._secret = "secret2"
# print( s._secret )

# s = SecretClass("secret")
# print(  dir( s )  )
# print( s._SecretClass__secret )
# s.__secret = "secret2"
# print( s.__secret )



# class Wallet:
#     def __init__(self, money) -> None:
#         self.__money = money

#     # getter
#     def get_money(self):
#         return self.__money

#     # setter
#     def set_money(self, amount):
#         self.__money = amount

# w = Wallet(0)
# w.set_money(100)

# print( w.get_money() )


# class Wallet:
#     def __init__(self, money) -> None:
#         self.__money = money

#     @property
#     def money(self):
#         # ..... validation
#         return self.__money

#     @money.setter
#     def money(self, value):
#         # ..... validation
#         self.__money = value

#     @money.deleter
#     def money(self, value):
#         # ..... validation
#         # .... clean up
#         self.__money = 0

# w = Wallet(100)
# w.money = 10
# print( w.money )
# del w.money




# ----
# class Rectangle:
#     def __init__(self, width: int, height: int) -> None:
#         self.width = width
#         self.height = height

#     def __str__(self) -> str:
#         return f"Rectanle ( {self.width}, {self.height} )"

#     def __repr__(self) -> str:
#         return self.__str__()

#     @property
#     def area(self) -> int:
#         return self.height * self.width

# r = Rectangle( 10, 20 )
# # print( r.area )

# print( r )
# print( [r] )


# -------
class Wallet:
    def __init__(self, money) -> None:
        Wallet.validate_amount(money)
        self.__money = money

    @staticmethod
    def validate_amount(value):
        if not isinstance(value, int):
            raise ValueError("Must be an integer")
        if value < 0:
            raise ValueError("Must be positive")

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        Wallet.validate_amount(value)
        self.__money = value

    def __str__(self) -> str:
        return f"Wallet ({self.__money})"

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self, other):
        other_amount = other.money if isinstance( other, Wallet ) else other
        return Wallet( self.money + other_amount )

    def __eq__(self, value: object) -> bool:
        other_amount = value.money if isinstance( value, Wallet ) else value
        return self.__money == other_amount


w1 = Wallet(10)
w2 = Wallet(15)
w1_copy = Wallet(10)
w3 = w1 + w2
# w1.__add__(w2)
print( w1 == w1 )
print( w1 == w1_copy )
print( w1 == w2 )

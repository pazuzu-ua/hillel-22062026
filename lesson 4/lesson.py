# uv add --dev pyright


# def add_numbers( first_number: int, second_number: int ) -> int:
#     return first_number + second_number

# result = add_numbers( 11, "10" )


# def get_user_info(): return {}
# user = get_user_info()


# def check_user( user_info: dict ):
#     user_info
#     ...


# def template(
#         number: int,
#         number_b: float,

#         string: str,

#         list_value: list,
#         list_value_b: list[int],

#         tuple_type: tuple[int, int, int],        #   (  1, 2, 3  )

#         dict_type: dict,
#         dict_type_b: dict[str, int],

#         bool_type: bool,
#         none_type: None,


#         # -- |
#         user_id: int | str,
# ):
#     ...



# PI: float = 3.14



# def analyze_user( user_info: dict | None ):
#     # dict.get() --> yes
#     # None.get() --> =(

#     if user_info is None:
#         return ""

#     return user_info.get("name")






# Номінальна типізація ---- структурна
# за успадкуванням           ---  за формою

# from typing import Protocol

# # trait = риса
# class Readable(Protocol):
#     def read(self) -> str: ...

# class Magazine:
#     def read(self) -> str: ...

# class Book:
#     def read(self) -> str: ...

# class Booklet:
#     def read(self) -> str: ...

# class Bulletin:
#     def read(self) -> str: ...


# def study( info_source: Readable ):
#     info = info_source.read()
#     return info

# study( Book() )







# ------

# class Animal: ...

# class Cat(Animal): ...
# class Dog(Animal):
#     def bark(self):
#         ...

# def add_a_cat( animals: list[Animal] ) -> None:
#     animals.append( Cat() )

# cats: list[Cat] = [ Cat() ]
# add_a_cat( cats )

# dogs: list[Dog] = [ Dog() ]
# add_a_cat( dogs )




# from typing import Any

# def do_smth() -> Any: ...

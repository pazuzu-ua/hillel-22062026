# 1 ---- DRY
# class Test:
#     def __init__(self, value) -> None:
#         self.value = value

#     # property
#     def value(self, value):
#         # validation
#         ...

# 2 ----- list vs tuple
# L = [ 1, 2, 3 ]
# T = ( 1, 2, 3 )

# obj = Text(X)
# obj.value = X


# ----
# L = []
# for i in range(2, 11):
#     L.append(i)

# -----
# L = [ i for i in range(2, 11) ]


# ----------------------------
# OOP - PYTHONIC
# container = smth. that contains smth. = API
# import random

# class Card:
#     def __init__(self, rank: str, suit: str) -> None:
#         self.rank = rank
#         self.suit = suit

#     def __str__(self) -> str:
#         return f"{self.rank} of {self.suit}"

#     def __repr__(self) -> str:
#         return self.__str__()

#     def __eq__(self, other_card: object) -> bool:
#         return ( self.rank == other_card.rank ) and ( self.suit == other_card.suit )


# class OrdinaryDeck:
#     RANKS = [ str(i) for i in range(2, 11) ] + list("JQKA")
#     SUITS = ( "spades", "diamonds", "clubs", "hearts" )

#     def __init__(self) -> None:
#         self.__cards = [ Card(rank, suit) for suit in self.SUITS for rank in self.RANKS ]

#     def get_length(self) -> int:
#         return len(self.__cards)

#     def get_by_id(self, index: int) -> Card:
#         return self.__cards[index]

#     def get_random_card(self):
#         return random.choice(self.__cards)

#     def get_sorted(self, key_func):
#         return sorted(self.__cards, key=key_func)

#     def get_reversed(self):
#         # iterator, generator
#         return list( reversed( self.__cards ) )

#     def contains_card( self, card: Card ) -> bool:
#         for inner_card in self.__cards:
#             if card == inner_card:
#                 return True
#         return False

# od = OrdinaryDeck()
# print( od.get_length() )
# print( od.get_by_id(33) )
# print( od.get_random_card() )
# print( od.contains_card( Card("9", "hearts") ) )
# print( od.contains_card( Card("9", "meow") ) )



# class PythonicDeck:
#     RANKS = [ str(i) for i in range(2, 11) ] + list("JQKA")
#     SUITS = ( "spades", "diamonds", "clubs", "hearts" )

#     def __init__(self) -> None:
#         self.__cards = [ Card(rank, suit) for suit in self.SUITS for rank in self.RANKS ]

#     def __len__(self):
#         return len( self.__cards )

#     def __getitem__(self, key):
#         return self.__cards[key]

#     def __setitem__(self, key, value):
#         # validation
#         self.__cards[key] = value

#     def __repr__(self) -> str:
#         return f"PythonicDeck({self.__len__()} cards)"

# pd = PythonicDeck()
# # print( len(pd) )
# # print( pd[-1] )

# # for card in pd:
# #     print(card)

# # print( random.choice(pd) )

# # print( Card("Q", "hearts") in pd )

# pd[2] = Card("A", "hearts")


# Python Data Model - це спільна мова протоколів, яку розуміє екосистема





# ----------------------------------------------------------------------------
# print(10)
# print( print )

# print = 10
# print() # error

# from typing import Any

# class A:
#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         return 10

# a = A()
# result = a()
# print(result)


# my_print = print
# my_print("Hello!")

# def return_print():
#     return print

# my_print = return_print()
# my_print()

# return_print()()            # return_print.__call__().__call__()


# --- замикання - closure
# def print_value( value ):
#     def printer():
#         print( value )
#     return printer

# greet = print_value("Hello")
# greet()
# greet()

# bye = print_value("Bye")
# bye()
# bye()


# ДЕКОРАТОР
# a(1, 1, 1); b(x=10, y=20)
# def test_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("BEFORE", args)
#         result = func( *args, **kwargs )
#         print("AFTER")
#         return result
#     return wrapper

# # say_hello = test_decorator(say_hello)
# @test_decorator
# def say_hello(name):
#     print(f"Hello, {name}")

# say_hello("Bob")

# import time

# def debug_function(func):
#     def wrapper(*args, **kwargs):
#         print("#----- Function called with: ", args, kwargs)
#         start = time.perf_counter()
#         result = func( *args, **kwargs )
#         elapsed = time.perf_counter() - start
#         print(f"#----- {func.__name__} took {elapsed:.6f} seconds")
#         return result
#     return wrapper

# @debug_function
# def hello():
#     print("Hello")

# hello()



# def check_user_permissions(func):
#     def wrapper( *args, **kwargs ):
#         # CHECK... ----
#         return func()
#     return wrapper

# # f = dec_a( dec_b( dec_c( f ) ) )
# # @check...
# # @check_requirements
# @check_user_permissions
# def get_book_list():
#     ...


from functools import lru_cache
# f( X ) -> X`


@lru_cache(maxsize=50)
def memorize(func):
    cache = {}

    # cache = {
    #     ( 1, 2, "hello" ): "result"
    # }

    def wrapper( *args ):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

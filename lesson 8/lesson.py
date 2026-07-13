# -----

# def alotofargs( num, *args, **kwargs ):
#     print(num)
#     print(args)
#     print(kwargs)

# alotofargs(1, 2, 3, 4, a=4, b=5)

# -----

# def decorator( func ):
#     def wrapper( *args ):
#         return func( *args )
#     return wrapper


# @decorator
# def do(a, b, c):
#     ...

# do = decorator(do)

# def decorator( do ):
#     def wrapper( *args ):
#         return do( *args )
#    return wrapper

# do( 1, 2, 3 )
# wrapper( 1, 2, 3 ) --> [ *args ] --> do( *args ) --> do( 1, 2, 3 )




# -------
# @decorator( 7 )
# @decorator( key="" )

# def repeat(times):
#     def decorator( func ):
#         def wrapper( *args ):
#             for _ in range( times ):
#                 func( *args )
#             # ------
#         return wrapper
#     return decorator

# @repeat(3)
# def do():
#     print("HI")

# do()

# do = repeat(3)(do) # --> do = decorator(do)


# -------
# import time
# from functools import wraps


# def delay( seconds=0 ):
#     def decorator( func ):
#         @wraps(func)
#         def wrapper( *args ):
#             if seconds:
#                 time.sleep( seconds )
#             return func( *args )
#         return wrapper
#     return decorator


# @delay(5)
# def hello():
#     """Very important"""
#     print("HELLO")

# hello()

# print( hello.__name__ )
# print( hello.__doc__ )









# ---------------
# while True:
#     user_input = input( ">  " )
#     if user_input:
#         break


# user_input = input( ">  " )
# while not user_input:
#     print(user_input)
#     user_input = input( ">  " )

# while not ( user_input := input(">  ") ):
#     print( user_input )


# ----
# config = { "name": "John" }

# if config.get("name"):
#     name = config.get("name")
#     print( name )
#     print( name )
#     print( name )

# if ( name := config.get("name") ):
#     print(name)



# config = { "key": False }
# if ( value := config.get("key") ) is not None:
#     print("Customer set value as", value)


# name = "Johny"
# if ( name_length := len(name) ) > 4:
#     print("Exceeded length: ", name_length)


# import math

# numbers = ( 16, -4, 25, 3, 100, -9 )
# # result = [ math.sqrt(n) for n in numbers if ( n >= 0 ) and ( math.sqrt(n) < 8 ) ]

# result = [ n_sqrt for n in numbers if ( n >= 0 ) and ( ( n_sqrt := math.sqrt(n) ) < 8 ) ]

# print(result)





# --------------------- iterator / generator
# L = [1, 2, 3]
# # for i in L:
# #     print(i)

# # L -- list --- ITERABLE

# iterator = iter(L)# L.__iter__()
# while True:
#     try:
#         value = next(iterator)
#     except StopIteration:
#         break
#     print(value)

# iterator
# class CountToFive:
#     def __init__(self) -> None:
#         self.current = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current > 5:
#             raise StopIteration
#         value = self.current
#         self.current += 1
#         return value

# c = CountToFive()
# for number in c:
#     print(number)

# for number in c:
#     print(number)


# iterator for iterable
# class CountToFiveIterator:
#     def __init__(self) -> None:
#         self.current = 1

#     def __next__(self):
#         if self.current > 5:
#             raise StopIteration
#         value = self.current
#         self.current += 1
#         return value

# # iterable
# class CountToFive:
#     def __iter__(self):
#         return CountToFiveIterator()


# c = CountToFive()
# for number in c:
#     print(number)

# for number in c:
#     print(number)



# ------
# def counter():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# for i in counter():
#     print(i)



# fibonacci
# 0, 1, 1, 2, 3, 5 ....

# lazy evaluation
# def fibonacci( stopper=5 ):
#     count = 1
#     a, b = 0, 1
#     while True:
#         yield a

#         if count == stopper:
#             break

#         count += 1

#         a, b = b, a + b

# for fib in fibonacci():
#     print(fib)



# -----------
# import sys

# list_comp = [ x for x in range(1_000_000) ]
# gen_exp = ( x for x in range(1_000_000) )

# print( sys.getsizeof(list_comp) )
# print( sys.getsizeof(gen_exp) )
# -----------


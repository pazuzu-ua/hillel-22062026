import threading


def test( argument_a ):
    print(argument_a)


t = threading.Thread( target=test, args=( 10, ) )
t.start()
t.join()

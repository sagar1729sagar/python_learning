# def greet():
#     friend = yield
#     print(f'Hello {friend}')
#
# g = greet()
# g.send(None) #priming the generator
# g.send('Adam')


from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting}, {friend}')


def greet(g):
    yield from g
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)


f = friend_upper()
g = greet(f)

g.send(None)
g.send("A")
g.send("B")
print("Hello World! Multitasking.....")
g.send("C")

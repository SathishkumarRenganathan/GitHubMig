def mygenerataor():
    print("First name")
    yield 10

    print("second name")
    yield 20

    print("last name")
    yield 30


gen = mygenerataor()
next(gen)
next(gen)
next(gen)
next(gen)
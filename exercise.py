lam = lambda x=0: lambda y=0: lambda z=0: x + y + z

curry = lam(1)(2)
curry2 = lam(3)

print(lam(1)(2)(3))
print(lam()(2)(1))
print(lam(lam(lam(1)(3)(5))(2)(4))(6)(7))

print(curry(50))
print(curry())
print(curry2(10)(100))


def gen():
    yield 100
    yield 200
    yield 300
    yield 400


a = gen()
print(
    f"""
{next(a)}
{next(a)}
{next(a)}
{next(a)}
"""
)
b = gen()
print(
    f"""
b = {lam(next(b))
		(next(b))
		(next(b))}
"""
)

import sys

# excercise.py 200 400 600
args = sys.argv
try:
    args = list(map(int, args[1:]))
    print(f"{lam(args[0])(args[1])(args[2])}")
except:
    print(f"error : excercise.py 数値 数値 数値")

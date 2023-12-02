lam = lambda x=1: lambda y=2: lambda z=3: x + y + z

curry = lam(1)(2)
curry2 = lam(3)


print(lam(1)(2)(3))
print(curry(50))
print(curry2(10)(100))
print()

lam = lambda x: lambda y: lambda z: x + y + z

curry = lam(1)(2)
curry2 = lam(3)


print(lam(1)(2)(3))
print(curry(50))
print(curry2(10)(100))
print()

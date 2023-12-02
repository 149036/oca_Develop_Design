a = [1, 1, 2, 3, 3]
print(a)

b = {1, 1, 2, 3, 3}
print(b)

c = set(a)
print(c)

d = {i * 2 for i in range(5)}
print(d)

##################################################
import random
import time

e = [random.randint(0, 100000000) for i in range(1000000)]
f = set(e)
checked_list = [random.randint(0, 100000000) for i in range(100)]


def test(rand_list):
    start = time.time()

    for temp in checked_list:
        if temp in rand_list:
            print(f"temp:{temp} in a")

    end = time.time()

    print(
        f""" 
        length : {len(rand_list)}  
        time   : {(end - start) * 1000}
		"""
    )


test(e)
test(f)

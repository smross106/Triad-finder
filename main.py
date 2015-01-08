import random, time
FOUND = 0

a1 = range(0,472,4)
a2 = range(0,472,4)
a3 = range(0,472,4)
random.shuffle(a1)
random.shuffle(a2)
random.shuffle(a3)

def find_1(x):
    found = 0
    a = 0
    while a < len(a1):
        b = 0
        for j in a2:
            c = 0
            for k in a3:
                if a1[a]+a3[c]/2 == a2[b]:
                    print "I found one!"
                    a1.pop(a)
                    a2.pop(b)
                    a3.pop(c)
                    found += 1
                    now = time.time()
                    print(start - now)
                    a += 1
                else:
                    print( found, a1[a], a2[b], a3[c])
                    c += 1
            b += 1
        a += 1


start = time.time()
find_1(0)

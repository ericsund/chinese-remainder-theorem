a = [1, 2, 3]
m = [2, 3, 5]

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def validate(m):
    # check if m_i are all coprime
    if len(m) >= 2:
        i = 0
        j = 1
        while i < len(m):
            while j < len(m):
                if gcd(m[i], m[j]) != 1:
                    print("CRT cannot be applied: not all m_i are coprime.  Check " + str(m[i]) + " and " + str(m[j]) + "!")
                    return 1
                j += 1
            i += 1

    elif len(m) == 1:
        print("Let's have at least two comgruence equations")
        return 1

    if len(a) != len(m):
        print("Make sure you have as many a_i as m_i")
        return 1

def crt(a, m):
    # compute big M
    M = 1
    for i in m:
        M *= i
    
    #compute big M_i
    M_i = []
    for i in m:
        M_i.append( M/i )

    # solve each congruence equation

    # for this new a list, make it the least positive residue
    # at the same time, compute a particular solution with n = 1 for simplicity

    # note: when we rewrite the equations, initially our new a list contains all 1s, so we don't really
    # need to initialize a new list since we'll just be multiplying each item in the m list by 1

    print("CRT gives new system of congruence equations:")

    particular_sols = []
    for i in range(len(a)):
        # new least positive redidue
        reduced_a = ( M_i[i] % m[i] )
        print("y_" + str(i) + " <congruent> " + str(reduced_a) + " (mod " + str(m[i]) + ")" )
        # compute new particular solution
        particular_sols.append(m[i] + reduced_a)

    x = 0
    print("------------")
    for i in range(len(particular_sols)):
        print("x += " + str(a[i]) + " * " + str(M_i[i]) + " * " + str(particular_sols[i]))
        x += a[i] * M_i[i] * particular_sols[i]
    
    print("Unique solution modulo M = : " + str(M) + " ===> " + str(x % M))

# MAIN
crt(a, m)
import sys

a = [0, 0, 1, 6]
m = [2, 3, 5, 7]

# displays the equation to solve
def print_original(a, m):
    print("System of congruences:")
    for i in range(len(a)):
        print("x <congruent> " + str(a[i]) + " (mod) " + str(m[i]))
    print("-----------------------")

# displays the revised equation to solve
def print_revised(M_i, m):
    print("Revised system:")
    for i in range(len(a)):
        print(str(int(M_i[i])) + "y_" + str(i+1) + " <congruent> 1 (mod) " + str(m[i]))
    print("-----------------------")

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def validate(a, m):
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
    
    return 0

def crt(a, m):
    # compute big M
    M = 1
    for i in m:
        M *= i
    print("Big M: " + str(M))
    
    #compute big M_i
    M_i = []
    for i in m:
        M_i.append( M/i )
    for i in range(len(M_i)):
        print("M_" + str(i) + " = " + str(M_i[i]))
    print("\n")

    print_revised(M_i, m)

    # solve each new congruence equation

    particular_sols = []
    for i in range(len(m)):
        # reduce the current congruence to something smaller
        reduced_m = ( M_i[i] % m[i] )

        print("(" + str(i+1) + ") reduced to:\t" + str(int(reduced_m)) + "y_" + str(i+1) + " <congruent> 1 (mod) " + str(m[i]))

        # find a solution to the reduced, simpler congruence
        y = 0
        while y < m[i]:
            if (reduced_m * y) % m[i] == 1:
                print("(" + str(i+1) + ") solution: \ty_" + str(i+1) + " = " + str(y))
                particular_sols.append(y)
            y += 1

    x = 0
    print("------------")
    for i in range(len(particular_sols)):
        print("x += " + str(a[i]) + " * " + str(M_i[i]) + " * " + str(particular_sols[i]))
        x += a[i] * M_i[i] * particular_sols[i]
        print("x = " + str(x))
    
    print("Unique solution x" + " (" + str(x) + ") modulo M (" + str(M) + ") ===> " + str(x % M))

# MAIN
if validate(a, m) == 1:
    sys.exit(1)

print_original(a, m)
crt(a, m)
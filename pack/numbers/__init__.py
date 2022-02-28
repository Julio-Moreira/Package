# ;)
# ! {<J>}
# ! author: Julio C. Moreira
# ! made between 02/27/2022 to 02/27/2022


# * FUNCTIONS {

def oper(num_1,num_2=2,op='m'):
    """function to do basic math operations

    num_1: the first number

    num_2: the second number

    op: parameter to control the operations m:multiplication d:division
    s:subtraction a:addition
    """
    if op == 'm':
        return num_1*num_2
    elif op == 'd':
        if num_1 > num_2:
            return num_1/num_2
        else:
            return num_2/num_1
    elif op == 's':
        if num_1 > num_2:
            return num_1-num_2
        else:
            return num_2-num_1
    elif op == 'a':
        return num_1+num_2

#even = par odd = impar
def isodd(num):
    """function to know if a number is odd

    num: the number
    
    return: True: is odd False: is not odd
    """
    if num % 2 != 0:
        return True
    else:
        return False

def root(rooting,index=2):
    """function to do root operations

    rooting: the number

    index: the index of root
    """
    return rooting**(1/index)

def isprime(num):
    """function to know if a number is prime

    num: the number
    
    return: True: is prime False: is not prime
    """
    ran = 1
    div = 0
    while ran <= num:
        if num % ran == 0:
            div += 1
        ran += 1
    if div == 2:
        return True
    else:
        return False

def div(num):
    """function to show the divisors of a number

    num: the number
    """
    divs = []
    for i in range(1,num+1):
        if num % i == 0:
            divs.append(i)
    return divs

# * }
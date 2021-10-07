

def is_palindrome(n):

    nr = n
    rez = 0
    while nr != 0:
        c = nr % 10
        rez = rez * 10 + c
        nr == nr // 10
    return n == rez
def test_is_palindrome():
    n=int(input("12321) n = ")
    if is_palindrome(n):
        print("Palindrome")
    else:
        print("Nu e palindrome")


 'Problema 6'

def is_superprim(n):
    while n!=0:
        if n<2:
            return False
        for i in range(2,n):
            if n%i == 0:
                return False
        n = n // 10
    return True
def test_is_superprime():
    n=int(input("3) n ="))
    if is_superprim(n):
        print("Superprim")
    else:
        print(" Nu e superprim")














def is_palindrome(n):
    nr = n
    rez = 0
    while nr != 0:
        c = nr % 10
        rez = rez * 10 + c
        nr == nr // 10
    return n == rez
def test_is_palindrome():
    n=int(input("12321) n = "))
    if is_palindrome(n):
        print("Palindrome")
    else:
        print("Nu e palindrome")


 #'Problema 6'

def is_superprim(n):
    while n != 0:
        if n < 2:
            return False
        for i in range(2 , n):
            if n % i == 0:
                return False
        n = n // 10
    return True


def test_is_superprime():
    n = int(input("3) n ="))
    if is_superprim(n):
        print("Superprim")
    else:
        print(" Nu e superprim")

def get_cmmmc(lst):
    nr = max(lst)
    while True == True:
        is_cmmmc= True
        for n in lst:
            if nr % n != 0:
                is_cmmmc = False
        if is_cmmmc == True:
            break
        nr = nr+1
    return nr

def test_is_palindrome():
    assert(is_palindrome(12321)==12321)
def test_is_superprim():
    assert(is_superprim(237)==237)
def test_get_cmmmc():
    assert(get_cmmmc([2,10,7])==70)



def main():
    print(is_palindrome())
    print(is_superprim())
    print(get_cmmmc([]))
    if __name__ == '__main__':
        main()












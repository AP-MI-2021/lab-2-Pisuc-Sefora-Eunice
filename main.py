def citire_date():
    n = int(input("Introduceti numarul de elemente din lista"))
    lst = []

    for i in range(n):
        lst.append(int(input("Dati numarul: ")))
    return lst


def is_palindrome(n):
    nr = n
    rez = 0
    while nr != 0:
        c = nr % 10
        rez = rez * 10 + c
        nr = nr // 10
    return n == rez
def test_is_palindrome():
    assert (is_palindrome(12321)==True)
    assert (is_palindrome(12522)==False)


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
    assert (is_superprim(23)==True)
    assert (is_superprim(36)==False)

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
def test_get_cmmmc():
    assert (get_cmmmc([1,3,7])==21)


def meniu():
    print("1.Citire date")
    print("2.Determina daca un nr dat este palindrome")
    print("3.Determina daca un nr este superprim")
    print("4.Sa se calculeze cmmmc al n numere")
    print("5.Iesire")

def run():
    lst = []
    while True == True:
        meniu()
        opt = input("Introdu optiunea:")
        if opt == "1":
            lst = citire_date()
        if opt == "2":
            n = int(input("Introduceti numarul"))
            if is_palindrome(n):
                print("Is palindrome")
            else:
                print("Is not palindrome")
        if opt == "3":
            n = int(input("Introduceti numarul"))
            if is_superprim(n):
                print("Is superprim")
            else:
                print("Is not superprim")
        if opt == "4":
            print("Multiplul este: ", get_cmmmc(lst))
        if opt == "5":
            break




def main():
    test_is_palindrome()
    test_is_superprime()
    test_get_cmmmc()
    run()

main()












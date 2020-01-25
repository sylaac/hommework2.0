name = input('what is your name? ')
print("hello", name)
choice = "yes"
while "yes" == choice:
    a = input('give me the real number you want to devise: ')
    b = input('give me the divisor')
    a = float(a)
    b = float(b)
    if b == 0:
        print("sorry you can't divide by 0")
    else :
        c = abs(a) % abs(b)
        if c < abs(b) / 2:
            d = int(abs(a) / abs(b))
        else :
            d = int(abs(a) / abs(b) + 1)
        if a < 0 or b < 0:
            if a > 0 or b > 0:
                d = -d
        print("the rounded division is", d)
    choice = input("tape yes if you want to do a new division")
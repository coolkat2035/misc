import os

def palindrome():
    '''Palindrome checker (alphabet only)'''

    s = input("What is your 'palindrome'? >> ")#raw thing
    S = list(filter(lambda c: c in 'abcdefghijklmnopqrstuvwxyz', s.lower())) #lower case, only leaves alphabet

    print(S == S[::-1])

def password():
    '''Checks if your password has enough length, any number, or any symbol.'''
    cin = input("Is your password safe?")
    cri = [False, False, False] #length, num, symbol

    if len(cin) >= 7:#7 chars or more
        cri[0] = True

    count = [0, 0]
    
    for c in cin:
        if c in '0123456789':#has 2+ numbers
            count[0] += 1

        elif c in '!@#$%&*':#has 2+ symbols (^+-/_ be like)
            count[1] += 1

    if count[0] >= 2:
        cri[1] = True

    if count[1] >= 2:
        cri[2] = True


    if all(cri):#all pass
        print("Strong")

    else:
        print("Weak")

def prime():
    """Lists out prime numbers. Might make you feel stronger."""
    prims = []
    count = None
    
    while True:
        try:
            count = int(input("How many prime numbers do you want?"))
            #THIS IS THE LARGEST NUMBER

        except ValueError:#bruh not a number
            print("I need a number.")
            continue


        if count in range(1000):
            start = True#lets go
            print('Here you go:')
            break
        
        else:#number too big or negative
            print("It is out of my control.")

    for num in range(2,count * 6): #number of primes
        for i in range(2, int(num**0.5)):#finding factors of current number
            if num % i == 0:#quits after finding any factor
                break

        else:#if didn't break(no factor found)
            prims.append(num)#you are qualified

    print(prims[:count])
    



allFunc = {
    1 : palindrome,
    2 : password,
    3 : prime
    }

#######################################################

if __name__ == "__main__":
    
    print("="*80)
    for f in allFunc.keys():
        print(f"({f}): {allFunc[f].__doc__}")#(index): DocString.
    print("="*80)

    while True:
        try:
            ans = int(input("Which one will you run? >>"))
            if ans in allFunc:
                break
            else:
                print("Not Found.")
        except:
            print("Not a number.")


    allFunc[ans]()#constant time babyy

    
os.system("pause")
    

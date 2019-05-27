def ispalindrome(num):
    numstr = str(num)
    for i in range(int(len(numstr) / 2)):
        if numstr[i] != numstr[-i - 1]:
            return False
    return True


def reverseNum(num):
    renum = 0
    if num == 0:
        return renum
    else:
        while num:
            renum = renum * 10 + num % 10
            num = num // 10
        return renum

def setA(amax,bmax):
    A = []
    B = []
    C = []
    a = 10
    while a < amax:
        b = a
        if ispalindrome(b) or b in B or b in A:
            a += 1
        else:
            while b < bmax:
                C.append(b)
                b += reverseNum(b)
                if ispalindrome(b):
                    B += C
                    C = []
                    break
                elif b in A or b in B:
                    C=[]
                    break
            A += C
            C=[]
            a += 1
    print(A)

setA(100000,10**20)
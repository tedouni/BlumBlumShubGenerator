import sys


def main():
    #Xo = (s*s)%n
    p = int(sys.argv[1])
    q = int(sys.argv[2])
    s = int(sys.argv[3])
    numberOfBits = int(sys.argv[4])
    n = float(p*q)
    #Test if p & q mod 4 ==3
    if (p%4 == 3):
        pass
    else:
        print '%.02f mod 4 not equal to 3.Parameters not met' %(p)
        sys.exit(-1)
    if (q%4 ==3):
        pass
    else:
        print '%.02f mod 4 not equal to 3.Parameters not met' %(q)
        sys.exit(-1)

    #test gcd(p*q,s)==1
    if(gcd(n,s) == 1):
        print 'Pass all Requirements. Generating bits'
    else:
        print 'fcg(p*q,s) != 1. Did not pass all requirements'
        sys.exit(-1)




    Xo = 0
    rangeOfBits = numberOfBits+1
    print('i\t\tXi\t\t\tBi')
    for i in range (0,rangeOfBits):
        if (i == 0):
            Xo = (s*s)%n
            print("%.02f\t\t%.02f\t\t\t%.02f" % (i,Xo,0)) #str(i)+"\t" +str(Xi)+"\t"+str(Bi)

        else:

            Xi = (Xo*Xo)%n
            Bi = Xi % 2
            print("%.02f\t\t%.02f\t\t\t%.02f" % (i,Xi,Bi)) #str(i)+"\t" +str(Xi)+"\t"+str(Bi)
            Xo = Xi

def gcd(a,b):
    if (a > b):
        smallerValue = b
    else:
        smallerValue = a
    for i in range(1,smallerValue + 1):
        if( (a%i ==0) and (b%i == 0)):
            hcf = i
    return hcf

if __name__ == '__main__':
    main()

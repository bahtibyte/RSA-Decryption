import multiprocessing
import math,time,os

def format(num):
    return "{:,}".format(num)

def found(c,p,q,n,s,e):
    print("Core ",c, " successfully found p * q\n")
    print("P: ",p,"\nq: ",q,"\n\n"+format(p)," * ",format(q)," = ",format(n))
    print("\nDecrypting p and q took ","{0:.2f}".format((e-s) / 60)," mins")

def analyze(c,n,s,e):  

    print("Core ",c," starting to analyze ",format(6*s - 1)," to ",format(6*e + 1))

    pS = time.time()

    p = 6 * s + 1

    for i in range(e-s+1):
        
        p += 4

        if (n % p == 0):
            q = int(n/p)
            found(c,p,q,n,pS,time.time())
            break

        p += 2

        if (n % p == 0):
            q = int(n/p)
            found(c,p,q,n,pS,time.time())
            break
    
    print("Core ",c," analyzed ",format(s)," to ",format(e),"! Took ","{0:.2f}".format((time.time()-pS) / 60)," mins")

def main():

    startTime = time.time()

    userP = 776533697
    userQ = 37270792891

    n = userP * userQ

    maxI = math.ceil(math.sqrt(n) / 6)

    print("===========================================================")
    print("Starting Decryption!\nGiven N = ","{:,}".format(n))
    print("\nTotal number of primes under N is ",format(maxI*2))
    print("Each Core calculates",format(int(maxI/4)),"\n")

    processes = []

    div = math.ceil(maxI / os.cpu_count())

    for i in range(os.cpu_count()):
        s = div * i + 1
        e = div * (i + 1)

        processes.append(multiprocessing.Process(target=analyze,args=(i,n,s,e,)))
        
        
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()

    endTime = time.time()
    print("\nFinished Decryption. Process Finished! Took ","{0:.2f}".format(endTime-startTime),'seconds')
    print("===========================================================")

if __name__ == "__main__":
    main()

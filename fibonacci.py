def fib1(n):
        seq=list(range(n+1))
        seq[0]=0
        seq[1]=1
        if(n>1):
                for i in range(2,n+1):
                        seq[i]=seq[i-1]+seq[i-2]
        return(seq[n])

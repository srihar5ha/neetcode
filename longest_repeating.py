import collections


def main():
    s="ABCDABBCABB"
    k=5
    print(my_func(s,k))

def my_func(s,k):
    x=0
    lp=0
    rp=1
    dct={}
    max_len=0
    dct[s[lp]]=1
    for lp in range(0,len(s)):
        while(x<k+1 and rp<len(s)):
            dct[s[rp]]=1+dct.get(s[rp],0)
            x=rp-lp+1-max(dct.values())
            if(x<k+1):
                max_len=max(max_len,rp-lp+1)
            #print(dct,rp,k,max_len)
            rp+=1
        #print(rp,max_len)
        dct[s[lp]]=dct[s[lp]]-1
        lp+=1
        x=x-1
    return (max_len)

if __name__=='__main__':
    main()
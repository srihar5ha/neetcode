def main():
    s="abab"
    t="ab"

    print(myfunc2(s,t))

def myfunc(s,t):
    ds={}
    dt={}
    lp=0
    rp=0
    min_string=s
    flag=0
    
    for i in t:
        dt[i]=1+dt.get(i,0)
    for rp in range(len(s)):
        ds[s[rp]]=1+ds.get(s[rp],0)
        while(check(ds,dt,s,t)):
            flag=1
            print(lp,rp)
            if(rp-lp+1 < len(min_string)):
                min_string=s[lp:rp+1]
                print(min_string)
            ds[s[lp]]=ds[s[lp]]-1
            lp+=1
    return (min_string if flag==1 else "")



def myfunc2(s,t):
    ds={}
    dt={}
    lp=0
    rp=0
    min_string=s
    flag=0
    
    for i in t:
        dt[i]=1+dt.get(i,0)
    for rp in range(len(s)):
        ds[s[rp]]=1+ds.get(s[rp],0)
        if(check(ds,dt,s,t)):
            flag=1
            print(lp,rp)
            if(rp-lp+1 < len(min_string)):
                    min_string=s[lp:rp+1]
            print("min string is ",min_string)
            while(lp<rp and ds.get(s[lp],0)>dt.get(s[lp],0)):
                ds[s[lp]]=ds[s[lp]]-1
                if(rp-lp+1 < len(min_string)):
                    min_string=s[lp:rp+1]
                    print(min_string)
                lp+=1
            if(rp-lp+1 < len(min_string)):
                    min_string=s[lp:rp+1]
            
            
    return (min_string if flag==1 else "")




def check(ds,dt,s,t):
    print("ds= ",ds)
    for i in range(len(t)):
        if(ds.get(t[i],0)>=dt[t[i]] ):
            pass
        else:
            return 0
    return 1

if __name__=="__main__":
    main()


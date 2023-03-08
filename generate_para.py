def generate(n,na,nb):
    print(na,nb)
    res=""
    if(na<n):
        res=res+("a"+generate(n,na+1,nb))
    if(na<=n and nb<na):
        res=res+("b"+generate(n,na,nb+1))
    if(na==nb==n):
        print("===== ",res)
    return res 

def main():
    s=""
    res=[]
    n=3
    def backtrack(open_count,close_count):
        nonlocal s
        if open_count==close_count==n:
            res.append("".join(s))
            return
        
        if open_count<n:
            s=s+"("
            backtrack(open_count+1,close_count)
            s=s[:-1]
        if close_count<open_count:
            s=s+")"
            backtrack(open_count,close_count+1)
            s=s[:-1]
        
    backtrack(0,0)
    print(res)


if __name__=="__main__":
    main()

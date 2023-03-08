def main():
    s="]"
    print(s)
    print(valid_paran(s))

def valid_paran(s):
    
    arr=[]
    for i in s:
        if(i=='(' or i=='{' or i=='['):
            arr.append(i)
            #print(arr)
        elif(i==')'):
                if(arr and arr[-1]=='('):
                    del arr[-1]
                else:
                    return 0
        elif(i==']'):
                if(arr and arr[-1]=='['):
                    del arr[-1]
                else:
                    return 0
        elif(i=='}'):
                if(arr and arr[-1]=='{'):
                    del arr[-1]
                else:
                    return 0
    return 1 if arr==[] else 0

if __name__=="__main__":
    main()
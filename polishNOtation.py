def polish(tokens):
    a=[]
    signs=["+","-","*","/"]

    for i in tokens:
        if i  not in signs:
            a.append(i)
            print("arr is ",a)
        else:
            x=a.pop()
            y=a.pop()
            res=int(eval(y+i+x))
            print("res ",res)
            a.append(str(res))
    return a



def main():
    tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(polish(tokens))


if __name__=="__main__":
    main()

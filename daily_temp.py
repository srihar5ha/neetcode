def dailyTemp(temperatures):
    output=[0]*len(temperatures)
    stack=[]
    for i,t in enumerate(temperatures):
        while stack and t >stack[-1][0]:
            stackT,stackInd=stack.pop()
            output[stackInd]=i-stackInd
        stack.append((t,i))
    return output
     

def main():
    t=[73,74,75,71,69,72,76,73]
    print(dailyTemp(t))


if __name__=="__main__":
    main()
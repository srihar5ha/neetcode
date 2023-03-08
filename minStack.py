class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        val =min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)




    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        

def main():
        
    #Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    val1=2
    obj.push(val1)
    val2=-1
    obj.push(val2)
    val3=3
    obj.push(val3)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3,param_4)


if __name__=="__main__":
    main()
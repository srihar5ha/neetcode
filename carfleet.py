def carfleet(target,position,speed):
    output=0
    stat=[]
    for i in range(len(position)):
        stat.append((position[i],speed[i]))
    stat.sort()
    #print("original stat ",stat)
    while(stat and len(stat)>1):
        p2,v2=stat.pop()
        p1,v1=stat[-1]
        #print("p2v2 ",p2,v2,p1,v1)
        #print(type(p1),type(v1),type(p2),type(v2))
        print((target-p2 )/ v2)
        if ( ((target-p2) / v2) >= ((target-p1) / v1) ):
           # print("inside")
            stat.pop()
            stat.append((p2,v2))
           # print("p2v2 ",p2,v2)
        else:
            output+=1
        #print("stat is ",stat)
    if(len(stat)==1):
        output+=1

    #print(output)

    return output


def main():
    target = 10
    position = [3]
    speed = [3]
    carfleet(target,position,speed)






if __name__=="__main__":
    main()
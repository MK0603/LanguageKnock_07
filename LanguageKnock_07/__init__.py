def template():
    tmp=[]
    x=input("x= ")
    y=input("y= ")
    z=input("z= ")
    print(x,end="")
    print("時の",end="")
    print(y,end="")
    print("は",end="")
    print(z,end="")
    tmp.append(x)
    tmp.append("時の")
    tmp.append(y)
    tmp.append("は")
    tmp.append(z)
    result ="".join(tmp)
    return result

template()
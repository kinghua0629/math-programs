d=float(input("本金："))
e=float(input("利率："))
f=int(input("期数："))



def money(principal,period,rate):     #principal=本金，period=期数，rate=利率
    ans=0
    for i in range(0,period,1):
        ans=ans+(1+rate)**i
        i=i+1
    x=principal*((1+rate)**(period))/ans
    return(float(x))

print("每月应付款",float(money(d,f,e)))
a = int(input("请输入第一个数\n"))

b= int(input("请输入第二个数\n"))

c =input("请输入运算\n 1.加 2.减 3.乘 4.除\n")

if c=='1' :print (a,"+",b,"=",a+b)
elif c=='2':print (a,"-",b,"=",a-b)
elif c=='3':print (a,"×",b,"=",a*b)
elif c=='4':print (a,"÷",b,"=",a/b)
else :print ("不存在的><")
def GenList(n):
    result=[]
    for i in range(1,n+1):
        result.append(i)
    return result

def MakeFizzBuzz(n):
    result=n
    if n%3==0:
        result="Fizz"
    if n%5==0:
        result="Buzz"
    if n%3==0 and n%5==0:
        result="FizzBuzz"
    return result

def FizzBuzz(array):
    result=[]
    for i in array:
        # print (MakeFizzBuzz(i))
        temp=MakeFizzBuzz(i)
        result.append(temp)
    return result
       
array=[1,32,23,321,465,89,12,85,3,968,1,]
rgpagvf=FizzBuzz(array)
print (rgpagvf)

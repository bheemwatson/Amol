num = int(input("enter a number:"))
if num == 1:
    print(num,'is not a prime number')
elif num>1:
    for j in range(2,num):
      if (num%j)==0:
        print(num," is not a prime number1")
        break
    else:
        print(num,'is a prime number')


name = input('enter the string:')
print('This is original string',name)
print('This is new reversed string',name [::-1])

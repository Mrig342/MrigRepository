#Find the factorial of a number
x=int(input('Enter the number: '))
y=1
while x>=2:
    y=y*x
    x-=1
print("the factorial of the number is: ", y)


#Find if a number is present in a list and show its position using Linear search
pos=0    #defined globally
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i   #if we give only 'pos=i' then it will be treated as local variable, so we need to make it global
            return True
        i+=1
    return False

list=[2,5,9,12,17,23,29,35,41,47]
n=int(input("Enter the number: "))

if search(list,n):
    print("Number is found at position ",pos+1)
else:
    print("Number is not found")
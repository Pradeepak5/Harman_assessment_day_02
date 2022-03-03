number = int (input("Enter a number :"))
temp=number
reverse=0
while(number>0):
    rem=number%10
    reverse=(reverse*10)+rem
    number//=10

if(temp == reverse):
    print("number is palinndrome")
else:
    print("number is not a palindrome")
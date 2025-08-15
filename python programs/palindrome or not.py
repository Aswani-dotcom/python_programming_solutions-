num=int(input())
temp=num
rem,rev=0,0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if rev==temp:
    print('palindrome')
else:
    print('palindrome')

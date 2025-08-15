string=input("enter a string: ")
count={}
for char in string:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print("character frequencies: ")
for char in count:
    print(char,":",count[char])

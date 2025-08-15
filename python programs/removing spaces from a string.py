string=input("ennnter a string")
empty=" "
for char in string:
    if char not in[' ']:
        empty+=char
print("string without spaces:",empty)

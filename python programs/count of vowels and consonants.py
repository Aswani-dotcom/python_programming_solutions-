str=input('enter a string: ')
list='aeiouAEIOU'
vowel_count=0;
consonant_count=0
for char in str:
    if char in list:
        vowel_count+=1
    else:
        consonant_count+=1
print('vowel count',vowel_count)
print('consonant count',consonant_count)



        


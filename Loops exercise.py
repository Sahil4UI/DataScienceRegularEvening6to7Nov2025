'''
x = "aaabbccddeefff"
#question: remove duplicates from String
result = ""
for c in x:
    if c not in result:
        result += c
print(result)
'''
'''
#find the reverse of String
x = "hello"
#print(x[::-1])
for i in reversed(range(len(x))):
    print("The String is :" ,x[i],sep="😋")
'''
#find the no of vowels and consonants in a given string
x = "hey Lets play87654"
vowels = "aeuio"
v_count,c_count,d_count=0,0,0

for c in x:
    if c.isalpha():
        if c in vowels:
            v_count+=1
        else:
            c_count+=1
    elif c.isdigit():
        d_count+=1

print(v_count)
print(c_count)
print(d_count)

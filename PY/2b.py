def reverse(str1):
    str2=''
    for i in str1:
        str2=i+str2
    return(str2)
word=input("Enter a string:")
print("The reverse of the string is ",reverse(word))

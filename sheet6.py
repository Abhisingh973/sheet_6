
'''1=> 
Write a program to input T strings (S) from user and print count of vowels and consonants in it.
 Input:
 2
 List
 Apple
 '''
T=int(input("Enter number of strings: "))
for i in range(T):
    s=input()
    vowels=0
    consonants=0
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
            vowels+=1
    else:
            consonants+=1
print(vowels, consonants)





2=>
string= input()
print(len(string))





#3=>
T= int(input())
result=[]
for i in range(T):
    s= input()
    if s==s[::-1]:
        result.append(1)
    else:
        result.append(0)
for r in result:
    print(r)





#4=>
A="**h*e*l*lo*" 
print(A.strip("*"))



#5>
A="**h*e*l*lo*"    
result=A.lstrip("*")    
print(result)




#6=>
A= "**h*e*l*lo*"  
result=A.rstrip('*') 
print(result)





#7=>
T="String"
print(T[::-1])





#8=>
T="Suyash Chaudhary"
result= T.split()
print(result[1],result[0])







#9=>
string= "Everyone loves data science" 
string=string.split()   
print(string[0][::-1], string[1][::-1], string[2][::-1], string[3][::-1]) 




#10=>
A= "PythoN"        
result= A.lower()  
print(result)




#11=>
A= "pYthON"        
result= A.upper()   
print(result)





#12=>
A= "Python45"         
if A.isalnum():         
    print(1)           
else:                 
    print(0) 




#13=>
A= "Python"         
if A.isalpha():      
    print(1)          
else:                  
    print(0) 






#14=>
A= "aabbcc"
B=98
result= A.find(chr(B))
print(result) 






#15=>
A = "aabababaa"
B = "ba"
result = A.find(B)  
print(result) 





#16=>
A= "abobc"     
result= A.count("bob") 
print(result) 




#17=>
''' Akash likes playing with strings. One day he thought of applying following operations on the
 string in the given order:
 Concatenate the string with itself.
 Delete all the uppercase letters.
 Replace each vowel with '#'.
 You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the
 resultant string after applying the above operations.
 NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.
 Input:
 A="aeiOUz"
 Output:
 "###z###z"
 '''

A="aeiOUz"
b=A+A
res=" "
for i in range(0,len(b)):
    if b[i] not in 'AEIOU':
        if b[i] in 'aeiou':
            res+='#'
        else:
            res+=b[i]
print(res)

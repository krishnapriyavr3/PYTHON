s=input("Enter a sentence")
c=len(s)
print("The count of character in the string is ",c)
l=s.lower()
print("Lowercase :",l)
u=s.upper()
print("Uppercased :",u)
new=s.replace(" ","_")
print("Replaces sentence is",new)
word="python"
if word in s:
   print("the word is present in the sentence")
else:
   print("The word is not present in the sentence")   


s= input("Input a list of student scores ").split()
# print(type(s),len(s))
for n in range(0,len(s)):
  s[n] = int(s[n])
print(s)

c=0
for b in s:
  if(b>c):
    c=b
print("highest score in the class is:",c)  




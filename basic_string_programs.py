#basic string programs:
#wap to  reverse internal content of each word:
#x = input()
#y=[]
#for i in (x.split()):
 #   y.append(x[::-1])
#print("".join(y))

#wap to find the character present at present at odd position and given position

#strr = input()
#for i in range(0,len(strr),2):
 #   print(strr[i],end=" ")
#print(" ")
#for i in range(1,len(strr),2):
 #   print(strr[i],end=" ")
#print(" ") 

#acha program - wap to find the substring in a given string where sumaation of substring is divisible by 5:
#x = "hiiamsupersleepy"
#test = 'abcdefghijklmnopqrstuvwxyz'
#summ= 0 
#for i in range (0, len(x)):
    #for j in range (i+1, len(x)):
     #   y = x[i:j+1]
      #  for a in y:
       #     summ+= (test.index(a)+1)
        #if summ%10 == 0 :
          #        print(y)

#next method:
#x = "hiiamsupersleepy"
#summ= 0
#for i in range (0, len(x)):
 #    q = ord(x[i])
  #   n = q - 97
   #  print(n) 

    #for j in range (i+1, len(x)):
     #   y = x[i:j+1]
      #  for a in y:
       

#PASSWORD VALIDATION : #isdigit() #isalnum #istitle #isupper #islower
password = input()
upper = 0
lower = 0
digit = 0
special = 0
if len(password) >= 8:
         for i in password:
            if i.isdigit():
                digit += 1
            elif i.isalpha():
                    if i.islower():
                       lower+= 1
                    else :
                           upper += 1
            elif i == '@'or i == '$' or i == '!' or i == "." :
                    special += 1 
            
              
else :
    print("false")
if digit >=1 and lower>= 1 and upper >= 1 and special >= 1 :
    print("true")
else :
    print("false")

   

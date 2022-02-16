print("----------------PHONE BOOK-----------")
print("0.QUIT")
print("1.ADD PHONE NUMBER TO THE PHONE BOOK")
print("2.SEARCH PHONE NUMBER IN THE PHONE BOOK")

d1={}
while True:
   n=int(input("Enter number [0/1/2]:-"))
   if n==1:
      name=input("Enter the Name:-")
      phone=input("Enter the phone number:-")
      d1[name]=phone
   elif n==2:
      name1=input("Enter name to SEARCH for phone number in the phone book")
      print("phone number of;-",name1,"is",d1[name1])
   elif n==0:
      break

# #camel casing
# noOfCars = 0
# noOfBikes = 0
# totalpayment = 0
# noOfCars = int(input("no. of cars"))
# noOfBikes = int(input("no. of bikes"))
# totalpayment = noOfBikes*20+noOfCars*40
# print("total payment is:", totalpayment)


Product1 = 40
Product2 = 50
Product3 = 60
product4 = 70
product5 = 80

##using input function
quantity1=int(input("enter the quantity of product1:"))
quantity2=int(input("enter the quantity of product2:"))
quantity3=int(input("enter the quantity of product3:"))
# quantity4=int(input("enter the quantity of product4:"))
# quantity5=int(input("enter the quantity of product5:"))


#using the list
# l=[quantity1,quantity2,quantity3]

# ##using for loop
# for i in l:
#     print(i)



##using if else statement
if((quantity1<=0)or(quantity2<=0)or(quantity3<=0)):
    print("please enter a positive value")
else:
    totalamount=Product1*quantity1 +Product2*quantity2+Product3*quantity3
    x = open("mydata.txt", "a")
    print("the quantity and cost of products is:")
    print("the quantity and cost of products is:",file=x)
    # x.close()
    entries = { quantity1 : 40,quantity2 : 50,quantity3 : 60}
    for i,p in entries.items():
        print(i,p)
        print(i,p, file=x)
print("the amount that you need to pay is: ", totalamount)
print("the amount that you need to pay is: ", totalamount, file=x)










# if(quantity1<=0 or quantity2<=0):
#     print("Enter a positive number")

# quantity3=int(input("enter the quantity of product3"))
# p1amount=Product1*quantity1
# p2amount=Product2*quantity2
# p3amount=Product3*quantity3
# totalamount=p1amount+p2amount+p3amount
# print("the total amount you need to pay is:",totalamount)



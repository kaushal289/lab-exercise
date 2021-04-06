'''Price of a house is $1M. if buyer has good credit, they need to put down 10% otherwise
 they need to put down 20%.print the down payment.'''

price_house=1000000
credit=input("enter if the buyer has good credit (yes or no):")
if credit=="yes":
    credit=True
if credit==True:
    price_housex=price_house*(10/100)
else:
    price_housex=price_house*(20/100)
print(f'the down paymenr is  ${price_housex}')


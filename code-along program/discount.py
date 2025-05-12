from datetime import datetime
DISCOUNT_RATE=.1
TAX_RATE=.06
today=datetime.now()
dow=today.weekday()
subtotal=0
quantity=1
while quantity !=0:
   quantity=int(input("Enter your quantity? " ))
   if quantity !=0:
     price=float(input("Enter your price? "))
     subtotal+=quantity * price

# subtotal= float(input("Enter Sub-total? "))
print(f"Total Order: {subtotal}")
discount=0
# if  dow==2 or dow==3 or dow==5:
if dow in[2,4,5]:
    if subtotal > 50:
     discount= round(subtotal * DISCOUNT_RATE,2)
     print(f"Discount: {discount:.2f}")
    else:
       short=50-subtotal
       print(f"you can get a subtotal by ordering {short:.2f} more. ")
subtotal -=discount
tax=round(subtotal * TAX_RATE,2)
total=subtotal + tax

print(f"Tax: {tax:.2f}")
print(f"Total Due: {total:.2f}")
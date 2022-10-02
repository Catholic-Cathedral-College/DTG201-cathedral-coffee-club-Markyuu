#Adding imports
import time

#Welcome to the cafe 
print("               ----------------------------------------------------")
print("             -- 𝒲𝑒𝓁𝒸🏵𝓂𝑒 𝓉♡ 𝓉𝒽𝑒 𝓂♡𝓈𝓉 𝒻𝒶𝓂♡𝓊𝓈 𝒸𝒶𝒻𝑒 𝒾𝓃 𝓉𝒽𝑒 𝓌𝒽♡𝓁𝑒 𝓌♡𝓇𝓁𝒹 --")
print("               ----------------------------------------------------")
time.sleep(1)
print("\n")
print("Note: pls use numbers to order")
print("Note: This cafe only accepts card payment method")
print("\n")

#Displaying the menu nad the prices
print("    *´¯`*.¸¸.*´¯`*   🎀  𝒯𝒽𝒾𝓈 𝒾𝓈 𝓌𝒽𝒶𝓉'𝓈 𝒶𝓋𝒶𝒾𝓁𝒶𝒷𝓁𝑒 𝒾𝓃 ♡𝓊𝓇 𝒸𝒶𝒻𝑒  🎀   *`¯´*.¸¸.*`¯´*")
time.sleep(2)
print("\n")
print("                          (1)    Hot Chocolatte,  ($4,00)")
time.sleep(1)
print("                          (2)      Flat White,    ($3.00)")
time.sleep(1)
print("                          (3)      Cappuccino,    ($3,00)")
time.sleep(1)
print("                          (4)        Latte,       ($3,50)")
time.sleep(1)
print("                          (5)        Decaf,       ($3,00)")
time.sleep(1)

#Coffee prices list
prices = [
    "4.00",
    "3.00",
    "3.00",
    "3.50",
    "3.00",
]


# While loop until user is ready to order
ordering = "no"
while ordering != "yes":
  ordering = input("\n Are you ready to order now?: ")
  if ordering == "yes":
    print()
    
#order
order = int(input("What coffee would you like to order?: "))
#Quantity
quantity = int(input("How many coffees would you like to order?: "))
#name
name = input("Under what name do you want you order under?: ")
#Sugar
def sugar():
    sugar = input("\n Would you like sugar with your order?: ")
    if sugar.lower().format() == "yes":
        print(" [yes to sugar] ")
    elif sugar.lower().format() == "no":
        print(" [Okay no sugar] ")

#Order 1 Hot Chocolatte
if order == 1:
    print("\n You chose a Hot Chocolatte")
    total =  int(quantity) * float(prices[0])
    sugar()
    print(" {} your total order is ${}".format(name,total))
    time.sleep(2)

#Order 2 Flate White
if order == 2:
    print("\n You chose a Flat White")
    total =  int(quantity) * float(prices[1])
    print(" {} your total order is ${}".format(name,total))
    time.sleep(2)

#Order 3 Cappuccino
if order == 3:
    print("\n You chose a Cappuccino")
    total =  int(quantity) * float(prices[2])
    print(" {} your total order is ${}".format(name,total))
    time.sleep(2)

#Order 4 Latte
if order == 4:
    print("\n You chose a Latte")
    total =  int(quantity) * float(prices[3])
    print(" {} your total order is ${}".format(name,total))
    time.sleep(2)

#Order 5 Decaf
if order == 5:
    print("\n You chose a Decaf")
    total =  int(quantity) * float(prices[4])
    print(" {} your total order is ${}".format(name,total))
    time.sleep(2)

#Reciept
def reciept():
    print("\n")
    print("~" * 30)
    print("Reciept for {}\n".format(name))
    print("order: {}".format(order))
    print("quantity:{}\n".format(quantity))
    print("{} your total order is ${}\n".format(name,total))
    print("~" * 30)



reciept()

payment = input("How would you like to pay for your order? Card or Cash: ")
if payment.lower().strip() == "card":
      print("Processing payment...")
      time.sleep(1)
      print("Your card was charged {}".format(total))
      time.sleep(1)
      print("Thank you for your purchase")
elif payment.strip().lower() == "cash":
         cash = input("Please input the amount of cash you would like to pay with: ")
         total_order = total - int(cash)
         total_order = abs(total)
         if total > 0:
            print("Here is your change ${}".format(total))
         elif total <= 0:
            print("You do not have enough money")
         else:
            print("Invalid input")
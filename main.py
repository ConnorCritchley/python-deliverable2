#Deliverable 2
#Connor Critchley
#7/24/24

#inital prompts/prints
print("Welcome to GC fruit market!")
name = input("What is your name? ")
flag = True #loop flag
subtotal = 0 #purchase total
apples = 0
grapes = 0 #initialize fruit counts
oranges = 0

#main loop (while not done)
while flag:
    print(f"\nWelcome {name}. Which fruit would you like to buy?\n"
          f" 1. Apple $2\n"
          f" 2. Grape $1\n"
          f" 3. Orange $3")
    buy = int(input())
    if buy == 1:
        subtotal += 2
        apples += 1
        print("You bought 1 apple at $2")
    elif buy == 2:
        subtotal += 1
        grapes += 1
        print("You bought 1 grape at $1")
    elif buy == 3:
        subtotal += 3
        oranges += 1
        print("You bought 1 orange at $3")
    else:
        print("Invalid response.")

    #check for loop break
    ask = input("Would you like to buy another piece of fruit? y/n ")
    if ask == "n":
        flag = False

#print reciept/totals
print(f"\nOrder for {name}\n"
      f"{apples} apples(s) at $2 apiece\n"
      f"{grapes} grapes(s) at $1 apiece\n"
      f"{oranges} orange(s) at $3 apiece")
print("Sub Total:", subtotal)
tax = subtotal * .05
print("5% Tax:", tax)
print("Total:", subtotal + tax)

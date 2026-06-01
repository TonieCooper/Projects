print("Welcome to the Tip Calculator!")

# create input for bill cost
bill = input("What is the cost of the bill? ")

# create input for tip as a %
tip = input("How much would you like to tip? 10, 12, 15 or 20% ")

# create input for amount of people
people = input("How many people will be splitting the bill? ")

# convert bill to a float, tip to an int and people to an int
bill_float = float(bill)
tip_int = int(tip)
people_int = int(people)

# calculate tip as a decimal
tip_math = bill_float * (tip_int / 100)

#calulate bill plus tip divided by number of people 
total = (bill_float + tip_math) / people_int

# round decmal to 2 places
total_rounded = "{:.2f}".format (total)

#show results
print(f"Each person should pay a total of ${total_rounded}")

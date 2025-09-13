# Count all the leap year from your birth date till now
birth_year = int(input("Enter your Birth Year: "))

for leap_year in range(birth_year, 2025):
    if leap_year % 4 == 0 and leap_year % 100 != 0:
        print("Leap Year: ", leap_year)

print("\n\n")

# Take 10 products prices from user and sum them 
sum = 0

for i in range(10):
    product_price = float(input(f"Enter price of product{i+1}: "))
    sum += product_price

print("\nYour total of 10 products is: ", sum)
        
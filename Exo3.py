def main():
 total_amount = float(input("Total amount: "))
num_items = int(input("Number of items: "))
day_of_week = input("Day of the week: ").strip().capitalize()

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    discount = 0.10  
elif day_of_week in ["Saturday", "Sunday"]:
    discount = 0.20  
else:
    print("Invalid day of the week. Please try again.")
    exit()

if num_items > 5:
    discount += 0.05

total_price = total_amount * (1 - discount)

print(f"Total price after discount: {total_price:.1f} dinars")

if __name__ == "__main__":
    main()
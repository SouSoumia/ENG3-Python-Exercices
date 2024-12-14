def main():
 name = input("Please enter your name: ")

if name == "VIP":
    print("Enjoy the show for free!")
else:
    tickets = int(input("How many tickets would you like to buy? "))
    
    ticket_price = 15.50
    total_cost = tickets * ticket_price
    
    print(f"The total cost is {total_cost}")
    print("Enjoy your tickets!")

if __name__ == "__main__":
    main()
def main():
  price = float(input("Please type in a price: "))

dinars = int(price)  
centimes = round((price - dinars) * 100)  


print(f"Dinars: {dinars}")
print(f"Centimes: {centimes}")

if __name__ == "__main__":
    main()
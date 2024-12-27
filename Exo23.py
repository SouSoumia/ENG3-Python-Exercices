def main():
 try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("The number must be positive.")
    else:
        for i in range(-n, n + 1):
            if i != 0:
                print(i)
 except ValueError:
    print("Invalid input. Please enter a positive integer.")
if __name__ == "__main__":
    main()
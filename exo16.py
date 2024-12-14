def main():
    numbers = [1, 2, 3, 4, 5]
    
    while True:
        try:
            index = int(input("Enter index (-1 to quit): "))
            
            if index == -1:
                break
            
            if index < 0 or index >= len(numbers):
                print("Invalid index! Please enter a valid index.")
                continue
            
            new_value = input("Enter new value: ")
            if not new_value.isdigit():   
                print("Invalid value! Please enter a numeric value.")
                continue
            new_value = int(new_value)
            
            numbers[index] = new_value
            
            print(numbers)
        
        except ValueError:
            print("Invalid input! Please enter valid integer values.")
    
if __name__ == "__main__":
    main()

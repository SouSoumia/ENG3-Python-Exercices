def display_menu():
    print("\nMenu:")
    print("1. Append")
    print("2. Insert")
    print("3. Pop")
    print("4. Remove")
    print("5. Sort")
    print("6. Reverse")
    print("7. Search")
    print("8. Save to File")
    print("9. Load from File")
    print("10. Quit")


def main():
    # Initialize the list
    numbers = [1, 2, 3, 4, 5]
    print(f"Initial List: {numbers}")

    while True:
        # Display menu
        display_menu()
        
        try:
            # Get user input for the menu
            choice = int(input("Choose an option: "))

            if choice == 1:  # Append
                value = int(input("Enter value to append: "))
                numbers.append(value)
                print(f"Updated List: {numbers}")
            
            elif choice == 2:  # Insert
                value = int(input("Enter value to insert: "))
                index = int(input("Enter index to insert at: "))
                if 0 <= index <= len(numbers):
                    numbers.insert(index, value)
                    print(f"Updated List: {numbers}")
                else:
                    print("Error: Index out of range.")
            
            elif choice == 3:  # Pop
                if numbers:
                    index = int(input("Enter index to pop (or press Enter to pop last): ") or -1)
                    if index == -1:
                        removed = numbers.pop()
                    elif 0 <= index < len(numbers):
                        removed = numbers.pop(index)
                    else:
                        print("Error: Index out of range.")
                        continue
                    print(f"Popped value: {removed}")
                    print(f"Updated List: {numbers}")
                else:
                    print("Error: List is empty.")
            
            elif choice == 4:  # Remove
                value = int(input("Enter value to remove: "))
                if value in numbers:
                    numbers.remove(value)
                    print(f"Updated List: {numbers}")
                else:
                    print("Error: Value not found in the list.")
            
            elif choice == 5:  # Sort
                numbers.sort()
                print(f"List sorted: {numbers}")
            
            elif choice == 6:  # Reverse
                numbers.reverse()
                print(f"List reversed: {numbers}")
            
            elif choice == 7:  # Search
                value = int(input("Enter value to search for: "))
                if value in numbers:
                    index = numbers.index(value)
                    print(f"Value {value} found at index {index}.")
                else:
                    print("Value not found in the list.")
            
            elif choice == 8:  # Save to File
                filename = input("Enter filename to save the list: ")
                with open(filename, "w") as file:
                    file.write(" ".join(map(str, numbers)))
                print(f"List saved to {filename}.")
            
            elif choice == 9:  # Load from File
                filename = input("Enter filename to load the list from: ")
                try:
                    with open(filename, "r") as file:
                        numbers = list(map(int, file.read().split()))
                    print(f"List loaded from {filename}: {numbers}")
                except FileNotFoundError:
                    print(f"Error: File {filename} not found.")
                except ValueError:
                    print("Error: Invalid data in the file.")
            
            elif choice == 10:  # Quit
                print("Goodbye!")
                break
            
            else:
                print("Error: Invalid option. Please choose a valid menu option.")

        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

# Run the program
main()

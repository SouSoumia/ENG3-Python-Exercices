import statistics

def main():
    user_list = []

    print("Enter numbers to add to the list. Enter 0 to stop.")

    while True:
        try:
            num = int(input("Enter a number: ").strip())

            if num == 0:  
                break

            user_list.append(num)

            print(f"Current List: {user_list}")
            print(f"Sorted List (Ascending): {sorted(user_list)}")

        except ValueError:
            print("Error: Please enter a valid integer.")

    if user_list:
        print("\nFinal List Information:")
        print(f"Current List: {user_list}")
        print(f"Sorted List (Ascending): {sorted(user_list)}")
        print(f"Sorted List (Descending): {sorted(user_list, reverse=True)}")

        mean = statistics.mean(user_list)
        median = statistics.median(user_list)
        print(f"Mean: {mean}")
        print(f"Median: {median}")

        save_option = input("Do you want to save the list to a file? (yes/no): ").strip().lower()
        if save_option == "yes":
            filename = input("Enter the filename to save the list: ").strip()
            try:
                with open(filename, "w") as file:
                    file.write("Numbers: " + ", ".join(map(str, user_list)) + "\n")
                    file.write("Sorted (Ascending): " + ", ".join(map(str, sorted(user_list))) + "\n")
                    file.write("Sorted (Descending): " + ", ".join(map(str, sorted(user_list, reverse=True))) + "\n")
                    file.write(f"Mean: {mean}\n")
                    file.write(f"Median: {median}\n")
                print(f"List saved to {filename}.")
            except Exception as e:
                print(f"Error saving file: {e}")

        # Ask the user if they want to load a list from a file
        load_option = input("Do you want to load and append a list from a file? (yes/no): ").strip().lower()
        if load_option == "yes":
            filename = input("Enter the filename to load the list from: ").strip()
            try:
                with open(filename, "r") as file:
                    loaded_numbers = []
                    for line in file:
                        if line.startswith("Numbers:"):
                            loaded_numbers = list(map(int, line.split(":")[1].split(",")))
                            break
                    user_list.extend(loaded_numbers)
                    print(f"Updated Current List: {user_list}")
                    print(f"Sorted List (Ascending): {sorted(user_list)}")
            except FileNotFoundError:
                print(f"Error: File {filename} not found.")
            except ValueError:
                print("Error: Invalid data in the file.")

    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()

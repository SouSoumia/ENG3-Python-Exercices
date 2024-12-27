def main():
# Initialize empty lists
 numbers = []
shoe_sizes = []

# Use append to add items to the lists
# Adding to numbers
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

# Adding to shoe_sizes using a loop
for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)

# Handle duplicates (remove duplicates from numbers)
numbers.append(3)  # Add a duplicate value
numbers = list(set(numbers))  # Remove duplicates by converting to a set and back to a list

# Combine numbers and shoe_sizes into a third list
combined_list = numbers + shoe_sizes

# Print the lists with descriptive labels
print(f"Numbers List: {sorted(numbers)}")
print(f"Shoe Sizes List: {shoe_sizes}")
print(f"Combined List: {combined_list}")
if __name__ == "__main__":
    main()
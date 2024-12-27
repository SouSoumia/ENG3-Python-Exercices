def main():
    unique_words = set()
    total_words = 0  
    print("Enter words one by one. Type a duplicate word to exit.")

    while True:
        word = input("Enter a word: ").strip()

        total_words += 1

        if word.lower() in (w.lower() for w in unique_words):
            print(f"\nYou typed in {len(unique_words)} unique words.")
            print(f"Total words entered: {total_words - 1}")
            print("Unique words (alphabetically):", sorted(unique_words, key=str.lower))

            save_option = input("Do you want to save the unique words to a file? (yes/no): ").strip().lower()
            if save_option == "yes":
                filename = input("Enter the filename to save the words: ").strip()
                try:
                    with open(filename, "w") as file:
                        file.write("\n".join(sorted(unique_words, key=str.lower)))
                    print(f"Unique words saved to {filename}.")
                except Exception as e:
                    print(f"Error saving file: {e}")
            break

        unique_words.add(word)

if __name__ == "__main__":
    main()

def main():
    word = input("Word: ")

    spaces_needed = (30 - len(word)) // 2
    
    frame = '*' * 30
    print(frame)  
    print(' ' * spaces_needed + word + ' ' * (30 - len(word) - spaces_needed))  
    print(frame)  
if __name__ == "__main__":
    main()

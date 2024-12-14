def main():
    width = int(input("Width: "))
    height = int(input("Height: "))
    
    for _ in range(height):
        print('#' * width)

if __name__ == "__main__":
    main()

def main():
    cities = []
    
    while True:
        city_name = input("Enter the name of a city (or 'stop' to end): ")
        
        if city_name.lower() == "stop":
            break
        
        population = len(city_name) * 1000000
        cities.append((city_name, population))
    
    # Sort cities by population (from largest to smallest)
    cities.sort(key=lambda x: x[1], reverse=True)
    
    # Print the cities and their populations
    for city, population in cities:
        print(f"{city}: {population} citizens")

if __name__ == "__main__":
    main()

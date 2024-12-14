
people = int(input("How many people need a ride? "))


capacity = int(input("How many people fit in one taxi? "))

full_taxis = people // capacity

if people % capacity != 0:
    taxis_needed = full_taxis + 1
else:
    taxis_needed = full_taxis

print(f"Number of taxis needed: {taxis_needed}")

slots = [None, None, None, None, None]   

while True:
    print("\n1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Show Parking Slots")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        vehicle = input("Enter vehicle number: ")
        for i in range(len(slots)):
            if slots[i] is None:
                slots[i] = vehicle
                print("Vehicle parked at slot", i+1)
                break
        else:
            print("Parking Full")

    elif choice == 2:
        vehicle = input("Enter vehicle number to remove: ")
        for i in range(len(slots)):
            if slots[i] == vehicle:
                slots[i] = None
                print("Vehicle removed from slot", i+1)
                break
        else:
            print("Vehicle not found")

    elif choice == 3:
        print("\nParking Status:")
        for i in range(len(slots)):
            print("Slot", i+1, ":", slots[i])

    elif choice == 4:
        break

    else:
        print("Invalid choice")
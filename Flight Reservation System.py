#Flight reservation system

flights = {
    "AV-101": {
        "Origin": "Lima",
        "Destination": "Bogota",
        "Seats": ["A1", "A2", "B1", "B2"],
        "Schedule": (15, 30)
    },
    "AV-102": {
        "Origin": "Bogota",
        "Destination": "Miami",
        "Seats": ["A2", "B1", "B2"],
        "Schedule": (17, 30)
    },
    "AV-103": {
        "Origin": "Paris",
        "Destination": "Roma",
        "Seats": ["A1", "B1", "B2"],
        "Schedule": (16, 00)
    }
}


def view_flights():
    print("\nAvailable flights")
    for flight in flights.values():
        print(f"Flight: {flight['Origin']} to {flight['Destination']} ")
        print(f"Schedule: {flight['Schedule'][0]}:{flight['Schedule'][1]}")
        print(f"Available seats: {flight['Seats']}")
        print()


def reserve_seats():
    flight_code = input("Enter flight code: ")
    if flight_code not in flights:
        print("Flight not found")
        return
    print(f"Available seats: {flights[flight_code]['Seats']}")
    seat = input("Enter seat to reserve: ").upper()

    try:
        if seat in flights[flight_code]["Seats"]:
            flights[flight_code]["Seats"].remove(seat)
            print(f"Seat {seat} reserved on flight {flight_code}.")
        else:
            print("Seat not available.")
    except ValueError:
        print("Enter a valid seat.")


def calculate_average_price():
    for code, flight in flights.items():
        price = flight["Schedule"][0] * 100 + flight["Schedule"][1] * 50
        print(f"Flight {code} costs ${price:.2f}")







def generate_report():
    print("\nFlight Report ")
    for code in flights:
        flight = flights[code]
        line = code + " | " + flight["Origin"] + " = " + flight["Destination"]
        line += " | " + str(flight["Schedule"][0]) + ":" + str(flight["Schedule"][1])
        print(line)







def main():
    while True:
        print("\nWelcome to Flight Reservation System")
        print("1. View available flights")
        print("2. Reserve seats")
        print("3. Calculate Average ticket price")
        print("4. Generate report")
        print("5. Exit")

        option = input("Enter your option: ")
        if option == "1":
            view_flights()
        elif option == "2":
            reserve_seats()
        elif option == "3":
            calculate_average_price()
        elif option == "4":
            generate_report()
        elif option == "5":
            print("Exiting of Flight Reservation System.....")
            break
        else:
            print("Invalid option. Please try again. Enter a number between 1 and 6.")


main()

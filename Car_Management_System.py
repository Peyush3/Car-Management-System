import csv
import os
from typing import List

class Car:
    def __init__(self, company, model, color, max_speed, fuel_type, manufacturer, price):
        self.company = company
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.fuel_type = fuel_type
        self.manufacturer = manufacturer
        self.price = price

def write_cars(cars: List[Car]):
    with open("cars.csv", "w", newline="") as csvfile:
        fieldnames = ["Company", "Model", "Color", "MaxSpeed", "FuelType", "Manufacturer", "Price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for car in cars:
            writer.writerow({
                "Company": car.company,
                "Model": car.model,
                "Color": car.color,
                "MaxSpeed": car.max_speed,
                "FuelType": car.fuel_type,
                "Manufacturer": car.manufacturer,
                "Price": car.price
            })

def display_car_details(company: str, cars: List[Car]):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    found = False
    for car in cars:
        if car.company.lower() == company.lower():
            print("\t\t\t ----------------------------")
            print(f"\t\t\t Company: {car.company}")
            print("\t\t\t ----------------------------")
            print(f"\t\t\t Model: {car.model}")
            print(f"\t\t\t Color: {car.color}")
            print(f"\t\t\t Max Speed: {car.max_speed}")
            print(f"\t\t\t Fuel Type: {car.fuel_type}")
            print(f"\t\t\t Manufacturer: {car.manufacturer}")
            print("\n\t\t\t ----------------------------")
            print(f"\t\t\t Price: {car.price}")
            print("\t\t\t ----------------------------")
            found = True
            break

    if not found:
        print("\t\t\t Company not found.")
    else:
        print("\t\t\t Details displayed successfully")

    input("Press Enter to return to the main menu...")  # Wait for user input

def display_cars_in_price_range(cars: List[Car]):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    min_price = int(input("\t Enter the minimum price: "))
    max_price = int(input("\t Enter the maximum price: "))
    print("Cars Within Price Range")
    print("====================================================")
    print("COMPANY         MODEL         COLOR         MAX SPEED        FUEL TYPE         MANUFACTURER         PRICE")
    print("====================================================")
    for car in cars:
        if min_price <= car.price <= max_price:
            print(f"{car.company:<16} {car.model:<14} {car.color:<12} {car.max_speed:<16} {car.fuel_type:<16} {car.manufacturer:<20} {car.price:<6}")
    input("Press Enter to return to the main menu...")  # Wait for user input


def display_all_cars(cars: List[Car]):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    print("Car List")
    print("====================================================")
    print("COMPANY         MODEL         COLOR         MAX SPEED        FUEL TYPE         MANUFACTURER         PRICE")
    print("====================================================")
    for car in cars:
        print(f"{car.company:<16} {car.model:<14} {car.color:<12} {car.max_speed:<16} {car.fuel_type:<16} {car.manufacturer:<20} {car.price:<6}")
    input("Press Enter to return to the main menu...")  # Wait for user input

def add_car(cars: List[Car]):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    company = input("\t\t\t Enter the car company: ")
    model = input("\t\t\t Enter the car model: ")
    color = input("\t\t\t Enter the car color: ")
    max_speed = input("\t\t\t Enter the max speed of the car: ")
    fuel_type = input("\t\t\t Enter the fuel type of the car: ")
    manufacturer = input("\t\t\t Enter the car manufacturer: ")
    price = int(input("\t\t\t Enter the car price: "))

    car = Car(company, model, color, max_speed, fuel_type, manufacturer, price)
    cars.append(car)
    write_cars(cars)
    print("\t\t\t Car Added Successfully!")
    input("\t\t\t Press Enter to return to the main menu...")  # Wait for user input

def delete_car(company: str, cars: List[Car]):
    cars = [car for car in cars if car.company.lower() != company.lower()]
    write_cars(cars)
    print("\t\t\t Record Deleted...")

def update_car(company: str, cars: List[Car]):
    found = False
    for car in cars:
        if car.company.lower() == company.lower():
            print("\t\t\t ----------------------------")
            print(f"\t\t\t Company: {car.company}")
            print("\t\t\t ----------------------------")
            print(f"\t\t\t Model: {car.model}")
            print(f"\t\t\t Color: {car.color}")
            print(f"\t\t\t Max Speed: {car.max_speed}")
            print(f"\t\t\t Fuel Type: {car.fuel_type}")
            print(f"\t\t\t Manufacturer: {car.manufacturer}")
            print("\n\t\t\t ----------------------------")
            print(f"\t\t\t Price: {car.price}")
            print("\t\t\t ----------------------------")

            print("\n\t\t\t ----------------------------")
            print("\t\t\t Update Car Details:")
            car.model = input(f"\t\t\t New Model ({car.model}): ") or car.model
            car.color = input(f"\t\t\t New Color ({car.color}): ") or car.color
            car.max_speed = input(f"\t\t\t New Max Speed ({car.max_speed}): ") or car.max_speed
            car.fuel_type = input(f"\t\t\t New Fuel Type ({car.fuel_type}): ") or car.fuel_type
            car.manufacturer = input(f"\t\t\t New Manufacturer ({car.manufacturer}): ") or car.manufacturer
            car.price = int(input(f"\t\t\t New Price ({car.price}): ") or car.price)

            write_cars(cars)
            print("\t\t\t Record Updated")
            found = True
            break

    if not found:
        print("\t\t\t Car not found.")

def car_management():
    if not os.path.isfile("cars.csv"):
        with open("cars.csv", "w", newline="") as csvfile:
            fieldnames = ["Company", "Model", "Color", "MaxSpeed", "FuelType", "Manufacturer", "Price"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    cars = []
    with open("cars.csv", "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            car = Car(row["Company"], row["Model"], row["Color"], row["MaxSpeed"], row["FuelType"], row["Manufacturer"], int(row["Price"]))
            cars.append(car)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
        print("\t\t ---------------------------------------")
        print("\t\t | Welcome to the Car Management System |")
        print("\t\t ---------------------------------------")
        print("\n\t --- Main Menu ---")
        print("\t 1. View Car Details")
        print("\t 2. View All Cars")
        print("\t 3. Add Car")
        print("\t 4. Update Car")
        print("\t 5. Delete Car")
        print("\t 6. Display Cars Under a Certain Price")
        print("\t 7. Exit")
        print()

        choice = input("\t Enter your choice (1-6): ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            company = input("\t Enter the car company: ")
            display_car_details(company, cars)

        elif choice == '2':
            display_all_cars(cars)

        elif choice == '3':
            add_car(cars)

        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            company = input("\t Enter the car company: ")
            update_car(company, cars)

        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            company = input("\t Enter the car company: ")
            delete_car(company, cars)

        elif choice == '6':
            display_cars_under_price(cars)

        elif choice == '7':
            print("\t Thanks for using the Car Management System")
            break

if __name__ == "__main__":
    car_management()
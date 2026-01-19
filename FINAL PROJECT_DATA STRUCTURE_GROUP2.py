import os
from datetime import datetime
import random
import time

def display_seats(movie_seats):
    os.system('cls')
    print("Available Seats: ")
    for start in range(1, 51, 10):
        for seat in range(start, start + 10):
            if seat in movie_seats:
                if seat < 10:
                    print(f" {seat}", end=" ")
                else:
                    print(f"{seat}", end=" ")
            else:
                print("  ", end=" ")
        print()

def generate_TID():
    while True:
        tid = random.randint(1000, 9999)
        if tid not in ids:
            ids.append(tid)
            return tid

def confirm_order(movie_number, seat_number, price):
    tid = generate_TID()
    orders[tid] = {
        "Movie Number": movie_number,
        "Seat Number": seat_number,
        "Price": price,
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    match(movie_number):
        case 1:
            movie1seats.remove(seat_number)
        case 2:
            movie2seats.remove(seat_number)
        case 3:
            movie3seats.remove(seat_number)
    os.system('cls')
    print(f"Order ID: {tid}\nMovie Number: {movie_number}\nSeat Number: {seat_number}\nPrice: {price}")    
    time.sleep(3)

def book_seat(movie):
    while True:
        display_seats(movie)
        seat_choice = tryparse(input("Which seat would you like to book? "))
        if seat_choice in movie:
            if movie == movie1seats:
                price = 320
                movie_number = 1
            elif movie == movie2seats:
                price = 340
                movie_number = 2
            else:
                price = 360
                movie_number = 3
            os.system('cls')
            print(f"Movie Number: {movie_number}\nSeat Number: {seat_choice}\nPrice: {price}")
            confirm = input("Press Y to Confirm: ").upper()
            if confirm == "Y":
                confirm_order(movie_number, seat_choice, price)
                os.system('cls')
                break
            else:
                os.system('cls')
                print("Order Cancelled.")
                time.sleep(3)
                os.system('cls')
                break
        else:
            os.system('cls')
            print("Invalid Seat")
            os.system('cls')


def book_order():
    os.system('cls')
    movie_choice = tryparse(input("Select a movie:\n1. Movie 1\n2. Movie 2\n3. Movie 3\nEnter choice (1-3): "))
    match(movie_choice):
        case 1:
            book_seat(movie1seats)
        case 2:
            book_seat(movie2seats)
        case 3:
            book_seat(movie3seats)
        case _:
            os.system('cls')
            print("Invalid Choice. Please Choose Between 1-3.")
            time.sleep(3)
            book_order()

def update_check(movie, seat):
    match(movie):
        case 1:
            if seat in movie1seats:
                return True
            else:
                return False
        case 2:
            if seat in movie2seats:
                return True
            else:
                return False
        case 3:
            if seat in movie3seats:
                return True
            else:
                return False


def update_order(tid):
    info = orders[tid]
    print(f"Order ID: {tid}, Movie Number: {info['Movie Number']}, Seat Number: {info['Seat Number']}, Price: {info['Price']}, Order Date: {info['Time']}")
    print("\nEnter New Informations: ")
    newmovie = tryparse(input("Movie Number: "))
    
    newseatnumber = tryparse(input("Seat Number: "))

    if newmovie or newseatnumber and update_check(newmovie, newseatnumber):
        if not newmovie:
            newmovie = info['Movie Number']
        if not newseatnumber:
            newseatnumber = info['Seat Number']
        match(newmovie):
            case 1:
                movie1seats.remove(newseatnumber)
            case 2:
                movie2seats.remove(newseatnumber)
            case 3:
                movie3seats.remove(newseatnumber)
        match(info['Movie Number']):
            case 1:
                movie1seats.append(info['Seat Number'])
                movie1seats.sort()
            case 2:
                movie2seats.append(info['Seat Number'])
                movie2seats.sort()
            case 3:
                movie3seats.append(info['Seat Number'])
                movie3seats.sort()

        orders[tid]['Movie Number'] = 1
        orders[tid]['Seat Number'] = newseatnumber
        orders[tid]['Time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("Order Successfully Updated")
        time.sleep(3)
        os.system('cls')
    else:
        print("Please Enter Valid Inputs")
                


def update_order_panel():
    while True:
        os.system('cls')
        print("Orders: ")
        for tid, info in orders.items():
            print(f"Order ID: {tid}, Movie Number: {info['Movie Number']}, Seat Number: {info['Seat Number']}, Price: {info['Price']}, Order Date: {info['Time']}")
        update_choice = tryparse(input("Enter the Order ID: "))
        if update_choice in ids:
            update_order(update_choice)
            break
        else:
            os.system('cls')
            print("Invalid Choice.")
            time.sleep(3)

def tryparse(value):
    try:
        return int(value)
    except ValueError:
        return None

movie1seats = list(range(1,51))
movie2seats = list(range(1,51))
movie3seats = list(range(1,51))
ids = []
orders = {}

while True:
    print("Welcome to Movie Ticket Reservation\n1. Order Ticket\n2. Update Order")
    main_choice = tryparse(input("What would you like to do? "))
    match(main_choice):
        case 0:
            break
        case 1:
            book_order()
        case 2:
            update_order_panel()
        case _:
            print("Invalid Choice.")
            time.sleep(3)
            continue
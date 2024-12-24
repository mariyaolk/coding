def greet_guests(guest_list):
    for guest in guest_list:
        print(f"Привет, {guest}!")

guests = ["Анна", "Иван", "Ольга", "Сергей"]
greet_guests(guests)
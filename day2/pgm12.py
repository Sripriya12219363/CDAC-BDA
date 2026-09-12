def main():
    date = input("Enter date: ")
    parts = date.split("/")

    months = (
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    )

    if len(parts) != 3:
        print("Invalid Date")
        return

    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
    except ValueError:
        print("Invalid Date")
        return

    if month < 1 or month > 12:
        print("Invalid Date")
        return

    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_day = 29
        else:
            max_day = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_day = 30
    else:
        max_day = 31

    if day < 1 or day > max_day:
        print("Invalid Date")
    else:
        print(f"{months[month - 1]} {day:02d}, {year}")


main()


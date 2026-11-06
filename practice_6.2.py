numbers = [5000, 75000, 25000, 12000]

if not numbers:
    print("List is empty")
else:
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    print(largest)
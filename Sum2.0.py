def main():

    counter = 0
    sum = 0
    amount = 0
    number = ""
    sum_equation = ""
    try:
        amount = int(input("How many numbers would you like to add: "))
        while counter < amount:
            try:
                number = int(input("What number would you like to add: "))
                if number <= 0:
                    continue
                sum_equation = sum_equation + str(number) + " + "
                print(" {} is added to the sum".format(number))
                counter = counter + 1
                sum = sum + number

            except ValueError:
                print("Invalid input. Please enter a whole number")
        print("{} = {}".format(sum_equation, sum))
    except ValueError:
        print("Please enter a whole number ")


if __name__ == "__main__":
    main()

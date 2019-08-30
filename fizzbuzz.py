# If number is divisible by 3: print "Fizz", if number is divisible by 5: print "Buzz", if divisible by both:
# print "FIZZBUZZ"

number_list = [4, 0, 3, 7, 5, 8, 15]

for number in range(1, 500):
    # if number == 0:
    #     print(number)
    if number != 0 and number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz!")
    elif number != 0 and number % 3 == 0:
        print("Fizz")
    elif number != 0 and number % 5 == 0:
        print("Buzz")
    else:
        print(number)

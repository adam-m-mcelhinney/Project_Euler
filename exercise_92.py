# A number chain is created by continuously adding the square of the digits in a number to form a new number
# until it has been seen before.
#
# For example,
#
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that
# EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?


def square_digit(input):
    if input == 1:
        return 0
    elif input == 89:
        return 1
    else:
        input_str = str(input)
        result = 0
        for i, val in enumerate(input_str):
            result +=int(val)**2
        #print(result)
        return square_digit(result)


input = 44
square_digit(input)
square_digit(85)

result = 0
for i in range(1, 10**7):
#for i in range(1, 10**7):
    try:
        result += square_digit(i)
    except:
        print(i)
        #sys.exit()

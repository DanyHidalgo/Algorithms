'''
Print and calculate the sum of the first n numbers
'''


def sum_of_first_n_numbers():


    n = int(input("Input an n number: "))
    print("n:", n)

    sum = 0

    for num in range(n + 1):

        sum += num

    print("Sum:", sum)


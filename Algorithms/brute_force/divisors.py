'''
Find all the divisors of n
'''

def divisors(n_param):

    n = n_param

    divisors_list = []


    for num in range(1, n + 1):

        if n % num == 0:

            divisors_list.append(num)

        else:
            pass
    

    return divisors_list

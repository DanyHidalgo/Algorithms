'''
Testing of all of the algorithms
'''
from brute_force import divisors, pin_unlock, sum_of_first_n_numbers
from lists import largest_num_list, merge_list
from recursion import countdown, n_factorial, nth_fibonacci_num, sum_of_n_recursive
from searching import binary_search, Linear_Search
from sorting import bubble_sort, bubble_sort_opt, insertion_sort, selection_sort

#Brute Force
n = 10 # Number divisors
print(divisors.divisors(n))

n = '0002' # Pin with 4 digits 
print(pin_unlock.unlock(n))

sum_of_first_n_numbers.sum_of_first_n_numbers()

#Lists
largest_num_list.largest_num_list([0,2,5,8,11,47,1,6]) # Largest number in list

merge_list.merge_list([1,4,8],[3,5,6]) # 2 Oredered lists into one ordered list

#Recursion
n = 5 # Countdown number
print(countdown.inf(n))

n = 5 # Factorial of an n number
print(n_factorial.fact(n))

n = 6 # Nth number of the Fibonacci sequence
print(nth_fibonacci_num.fib(n))

n = 5 # Sum of n
print(sum_of_n_recursive.sum_of_n(n))

#Searching
a = a = [] # List to search de element
for i in range (1, 101):
    a.append(i) 
n = len(a) # Parameter
d = 89 # Searched item
print(binary_search.binary_search(a,n,d))

print(Linear_Search.Search(a,d))

#Sorting
a = a = [] # List to search de element
for i in range (1, 101):
    a.append(i) 
print(bubble_sort.bubble_sort(a))

print(bubble_sort_opt.bubble_sort_opt(a))

print(insertion_sort.insertion_sort(a))

print(selection_sort.selection_sort(a))
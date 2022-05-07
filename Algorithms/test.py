'''
Testing of all of the algorithms
'''
from brute_force import divisors, pin_unlock, sum_of_first_n_numbers
from lists import largest_num_list, merge_list
from recursion import countdown, n_factorial, nth_fibonacci_num, sum_of_n_recursive
from searching import binary_search, Linear_Search
from sorting import bubble_sort, bubble_sort_opt, insertion_sort, selection_sort

#Brute Force
print('---Divisors---')
n = 10
print(divisors.divisors(n))

print('---Pin Unlock---')
n = '0002' # Pin with 4 digits 
print(pin_unlock.unlock(n))

print('---Sum of the First N Numbers---')
sum_of_first_n_numbers.sum_of_first_n_numbers()

#Lists
print('---Largest Number in the List---')
largest_num_list.largest_num_list([0,2,5,8,11,47,1,6])

print('---Merge List---')
merge_list.merge_list([1,4,8],[3,5,6]) # 2 Oredered lists into one ordered list

#Recursion
print('---Countdown---')
n = 5 # Countdown number
print(countdown.inf(n))

print('---Factorial of an n Number---')
n = 5
print(n_factorial.fact(n))

print('---Nth Number ofthe Fibonacci Sequence---')
n = 6
print(nth_fibonacci_num.fib(n))

print('---Sum of N Recursive---')
n = 5 
print(sum_of_n_recursive.sum_of_n(n))

#Searching
a = a = [] # List to search de element
for i in range (1, 101):
    a.append(i) 
n = len(a) # Parameter
d = 89 # Searched item
print('---Binary Search---')
print(binary_search.binary_search(a,n,d))

print('---Linear Search---')
print(Linear_Search.Search(a,d))

#Sorting
a = a = [] # List to search de element
for i in range (1, 101):
    a.append(i) 
print('---Bubble Sort---')
print(bubble_sort.bubble_sort(a))

print('---Bubble Sort Optimized---')
print(bubble_sort_opt.bubble_sort_opt(a))

print('---Insertion Sort---')
print(insertion_sort.insertion_sort(a))

print('---Selection Sort---')
print(selection_sort.selection_sort(a))
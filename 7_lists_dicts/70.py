# To generate random numbers
from random import randint
# Used to time performance of function execution
import time

'''
70. Écrire une boucle qui trie une liste sans utiliser la méthode .sort(). 
my_list = [4, 2, 9, 12, 32, 13, 8, 78, 14, 21, 7, 1, 3, 5, 6]

Went a tiny bit further than asked xD
'''
# O(1) constant - runtime is constant regardless of the size of the input. Finding an element in a hash table is an example of an operation that can be performed in constant time.
# O(n) - linear - runtime grows linearly with the size of the input. A function that checks a condition on every item of a list is an example of an O(n) algorithm.
# O(n^2): quadratic - runtime is a quadratic function of the size of the input. A naive implementation of finding duplicate values in a list, in which each item has to be checked twice, is an example of a quadratic algorithm.
# O(2n): exponential	- runtime grows exponentially with the size of the input. These algorithms are considered extremely inefficient. An example of an exponential algorithm is the three-coloring problem.
# O(log n): logarithmic	- runtime grows linearly while the size of the input grows exponentially. For example, if it takes one second to process one thousand elements, then it will take two seconds to process ten thousand, three seconds to process one hundred thousand, and so on. Binary search is an example of a logarithmic runtime algorithm.

def time_it(function):
    """ Simple timing decorator to measure function execution performance
    Using timeit module to lower noise and get an average
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time for {function.__name__} : {elapsed_time} secondes")
        return result
    return wrapper

@time_it
def bubble_sort(lst: list) -> list:
    ''' O(n^2) time complexity, O(1) space complexity
    Pretty trash but simple and works for trivial data sets
    '''
    length = len(lst)
    for index in range(length):
        checks = length - index - 1
        for j in range(checks):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# @time_it
# not timing with our generator because it's a recursive call, so it will time each function call. Cba figuring it out
def quick_sort(lst: list) -> list:
    ''' O(log n) time complexity, O(n^2) worst case
    Most classic sorting algo, very good if worst case perf doesn't matter too much
    '''
    # If only 1 elem in lst, means we're done, so return the result
    if len(lst) < 1:
        return lst

    # Always choose middle index as pivot, could also select randomly
    pivot = lst[len(lst) // 2]
    greater = []
    lesser = []
    equal = []

    for elem in lst:
        # all elemens smaller than pivot go into the lesser (left) list
        if elem < pivot:
            lesser.append(elem)
        # all elemens greater than pivot go into the greater (right) list
        elif elem > pivot:
            greater.append(elem)
        # rest is equal
        else:
            equal.append(elem)
    # Concatenate the 3 lists in the the proper order, and recursively call the function
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    ARRAY_LEN = 100
    # Gen array of `ARRAY_LEN` size filled with random ints between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LEN)]
    print(bubble_sort(array))
    array = [randint(0, 1000) for i in range(ARRAY_LEN)]
    print(quick_sort(array))
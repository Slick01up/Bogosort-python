# Bogosort Algorithm Implementation in Python

## Introduction
This Python script demonstrates the Bogosort algorithm, a highly inefficient sorting algorithm with a worst-case time complexity of O((n+1)!), where n is the number of elements in the list to be sorted. The algorithm works by randomly shuffling the elements of the list until they are sorted. While conceptually simple, Bogosort is practically useless for sorting anything but very small lists due to its inefficiency.

## Usage
To use this script, simply run it using a Python interpreter. The script will repeatedly shuffle a list of numbers until they are sorted, using the Bogosort algorithm. The number of attempts required to sort the list is then recorded, and after a specified number of iterations (in this case, 100), the average number of attempts is calculated and displayed.

## Code Structure
- The original list to be sorted is defined as `original_list`.
- The `test` function takes the original and shuffled lists as input and repeatedly shuffles the shuffled list until it matches the original list, counting the number of attempts required.
- The main loop iterates 100 times, shuffling the list and calling the `test` function to determine the number of attempts required to sort it each time.
- The results are stored in a list called `attempts_list`, and the average number of attempts is calculated and displayed at the end.

## Limitations
Bogosort is highly inefficient and should not be used in any practical application where performance matters. It is primarily used for educational purposes or as a joke due to its absurdly poor performance on large datasets.

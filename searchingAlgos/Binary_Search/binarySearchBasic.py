'''
Author: c17hawke
Name: Sunny Bhaveen Chandra
Date: November 19, 2019
Time: 01:08 hrs IST
Aim:-
	to impliment binary search algo using simple functional method
'''	

import numpy as np

def binary_search(my_list, element):
	'''
	this is binary search algo for sorted list
	'''
	low = 0
	high = len(my_list) - 1

	while low<=high:
		mid = (low + high)//2
		guess = my_list[mid]
		if guess == element:
			return mid
		if guess > element:
			high = mid -1 
		else:
			low = mid + 1
	return None

def main():
	# giving a sorted but random list 
	my_random_list = sorted(list(np.random.randint(1,100, 11)))

	print(my_random_list)
	print()

	# search for the desired element
 	element = int(input("search for = "))

 	# get the results-
 	result_idx = binary_search(my_random_list, element)
	print("element found and its located at index #{}".format(result_idx) if result_idx \
		else "Element not found")

if __name__ == '__main__':
	main()
'''
Author: c17hawke
Name: Sunny Bhaveen Chandra
Date: November 19, 2019
Time: 03:04 hrs IST
Aim:-
	to impliment binary search algo using recursion
'''

import numpy as np

def recursive_binary_search(my_list, element, low, high):
	'''
	this is binary search algo for sorted list
	'''
	# termination case when element was not found
	if low > high:
		return None
	else:
		#calculating mid value
		mid = (low + high)//2
		if element == my_list[mid]:
			return mid
		elif element > my_list[mid]:
			return recursive_binary_search(my_list, element, mid + 1, high)
		else:
			return recursive_binary_search(my_list, element, low, mid - 1)



def main():
	# giving a sorted but random list 
	my_random_list = sorted(list(np.random.randint(1,100, 11)))

	print(my_random_list)
	print()

	# search for the desired element
	element = int(input("search for = "))

	low = 0
	high = len(my_random_list) - 1

	# get the results-
	result_idx = recursive_binary_search(my_random_list, element, low, high)
	print("element found and its located at index #{}".format(result_idx) if result_idx >= 0 \
		else "Element not found")

if __name__ == '__main__':
	main()
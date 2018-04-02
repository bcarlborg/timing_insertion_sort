from random import *

def beaus_insertion_sort(input_list):
	"""recursively constructs sorted lists using the insertion sort algorithm"""

	list_length = len( input_list )

	# Base Case
	if ( list_length == 1 ):
		return input_list

	# Recursive case
	else:
		# passing sub list to sorting algorithm
		item_to_insert = input_list.pop()
		sorted_sub_list = beaus_insertion_sort( input_list )
		sorted_sub_list.append( item_to_insert )

		# index value to be inserted and values to be compared with
		index_of_item_to_insert = list_length - 1
		index_of_comparison_item = index_of_item_to_insert - 1

		# insert item until it is larger than the value it is being compared to.
		while ( ( sorted_sub_list[ index_of_item_to_insert ] < sorted_sub_list[ index_of_comparison_item ] ) and ( index_of_comparison_item >= 0 ) ):
			temp = sorted_sub_list[ index_of_comparison_item ]
			sorted_sub_list[ index_of_comparison_item ] = sorted_sub_list[ index_of_item_to_insert ]
			sorted_sub_list[ index_of_item_to_insert ] = temp

			index_of_item_to_insert -= 1
			index_of_comparison_item -= 1
		return sorted_sub_list

def worst_case_input_generator( number_of_inputs ):
	"""Creates decending sorted list"""
	output_list = list( range( number_of_inputs ) )
	output_list.sort( reverse=True )
	return output_list

def best_case_input_generator( number_of_inputs ):
	"""Creates a list that has already been sorted in ascending order"""
	output_list = list( range( number_of_inputs ) )
	return output_list

def random_input_generator( number_of_inputs ):
	"""Creates a list of random inputs of the length specified to the function"""
	output_list = []
	for x in range( number_of_inputs ):
		output_list.append( randint( 1, number_of_inputs ) )
	return output_list



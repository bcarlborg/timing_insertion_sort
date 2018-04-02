from random import *

def beaus_insertion_sort(input_list):
	list_length = len( input_list )

	if ( list_length == 1 ):
		return input_list

	else:
		item_to_insert = input_list.pop()
		sorted_sub_list = beaus_insertion_sort( input_list )
		sorted_sub_list.append( item_to_insert )

		index_of_item_to_insert = list_length - 1
		index_of_comparison_item = index_of_item_to_insert - 1

		while ( ( sorted_sub_list[ index_of_item_to_insert ] < sorted_sub_list[ index_of_comparison_item ] ) and ( index_of_comparison_item >= 0 ) ):
			temp = sorted_sub_list[ index_of_comparison_item ]
			sorted_sub_list[ index_of_comparison_item ] = sorted_sub_list[ index_of_item_to_insert ]
			sorted_sub_list[ index_of_item_to_insert ] = temp

			index_of_item_to_insert -= 1
			index_of_comparison_item -= 1
		return sorted_sub_list

def worst_case_input_generator( number_of_inputs ):
	output_list = list( range( number_of_inputs ) )
	output_list.sort( reverse=True )
	return output_list

def best_case_input_generator( number_of_inputs ):
	output_list = list( range( number_of_inputs ) )
	return output_list

def random_input_generator( number_of_inputs ):
	output_list = []
	for x in range( number_of_inputs ):
		output_list.append( randint( 1, number_of_inputs ) )
	return output_list



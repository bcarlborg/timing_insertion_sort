def return_list( N ):
	my_list=list(range(12))
	new_list = my_list[:]
	return new_list 

print(return_list(10))


def insertion_sort(input_list, element_to_add):
	current_element_index = len(input_list) - 1
	while element_to_add < input_list[current_element_index]:
		current_element_index = current_element_index - 1
	input_list.insert(current_element_index, element_to_add)
	return input_list

print('function input list', insertion_sort([1,3,4,10], 7))



def worst_case_input_generator( input_size ):
	pass

def best_case_input_generator( input_size ):
	pass

def random_input_generator( input_size ):
	pass



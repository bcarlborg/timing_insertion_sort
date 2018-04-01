def list_generator():
	output_list = [1,2,3,4,5]
	output_list[1:4] = ['b','c','d']
	print("expecting output to be [1,b,c,d,5]")
	print(output_list)

def insertion_sort(input_list):
	"""Sort the input_list using insetion sort"""
	s = input_list
	print(s)

list_generator()

import unittest
import insertion_sort as insertion_sort

class InsertionSortTestCase(unittest.TestCase):
	"""Tests for insertion_sort.py"""

	def test_sorting_list_of_one_element(self):
		"""does insertion sort return same list for [4]"""
		self.assertEqual( [ 4 ], insertion_sort.beaus_insertion_sort( [ 4 ] ) )

	def test_sorting_random_list(self):
		"""does the algorithm correctly sort a random list"""
		self.assertEqual( [ 1, 2, 3, 4 ], insertion_sort.beaus_insertion_sort( [ 4, 3, 2, 1  ] ) )

	def test_sorting_list_with_copies_of_same_number( self ):
		"""will insertion sort work with multiple of the same number in the ist"""
		self.assertEqual( [ 1, 2, 2, 2, 5], insertion_sort.beaus_insertion_sort( [ 2, 5, 2, 1, 2 ] ) )

	def test_worst_case_input_generator(self):
		"""does the worst case generator make correct lists"""
		self.assertEqual( [ 5, 4, 3, 2, 1, 0 ], insertion_sort.worst_case_input_generator( 6 ) )

	def test_best_case_input_generator(self):
		"""does the best case generator make correct lists"""
		self.assertEqual( [ 0, 1, 2, 3, 4, 5 ], insertion_sort.best_case_input_generator( 6 ) )

	def test_random_case_input_generator(self):
		"""does the random input generator produce lists of correct length"""
		self.assertEqual( 6, len(insertion_sort.random_input_generator( 6 ) ) )

if __name__ == '__main__':
	unittest.main()


import matplotlib.pyplot as plt
import insertion_sort as insertion_sort 
import time

ns     = []
random_times  = []
best_times = []
worst_times = []
timesr = []
min_i  = 2
max_i  = 27 
n_base = 1.3 

for i in range( min_i, max_i ):
    n = int( n_base ** i )

    # generate an input to the algorithm under test
    input_list = insertion_sort.random_input_generator( n )
    time_1_random = time.time()
    insertion_sort.beaus_insertion_sort( input_list )
    time_2_random = time.time()
    time_difference_random = time_2_random - time_1_random

    input_list = insertion_sort.best_case_input_generator( n )
    time_1_best_case = time.time()
    insertion_sort.beaus_insertion_sort( input_list )
    time_2_best_case = time.time()
    time_difference_best_case = time_2_best_case - time_1_best_case

    input_list = insertion_sort.worst_case_input_generator( n )
    time_1_worst_case = time.time()
    insertion_sort.beaus_insertion_sort( input_list )
    time_2_worst_case = time.time()
    time_difference_worst_case = time_2_worst_case - time_1_worst_case

    ns.append( n )
    random_times.append( time_difference_random )
    best_times.append( time_difference_best_case )
    worst_times.append ( time_difference_worst_case )

plt.plot( ns, random_times, "blue")
plt.plot( ns, best_times, "green")
plt.plot( ns, worst_times, "red" )

plt.xlabel('input size')
plt.ylabel('time (s)')
plt.title('Algorithm Timing is Fun')
plt.grid(True)
# plt.savefig("test.png")
plt.show()

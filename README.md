The goal of this assignment is to observe theoretical performance scaling of a simple algorithm in the wild. The algorithm you'll be working with is insertion sort. Your tasks:

Write an implementation of insertion sort
Write three input generators. Each of these should be a function/method that takes in a number and outputs a list/array that can be passed to insertion sort as input. The size of the output should be proportional to the value of the input number provided. The generators should be:
One that generates the worst possible kind of input to insertion sort. For these inputs, insertion sort should scale quadratically with the size of the input.
One that generates the best possible kind of input to insertion sort. For these inputs, insertion sort should scale linearly with the size of the input.
One that generates "random" inputs. It's your job to decide how exactly the input are randomized.
Run your insertion sort on a range of input sizes, for each input generator. Remember, it is very important that the run time of the invocations of insertion sort be macroscopic (at least many milliseconds); otherwise, random system noise will likely make it impossible to get meaningful results.
Graph your results. It is up to you to decide how best to represent your results as graphs. For example, does it make sense to put results from different input generators on the same plot, or not?
Write a very short text document describing your results. In particular:
Were you able to get quadratic and linear scaling with different input generators? What is it about those inputs that causes the scaling to be what it is?
For the random input, was the scaling closer to linear, closer to quadratic, or something else entirely?
You should upload:

Your code for insertion sort and running the timing experiments. I recommend using Python, but you're welcome to use another language if you want.
The graph(s) your code produces
Your short text document.
The final deadline for this assignment is Monday morning. If you think you will have a problem with this deadline, talk to Ben.

Scoring rubric:

30 - Correct insertion sort implementation
30 - Input generators
20 - Testing and graph generation
10 - Text document
10 - Code style sanity
Example code that you can pattern yours after:

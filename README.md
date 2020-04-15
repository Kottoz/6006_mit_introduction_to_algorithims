## mit_introduction_to_algorithims_6.006
This is my work through 6.006 course, introduction to algorithms.
[Course website](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/)
### why do we use ![equation](https://latex.codecogs.com/gif.latex?\fn_phv&space;\log_{2}{n})  in algorithims analysis ?
 You might expect that this is because computers represent numbers in binary, but usually that is not why, 
 ![equation](https://latex.codecogs.com/gif.latex?\fn_phv&space;\log_{2}{n})  is (with suitable rounding)   the number of times you can divide n by 2 before reaching 1

## Notes
#### [1] Algorithim analysis
- We want to predict how the algorithm will behave (e.g. running time) on arbitrary inputs **(Asymptotic)**, and how it will compare to other algorithms
- we look at the running time of an algorithm when the input size n is large enough so that constants and lower-order terms do not matter. This is called `aymptotic analysis of algorithms` .
- **rate of growth of a function** `(O-notation, Ω-notation, Θ-notation)`, 
- Assume we have two functions f, g : N −→ R that represent running times. Comparing f and g in terms of their growth can be summarized as: 
    - f is below g ⇔ f ∈ O(g) ⇔ f ≤ g
    - f is above g ⇔ f ∈ Ω(g) ⇔ f ≥ g
    - f is both above and below g ⇔ f ∈ Θ(g) ⇔ f = g 
    - **NB** `⇔ means if and only if` 
- **Growth rate of standard functions**
- Polynomial of degree d is defined as: 
    - ![equation](https://latex.codecogs.com/gif.latex?P(n)&space;=\sum_{i-1}^{d}&space;a_{i}n^{i}&space;=&space;\Theta&space;(n^{d}))


#### [4] Divide and conquer
- **Divide** the problem into a number of subproblems that are smaller instances of the same problem.
- **Conquer** the subproblems by solving them recursively. If the subproblem sizes are small enough which reaching the (**Base case**), just solve the subproblems in a straightforward manner `algorithm is solved in the most straightforward manner, without takingadvantage of any ideas that can make thealgorithm more efficient`.
- Ex:. **Merge sort**
    - Divide: Divide an array of n elements into two arrays of n/2 elements each.
    - Conquer: Sort the two arrays recursively.
    - Combine: Merge the two sorted arrays.

- **Combine** the solutions to the subproblems into the solution for the original problem. 
    #### [4.3] The substitution method
    1. Guesstheformofthesolution.
    2. Use mathematical induction to find the constants and show that the solution works.
    We can use the substitution method to establish either upper or lower bounds on a recurrence.

## My solutions to CLRS
#### [4] Divide and conquer

**Tools**
- [Function simulator tool](https://www.desmos.com/calculator/auubsajefh).
- [Latex editor](https://www.codecogs.com/latex/eqneditor.php).
- [Python visualize](http://www.pythontutor.com/visualize.html#mode=edit)
- [Python Cost Model](http://scripts.mit.edu/~6.006/fall08/wiki/index.php?title=Python_Cost_Model#Cost_of_Python_String_Operations)

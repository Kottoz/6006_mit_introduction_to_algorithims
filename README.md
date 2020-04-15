## mit_introduction_to_algorithims_6.006
This is my work through 6.006 course, introduction to algorithms.
[Course website](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/)
### why do we use ![equation](https://latex.codecogs.com/gif.latex?\fn_phv&space;\log_{2}{n})  in algorithims analysis ?
 You might expect that this is because computers represent numbers in binary, but usually that is not why, 
 ![equation](https://latex.codecogs.com/gif.latex?\fn_phv&space;\log_{2}{n})  is (with suitable rounding)   the number of times you can divide n by 2 before reaching 1

## Notes
#### [4] Divide and conquer
- **Divide** the problem into a number of subproblems that are smaller instances of the same problem.
- **Conquer** the subproblems by solving them recursively. If the subproblem sizes are small enough which reaching the (**Base case**), just solve the subproblems in a straightforward manner `algorithm is solved in the most straightforward manner, without takingadvantage of any ideas that can make thealgorithm more efficient`.
- **Combine** the solutions to the subproblems into the solution for the original problem. 
## My solutions to CLRS
#### [4] Divide and conquer

**Tools**
- [Function simulator tool](https://www.desmos.com/calculator/auubsajefh).
- [Latex editor](https://www.codecogs.com/latex/eqneditor.php).
- [Python visualize](http://www.pythontutor.com/visualize.html#mode=edit)
- [Python Cost Model](http://scripts.mit.edu/~6.006/fall08/wiki/index.php?title=Python_Cost_Model#Cost_of_Python_String_Operations)

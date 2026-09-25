# Unit 7 Discussion: Sorting Algorithms

## Overview

I implemented Bubble Sort and Merge Sort in `unit7_discussion.py`. Both functions returned new sorted lists, leaving the inputs unchanged. I ran the file with `python unit7_discussion.py` and compared each result to Python's `sorted()` as a check.

## What I tested

I sorted seven product prices and eight streaming popularity scores with both algorithms. I also tested an empty list, an already sorted list, a reverse-sorted list, duplicates, and a single-element list. Both algorithms produced the expected ascending order for every example. The empty and single-element inputs worked without errors. Bubble Sort stopped early on the sorted list after finding no swaps in a pass.

## Reflection

I learned how two algorithms could produce identical results while doing very different amounts of work. For Bubble Sort, I compared neighboring values and swapped them when the left value was larger. The inner loop shortened after each pass because the largest remaining value had reached the end. The nested loops still made its average and worst-case running time O(n²), although the no-swap check let it finish an already sorted list in O(n).

Merge Sort was more challenging because I had to track two positions while combining sorted halves. I used a small list to follow the recursive calls, then checked what happened when one half ran out first. Appending the remaining items solved that case. Merge Sort split the input and merged the pieces in O(n log n) time, which made it a better fit for a large streaming recommendation list. It needed O(n) additional space, whereas Bubble Sort used a small amount of working space after making its required copy. Both versions kept equal items in their original relative order: Bubble Sort swapped only when the left value was greater, and Merge Sort chose the left value first on a tie. I would use Bubble Sort to demonstrate the mechanics on a tiny list and Merge Sort when stable ordering and reliable performance mattered for large lists.

## Real-world use

A streaming platform could use stable Merge Sort to order a large list by rating while retaining the original order of shows with equal ratings. The sample code uses integer popularity scores to demonstrate the ordering; checking stability across distinct shows would require records with both a rating and an identity.

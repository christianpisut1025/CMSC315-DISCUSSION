# Unit 5 Discussion Search Algorithms

## Overview

This assignment compared linear search and binary search using small and large sorted datasets. The program also tested empty input, single-element input, missing values, and values at the first and last positions.

## Implementation

I implemented linear search by examining values sequentially and returning the matching index or `-1`. I implemented binary search with low, high, and middle indexes. Each unsuccessful comparison removed half of the remaining sorted search space. I also added explanatory output and elapsed-time measurements for a dataset containing 1,000,000 integers.

## Discussion Board Reflection

While completing this assignment, I learned how linear and binary search solve the same problem through different strategies. Linear search examined each value in sequence, giving it O(n) time complexity in the worst case. Binary search repeatedly removed half of a sorted search space, giving it O(log n) time complexity. Testing one million integers made the performance difference easier to observe.

The most challenging part was handling binary-search boundaries correctly. I had to update the low and high indexes without skipping a possible match or creating an endless loop. I addressed this by testing an empty list, a single-element list, missing values, and targets at both boundaries. Those tests confirmed that both methods returned either the correct index or `-1`.

I found that binary search was the better option for a large collection that was already sorted and searched frequently. Linear search remained appropriate for small or unsorted collections because it required no sorting preparation. In a real inventory system, sorting could add unnecessary work when records changed constantly. However, a large, stable product index could justify sorting once so repeated binary searches would be much faster.

## Running the Program

```bash
python unit5_discussion.py
```

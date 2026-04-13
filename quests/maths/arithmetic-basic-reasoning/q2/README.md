# Find the Pivot Integer

## Problem
Given a positive integer `n`, find an integer `x` such that:

- Sum of all integers from `1` to `x` (inclusive)
- Equals the sum of all integers from `x` to `n` (inclusive)

Return `x` if it exists, otherwise return `-1`.

It is guaranteed there is **at most one** such pivot.

---

## Examples

### Example 1
Input: `n = 8`  
Output: `6`  
Explanation:  
`1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21`

### Example 2
Input: `n = 1`  
Output: `1`  
Explanation:  
`1 = 1`

### Example 3
Input: `n = 4`  
Output: `-1`  
Explanation:  
No such integer exists.

---

## Constraints
- `1 <= n <= 1000`

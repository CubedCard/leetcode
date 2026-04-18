# 3783. Mirror Distance of an Integer

## Problem
You are given an integer `n`.

Define its **mirror distance** as:
`abs(n - reverse(n))`

where `reverse(n)` is the integer formed by reversing the digits of `n`.

Return the mirror distance of `n`.

---

## Examples

### Example 1
**Input:** `n = 25`  
**Output:** `27`  
**Explanation:** `reverse(25) = 52`, so `abs(25 - 52) = 27`.

### Example 2
**Input:** `n = 10`  
**Output:** `9`  
**Explanation:** `reverse(10) = 1`, so `abs(10 - 1) = 9`.

### Example 3
**Input:** `n = 7`  
**Output:** `0`  
**Explanation:** `reverse(7) = 7`, so `abs(7 - 7) = 0`.

---

## Constraints
- `1 <= n <= 10^9`

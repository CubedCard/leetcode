# Q3. Not Boring Movies

Table: Cinema

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| movie       | varchar |
| description | varchar |
| rating      | float   |

- `id` is the primary key.
- Each row contains a movie’s name, description, and rating.
- `rating` is a float in the range [0, 10].

## Problem
Report movies that:
- Have an **odd-numbered ID**
- Have a description **not equal to "boring"**

Return the result ordered by **rating (descending)**.

## Example

### Input

| id | movie      | description | rating |
|----|------------|-------------|--------|
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |

### Output

| id | movie      | description | rating |
|----|------------|-------------|--------|
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |

### Explanation
- Odd IDs: 1, 3, 5  
- Exclude ID 3 because description is "boring"  
- Sort remaining by rating (descending)

## Q4. Find Customer Referee

### Table: Customer

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| referee_id  | int     |

- `id` is the primary key.
- Each row contains a customer, their name, and the id of the customer who referred them.

---

### Problem

Find the names of customers who are either:
- **not referred by customer with id = 2**, or
- **not referred by anyone (NULL referee_id)**

Return the result table in any order.

---

### Example

**Input:**

Customer table:

| id | name | referee_id |
|----|------|------------|
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |

**Output:**

| name |
|------|
| Will |
| Jane |
| Bill |
| Zack |

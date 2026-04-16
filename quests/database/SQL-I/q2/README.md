## Q2. Employees Earning More Than Their Managers

### Table: Employee

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |

- `id` is the primary key.
- Each row represents an employee, including their salary and manager's ID.

### Problem

Find employees who earn more than their managers.

Return the result in any order.

### Example

**Input**

| id | name  | salary | managerId |
|----|-------|--------|-----------|
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |

**Output**

| Employee |
|----------|
| Joe      |

**Explanation**

Joe earns more than his manager.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT MAX(salary)
      FROM (
          SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
          FROM Employee
      ) as sub
      WHERE rnk = N
  );
END

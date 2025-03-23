# Introduction to Diophantine Equations

## What is a Diophantine Equation?
A **Diophantine equation** is a polynomial equation where integer solutions are sought. These equations are named after the ancient Greek mathematician **Diophantus**.

## Linear Diophantine Equations in Two Variables
A **linear Diophantine equation** in two variables takes the form:
$$ax + by = c$$
where:
- $a, b, c$ are given integers,
- $(x, y)$ are integer variables to be solved for.

For integer solutions to exist, a necessary and sufficient condition is:
$$\gcd(a, b) \mid c$$
That is, the greatest common divisor (GCD) of $\( a \)$ and $\( b \)$ must divide $\( c \)$.

# Function Documentation

## gcd(a, b)<br>
Computes the greatest common divisor (GCD) of two integers using **Euclidean Algorithm**.
Given two integers \( a \) and \( b \), their GCD is the largest integer \( d \) such that:
$$d \mid a \quad \text{and} \quad d \mid b$$

### Example:
```python
gcd(48, 18) # Output: 6
```

## gcd_mult(*args)<br>
Finds the GCD of multiple integers by applying the **pairwise Euclidean algorithm** iteratively.

### Example:
```python
gcd_mult(48, 18, 30) # Output: 6
```

## is_integral_sol_exist(a, b, c)<br>
Checks if the given linear Diophantine equation $\( ax + by = c \)$ has integer solutions.

### Example:
```python
is_integral_sol_exist(5, 7, 144) # Output: True
```

## get_bezout(a, b, d)<br>
Finds **Bézout coefficients** \( s \) and \( t \) such that:
$$a \cdot s + b \cdot t = d$$
where $d = \gcd(a, b)$.

### Example:
```python
get_bezout(7, 5, 1) # Output: (−2, 3) because 7(-2) + 5(3) = 1
```

## particular_solution(a, b, c)<br>
Finds one particular integer solution  $(x_0, y_0)$ to $ax + by = c$. The solution are 

$$x_0 = s\cdot\frac{c}{d}, \quad y_0 = t\cdot\frac{c}{d}$$

### Example:
```python
particular_solution(7, 5, 144) # Output: (26, 2)
```

## general_solution(a, b, c)<br>
Finds the general solution:
$$x = x_0 + \frac{b}{d}t, \quad y = y_0 - \frac{a}{d}t$$
where $d = \gcd(a, b)$ and $t$ is an arbitrary integer.

### Example:
```python
general_solution(7, 5, 144) # Output: [(26, -5), (2, 7)]
```

## get_natural_solutions(a, b, c, x_gen, y_gen)<br>
Finds all natural number solutions $(x, y)$ where $( x, y) \in \mathbb{N}^2$ or $( x, y > 0 \)$

### Example:
```python
get_natural_solutions(5, 7, 144, (26, -5), (2, 7))
# Output: [(26, 2), (31, 1), (36, 5), ...]
```


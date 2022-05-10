# Exercise 1

```py
print('Exercise 1')
```

---

# Exercise 2

* `+`, `-` are addition and subtraction,
* `*`, `/` are multiplication and division,
* `**` is exponentiation (e.g. `2 ** 3` returns $2^3$),
* `//` is integer division,
* `%` is modulus, e.g. `38 % 5` returns the remainder of `38 // 5`.

---

### Question 3

```py
my_string = 'Some text characters of my choice.'
m = 7

# Find out how many times we can print the mth character
# before exceeding the string length
N = len(my_string)
print(N // m)

print(my_string[m - 1])
print(my_string[2 * m - 1])
print(my_string[3 * m - 1])
print(my_string[4 * m - 1])
```

---

##prob4

```py
x = 1.110223024625156e-16

print(x == 0)
print(x + 1 == 1)
```

The value given is (just under) half of what we call $\epsilon$, or **machine epsilon** --
the distance between 1 and the next closest number in double-precision floating-point representation
(i.e. using the `float` type).

This means that any real number $a \in [1, 1+\frac{\epsilon}{2})$ has the same floating-point
representation as $1$ -- it effectively gets rounded down to 1. Similarly, any real number
$b \in [1 + \frac{\epsilon}{2}, 1 + \epsilon]$ has the same representation as $1 + \epsilon$,
because it is rounded up. Now, working in finite precision means that we can actually find
*the* largest floating-point number `x`$>0$ such that `x`$<\frac{\epsilon}{2}$ -- this is the
value given here.

For a simpler example, if we worked with a system which could only represent numbers up to
3 significant digits:
* We could represent the number $1$ and the number $1.01$, but every real number in between
would get rounded to the closest of these values.
* This means that, for this system, $\epsilon=0.01$.
* The largest number `x`$>0$ representable in this system such that `x`$<\frac{\epsilon}{2}=0.005$
is `x = 0.00499`, since we can store at most 3 significant digits.

Note that, in this system, there is no difference between the value of `1 + 0.001`, `1 + 0.00136`,
`1 + 0.00487`, etc. -- they all evaluate to `1`. We say that [floating-point addition leads to
**round-off error**](https://en.wikipedia.org/wiki/Round-off_error#Addition).

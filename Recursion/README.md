# Recursion in Programming

## Overview

Recursion is a powerful programming technique where a function calls itself to solve smaller instances of a problem. It is often used in algorithms that involve repetitive or nested structures, such as tree traversal, sorting algorithms, and more.

This repository aims to provide a comprehensive guide to understanding and implementing recursion in various programming languages. It includes explanations, examples, and exercises to help you grasp the concept and apply it effectively in your code.

## Table of Contents

- [Introduction](#introduction)
- [How Recursion Works](#how-recursion-works)
- [Base Case and Recursive Case](#base-case-and-recursive-case)
- [Common Recursive Algorithms](#common-recursive-algorithms)
  - [Factorial Calculation](#factorial-calculation)
  - [Fibonacci Sequence](#fibonacci-sequence)
  - [Tree Traversal](#tree-traversal)
- [Languages Covered](#languages-covered)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Recursion occurs when a function calls itself in order to solve a problem. The function typically includes a base case, which provides a condition to stop the recursion, and a recursive case, which breaks the problem down into smaller instances.

## How Recursion Works

1. **Base Case**: The simplest instance of the problem that can be solved directly. This prevents infinite recursion.
2. **Recursive Case**: The part of the function where the function calls itself with a modified argument to solve a smaller problem.

## Base Case and Recursive Case

- **Base Case**: Stops the recursion. Example: `if n == 0: return 1`.
- **Recursive Case**: The function calls itself with new parameters. Example: `return n * factorial(n - 1)`.

## Common Recursive Algorithms

### Factorial Calculation

The factorial of a non-negative integer `n` is the product of all positive integers less than or equal to `n`. It's defined as:

- `factorial(0) = 1`
- `factorial(n) = n * factorial(n - 1)`

### Fibonacci Sequence

The Fibonacci sequence is a series where each number is the sum of the two preceding ones. It starts with 0 and 1:

- `fibonacci(0) = 0`
- `fibonacci(1) = 1`
- `fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)`

### Tree Traversal

Tree traversal involves visiting all nodes in a tree structure. Common traversals include:

- **In-order**: Left subtree → Root → Right subtree
- **Pre-order**: Root → Left subtree → Right subtree
- **Post-order**: Left subtree → Right subtree → Root

## Languages Covered

This repository includes examples in various programming languages, including:

- Python
- JavaScript
- Java
- C++
- Ruby

## Examples

Each language directory contains examples and explanations of recursive functions. Check the respective language folders for code samples and exercises.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

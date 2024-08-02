# Patterns Program

This repository contains a collection of different pattern generation functions in Python. Each function generates a specific pattern that can be dynamically sized based on the input parameter.

## Patterns

1. **Right-Angle Triangle**
   - **Function**: `pattern_right_angle_triangle(n)`
   - **Description**: Generates a right-angle triangle of asterisks.
   - **Example**:
     ```python
     pattern_right_angle_triangle(4)
     ```
     Output:
     ```
     *
     **
     ***
     ****
     ```

2. **Square Grid of Asterisks**
   - **Function**: `pattern_square_grid(n)`
   - **Description**: Generates a grid of asterisks.
   - **Example**:
     ```python
     pattern_square_grid(4)
     ```
     Output:
     ```
     * * * * 
     * * * * 
     * * * * 
     * * * * 
     ```

3. **Right-Angle Triangle of Numbers**
   - **Function**: `pattern_right_angle_triangle_numbers(n)`
   - **Description**: Generates a right-angle triangle of numbers.
   - **Example**:
     ```python
     pattern_right_angle_triangle_numbers(4)
     ```
     Output:
     ```
     1 
     1 2 
     1 2 3 
     1 2 3 4 
     ```

4. **Number Triangle**
   - **Function**: `pattern_number_triangle(n)`
   - **Description**: Generates a triangle with repeating numbers.
   - **Example**:
     ```python
     pattern_number_triangle(5)
     ```
     Output:
     ```
     1 
     2 2 
     3 3 3 
     4 4 4 4 
     5 5 5 5 5 
     ```

5. **Inverted Right-Angle Triangle of Asterisks**
   - **Function**: `pattern_inverted_right_angle_triangle_asterisks(n)`
   - **Description**: Generates an inverted right-angle triangle of asterisks.
   - **Example**:
     ```python
     pattern_inverted_right_angle_triangle_asterisks(4)
     ```
     Output:
     ```
     * * * * 
     * * * 
     * * 
     * 
     ```

6. **Inverted Right-Angle Triangle of Numbers**
   - **Function**: `pattern_inverted_right_angle_triangle_numbers(n)`
   - **Description**: Generates an inverted right-angle triangle of numbers.
   - **Example**:
     ```python
     pattern_inverted_right_angle_triangle_numbers(5)
     ```
     Output:
     ```
     1 2 3 4 5 
     1 2 3 4 
     1 2 3 
     1 2 
     1 
     ```

7. **Pyramid of Asterisks**
   - **Function**: `pattern_pyramid_asterisks(n)`
   - **Description**: Generates a pyramid of asterisks.
   - **Example**:
     ```python
     pattern_pyramid_asterisks(5)
     ```
     Output:
     ```
        *        
       ***       
      *****      
     *******     
    *********    
     ```

8. **Diamond of Asterisks**
   - **Function**: `pattern_diamond_asterisks(n)`
   - **Description**: Generates a diamond shape of asterisks.
   - **Example**:
     ```python
     pattern_diamond_asterisks(5)
     ```
     Output:
     ```
        *        
       ***       
      *****      
     *******     
    *********    
     *******     
      *****      
       ***       
        *        
     ```

9. **Diamond of Asterisks with a Single Line in the Middle**
   - **Function**: `pattern_diamond_asterisks_single_line(n)`
   - **Description**: Generates a diamond shape with a single line in the middle.
   - **Example**:
     ```python
     pattern_diamond_asterisks_single_line(5)
     ```
     Output:
     ```
     *
     **
     ***
     ****
     *****
     ****
     ***
     **
     *
     ```

10. **Alternating Binary Pattern**
    - **Function**: `pattern_alternating_binary(n)`
    - **Description**: Generates a pattern of alternating 0s and 1s.
    - **Example**:
      ```python
      pattern_alternating_binary(5)
      ```
      Output:
      ```
      1 
      0 1 
      1 0 1 
      0 1 0 1 
      1 0 1 0 1 
      ```

11. **Number Pyramid**
    - **Function**: `pattern_number_pyramid(n)`
    - **Description**: Generates a pyramid of numbers with decreasing spaces.
    - **Example**:
      ```python
      pattern_number_pyramid(4)
      ```
      Output:
      ```
      1      
      1 2 1  
      1 2 3 2 1  
      1 2 3 4 3 2 1  
      ```

12. **Incremental Number Triangle**
    - **Function**: `pattern_incremental_number_triangle(n)`
    - **Description**: Generates a triangle of incremental numbers.
    - **Example**:
      ```python
      pattern_incremental_number_triangle(5)
      ```
      Output:
      ```
      1 
      2 3 
      4 5 6 
      7 8 9 10 
      11 12 13 14 15 
      ```

13. **Alphabet Triangle**
    - **Function**: `pattern_alphabet_triangle(n)`
    - **Description**: Generates a triangle of alphabet characters.
    - **Example**:
      ```python
      pattern_alphabet_triangle(5)
      ```
      Output:
      ```
      A 
      A B 
      A B C 
      A B C D 
      A B C D E 
      ```

14. **Inverted Alphabet Triangle**
    - **Function**: `pattern_inverted_alphabet_triangle(n)`
    - **Description**: Generates an inverted triangle of alphabet characters.
    - **Example**:
      ```python
      pattern_inverted_alphabet_triangle(5)
      ```
      Output:
      ```
      A B C D E 
      A B C D 
      A B C 
      A B 
      A 
      ```

15. **Repeating Alphabet Triangle**
    - **Function**: `pattern_repeating_alphabet_triangle(n)`
    - **Description**: Generates a repeating alphabet triangle pattern.
    - **Example**:
      ```python
      pattern_repeating_alphabet_triangle(5)
      ```
      Output:
      ```
      A 
      B B 
      C C C 
      D D D D 
      E E E E E 
      ```

16. **Alpha-Hill**
    - **Function**: `pattern_alpha_hill(n)`
    - **Description**: Generates an Alpha-Hill pattern with letters.
    - **Example**:
      ```python
      pattern_alpha_hill(5)
      ```
      Output:
      ```
        A        
       A B A       
      A B C B A      
     A B C D C B A     
    A B C D E D C B A    
      ```

## Usage

To use any of these functions, call the function with the desired size as the parameter. For example:

```python
pattern_right_angle_triangle(5)

# Python Programming Assignment

**Author:** Spriha Sahu  
**Language:** Python 3  
**Repository:** [Python_Assignment](https://github.com/sprihasahu/Python_Assignment)

Python exercises covering functions, conditional statements, loops, number operations, string processing, and patterns. The assignment has 30 questions, organised into 32 Python files, with separate files for alternative string-reversal and uppercase-conversion approaches.

## Programs

| Question | Topic | File(s) |
| --- | --- | --- |
| 1 | Even or odd | `even_odd.py` |
| 2 | Positive, negative or zero | `neg_pos.py` |
| 3 | Largest of two numbers | `largest_no.py` |
| 4 | Largest of three numbers | `largest_no_three.py` |
| 5 | Sum of natural numbers | `sum_natural.py` |
| 6 | Multiplication table | `mul_table.py` |
| 7 | Factorial | `fac_no.py` |
| 8 | Count digits | `count_digits.py` |
| 9 | Reverse a number | `rev_no.py` |
| 10 | Prime number | `prime_no.py` |
| 11 | Count characters | `count_char.py` |
| 12 | Count vowels | `count_vowels.py` |
| 13 | Count consonants | `count_consonants.py` |
| 14 | Count vowels and consonants | `count_vow_con.py` |
| 15 | Reverse a string: loop and slicing | `rev_str.py`, `rev_str_2.py` |
| 16 | Check palindrome | `palindrome.py` |
| 17 | Count words | `count_words.py` |
| 18 | Character frequency | `freq_char.py` |
| 19 | Remove spaces | `remove_spaces.py` |
| 20 | Convert to uppercase: upper() and character codes | `low_upcase.py`, `low_upcase_2.py` |
| 21 | Count uppercase, lowercase, digits and spaces | `count_lowup_char.py` |
| 22 | Find first character | `find_first.py` |
| 23 | Find last character using indexing | `find_last.py` |
| 24 | Print each character | `print_each_char.py` |
| 25 | Print characters with positions | `print_char_position.py` |
| 26 | Remove vowels | `rem_vowels.py` |
| 27 | Find longest word | `longest_word.py` |
| 28 | Count each vowel separately | `count_occ_vowels.py` |
| 29 | Star pattern | `star_pattern.py` |
| 30 | Number pattern | `number_pattern.py` |

## Requirements

- Python 3
- A terminal or an editor such as VS Code
- No external Python packages are required.

## How to Run

Download and extract the repository, or clone it if Git is installed:

```bash
git clone https://github.com/sprihasahu/Python_Assignment.git
cd Python_Assignment
```

Open a terminal in the folder containing the `.py` files. Run a program by its filename:

```bash
python even_odd.py
```

More examples:

```bash
python largest_no.py
python count_vowels.py
python star_pattern.py
```

On Windows, use `py` instead of `python` if needed. On macOS or Linux, use `python3` if needed.

The programs use example values in their function calls and print their results. They do not prompt for keyboard input. To try another value, edit the function call, save the file, and run it again.

For example, in `largest_no.py`:

```python
print(find_largest(10, 25))
```

Output:

```text
25
```

## Assignment Notes

- Question 23 currently demonstrates `text[-1]`. The loop-based approach required by the question still needs to be added.
- In the question sheet, two example counts need correction: `Python Programming` has 4 vowels and 13 consonants; `Python123 ABC` has 4 uppercase letters, 5 lowercase letters, 3 digits and 1 space.

## Learning Objectives

- Define and call functions with parameters and return values.
- Apply `if`, `elif`, and `else` conditions.
- Use `for`, `while`, and nested loops.
- Process strings with indexing, slicing, and character methods.
- Solve basic number problems and print patterns.


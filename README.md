# Advent of Code 2023

https://adventofcode.com/

I may do a few of these puzzles as I have time. So far I have completed the first day. I'm approaching this as if I were writing code for a professional application. By that I mean I'm focused on code readability, composability, and testability rather than trying to solve the puzzles as fast as possible or play 'code golf'.

I am interested in writing the most performant algorithms I can think of and learning some algorithm tricks, but this is secondary to the goals above.

## Day 1

This is not a complex puzzle, but as I typed out the following, it struck me how much detail it contains, how many small decisions need to be made, and how much one can actually say about even a simple problem like this.

### Part 1 & Pure Functional Approach

In this problem you are given a list of apparently random alphanumeric strings. The goal is to extract the first and last number from the string to make a two-digit number. The final result is the sum of all of these two-digit numbers.

The input file for both parts of this problem is in `01/input.txt`.

I approached this problem from a functional programming (FP) perspective. In my mind, this is all about the _transforming_ the data in stages. Each 'transform' is a function taking in a particular input and giving a particular output.

The transformation steps can be summarized like this.

```
input -> split -> parse -> join -> sum -> output
```

In true FP fashion, we start with the input data and 'pipe' it through each transformation in order. The output of each step becomes the input of the next until we reach the final result. At that point we have 'reduced' our large input string to a single number.

So the first step is to read the input and split it into lines. This can be thought of as having one large `str` containing newline characters (`'\n'`) as the input, then calling the `split` method on that string to get a `list` of `str`. This is the first 'transform'. Note that in this case the transform is reversible. We could reconstruct the original string from the list of lines by calling the `join` method on the newline character.

Python saves us effort of course. When we read the file, we can use a `for` loop to iterate each line. Under the hood, Python is creating a generator function that reads and `yield`s each newline as we need it.

The next transform happens at the level of each level. The lines contain numbers and letters. For part 1 of this problem, we want to extract the numbers and discard the letters.

In this case the transformation looks like this:

```python
'3eight44' -> ['3', '4', '4']
```

We are _transforming_ the input string into a list of number characters. Note that unlike the first operation, this cannot be reversed, but there is still a sort of equivalency between the input string and the output list.

Next we want to get the first and last number from that list. This is very easily done in Python by indexing the list. The first index `0` and the last number is always at index `-1`.

```python
digits = ['3', '4', '4']
first = digits[0]  # '3'
last = digits[-1]  # '4'
concatenated = first + last  # '34'
```

One tricky detail here is that if a number appears only once, it counts as BOTH the first and last number.

So for example in this case:

```python
'aefbd3dasdun' -> ['3']
```

We want the concatenated result to be `'33'`. Fortunately, using the `0` and `-1` indexes works just fine.

Notice how up until this point we've been working with strings that contain number characters. I think it is a good idea to stick with strings for as many steps as possible and _avoid mixing or switching between string and number types_. This is a very common pitfall and source of both complexity and bugs that I have often seen developing on a team.

The final step is simple: convert each line's two-digit numbers from `str` to `int` and `sum` that list of numbers.

### Part 2 Tricky Twist

The second part adds a twist: now any of the numbers 'one' through 'nine' in word form must also be identified.

This means we can no longer check characters one-by-one. We have to find entire words in the string.

I'm sure there is a more efficient way to do this than I did. I took a naive approach. Using a recursive function, I start by looking at the start of the string. If it contains a digit or a number word, then I save that to a list. Then I pop the first character off the string and call the function again. This continues until the string is empty.

At first, I was removing the entire number string when I detected one, but this was not giving a correct result. I started going through the results line by line and found the issue.

One of the lines contained _overlapping_ number words:

```python
'3oneight44'
```

In this case, the result should be:

```python
'3oneight' -> ['3', 'one', 'eight']
```

But I was missing the `eight` because I was removing the `one` and the first character `e` from `eight` so I was getting `31` as the value for this line, when it should have been `38`. This must have also been happening on other lines.

Beyond that, I had to convert the number words to digits. I did this by creating a lookup table, which you can see in `01/common.py`.

So overall, the pipeline of transforms was very similar to part 1, except that the line parsing function became more complicated and there was an additional step to convert the number words to digits.

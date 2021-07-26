# randomizing-algorithm
- Random number generating algorithm

- I've heard that the way computers generate random numbers is not really random, but algorithm based.

- This algorithm does generate varying numbers, but some repeated many times, and some never appear.

- works better for larger number ranges, for small ranges variation is little

- I'm currently working on an algorithm which does not repeat numbers at all

- Open a pull request or issue if you spot any problems

# how it works

- makes a list of all the integers in the given range
- shuffles the list twice using the randomize list algorithm
  - originally, it would shuffle the list using the picking algorithm, but then i found out that the picking algorithm excludes some numbers and repeates other
  - Now there is another algorithm that I added which shuffles this list by pushing all the numbers down by 1. the last number is moved to the start. every 5 number generations, the program will push the list a few times.
- picks an algorithm decided number from the list

![](pong_demo_3.gif)

# Stats


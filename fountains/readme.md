# Problem

Fountains are installed at every position along a one-dimensional garden of length n. Array locations[] represents the coverage limit of these fountains. The ith fountain (where 1 ≤ i ≤ n)  has a coverage limit of locations[i] that can range from the position max( (i - locations[i]), 1 ) to min( (i + locations[i] ), n ). In other words, the fountains do not reach outside the boundaries of the garden. In the beginning, all the fountains are switched off. Determine the minimum number of fountains that need to be activated to cover the n length garden by water.
 
## Example

```
n = 3
locations[] = {0, 2, 1}
```
then

- For position 1: locations[1] = 0, max( (1 - 0), 1) to min( (1+0), 3) gives range = 1 to 1
- For position 2: locations[2] = 2, max( (2 - 2), 1) to min( (2+2), 3) gives range = 1 to 3
- For position 3: locations[3] = 1, max( (3 - 1), 1) to min( (3+1), 3) gives range = 2 to 3

For the entire length of this garden to be covered, only the fountain at position 2 needs to be activated.  
 
## Function Description

Complete the function `fountain_activation` in the editor below.
 
`fountain_activation` has the following parameter:
- `int locations[n]`:  the fountain locations

Returns 
- `int`: the minimum number of fountains that must be activated
 
Constraints
1 ≤ n ≤ 105
0 ≤ locations[i] ≤ min( n,100) (where 1 ≤ i ≤ 105)
 
## Input Format For Custom Testing
The first line contains an integer, n, the number of elements in locations.

Each line i of the n subsequent lines (where 1 ≤ i ≤ n) contains an integer, locations[i].

Sample Case 0

Sample Input For Custom Testing

```
STDIN     Function 
-----     -------- 
3    →    locations[] size n = 3
1    →    locations[] = [ 1, 1, 1 ]
1
1
Sample Output
1
```

## Explanation

Here, locations = {1, 1, 1}
 
- For position 1: locations[1] = 1, max( (1 - 1), 1) to min( (1+1), 3) gives range = 1 to 2
- For position 2: locations[2] = 1, max( (2 - 1), 1) to min( (2+1), 3) gives range = 1 to 3
- For position 3: locations[3] = 1, max( (3 - 1), 1) to min( (3+1), 3) gives range = 2 to 3

If the 2nd fountain is active, the range from position 1 to 3 will be covered. The total number of fountains needed is 1.

# Approach

1. Iterate through array of `locations`
2. Turn on first fountain
3. As next fountain is approached, test whether it has better range than previous fountain.
4. If it is a better choice, previous fountain can safely de-activated and current one be activated    
5. This will result in a local minimum of activated fountains. 
   
## Explanation for un-optimized solution

Legend:
```
+ Fountain activated
- Fountain never touched (not activated)
r Fountain activation reverted
```

Simple example:

```
 + - + -
[1,1,1,1]
 ---   
   -----
-> 2
```

More complex example:

```
 r + - - - r + - -
[1,3,1,1,1,1,2,1,1]
 ---------   
         ---------
-> 2
```

Even more complex example:

```
 + - r + - - r + - -
[1,1,1,2,1,1,1,3,1,1]
 ---
   ---------   
         -----------
-> 3
```


## Optimized Solution

To achieve global minimum, there are a couple of options:

- utilize look-back
- brute-force: generate all possible solutions and pick minimum (backtracking)


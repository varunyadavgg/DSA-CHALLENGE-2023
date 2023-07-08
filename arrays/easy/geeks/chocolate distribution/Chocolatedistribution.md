Here's the code with step-by-step explanations using code snippets:

```python
def findMinDiff(arr, n, m):
    if (m == 0 or n == 0):
        return 0
    arr.sort()
    if (n < m):
        return -1
    min_diff = arr[n-1] - arr[0]
    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])
    return min_diff
```

Explanation:

1. The `findMinDiff` function takes three parameters: `arr` (list of packet sizes), `n` (number of packets), and `m` (number of students).

2. The function checks if there are no chocolates (`m == 0`) or no packets (`n == 0`). If either of these conditions is true, it returns 0.

3. The `arr` list is sorted using the `sort` method, which rearranges the elements in ascending order.

4. It checks if the number of packets (`n`) is less than the number of students (`m`). If this condition is true, it means there are fewer packets than students, and it returns -1.

5. The `min_diff` variable is initialized with the difference between the largest and smallest packet sizes (`arr[n-1] - arr[0]`). This represents the largest possible difference.

6. A loop is started using the `range` function from 0 to `len(arr) - m + 1`. This loop finds the subarray of size `m` such that the difference between the last element and the first element is minimum.

7. In each iteration, it calculates the difference between the last element of the subarray (`arr[i + m - 1]`) and the first element of the subarray (`arr[i]`). It updates `min_diff` with the minimum value between the current `min_diff` and the calculated difference using the `min` function.

8. After the loop, the function returns the final value of `min_diff`, representing the minimum difference between the maximum and minimum values of the chocolate distribution.

Here's an example usage of the `findMinDiff` function:

```python
arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7
n = len(arr)
print("Minimum difference is", findMinDiff(arr, n, m))
```

Output:
```
Minimum difference is 10
```

In this example, the `arr` list represents the sizes of different chocolate packets. We want to distribute these packets among 7 students (`m`). The `findMinDiff` function is called with the `arr`, `n`, and `m` values, and it returns the minimum difference between the maximum and minimum values of the chocolate distribution, which is 10 in this case.
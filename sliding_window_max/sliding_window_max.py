'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

"""

Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Expected Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""

def sliding_window_max(nums, k, i=0, big_boys=[]):
    # given a list of numbers and a maximum window
    # find the maximum values within the given windows

    # What is my base case?
    # - when i + k >= len(nums)
    if i + k > len(nums):
        return big_boys

    # How is the window being kept track of?
    # - The window is being tracked from the starting
        # position of i: i + k
    # - i will be stored as a paramater

    largest = nums[i]
    for n in nums[i:i+k]:
        if n > largest:
            largest = n

    big_boys.append(largest)

    # How am I storting max values?
    # - max_values will be stored as an array
        # being held as a parmater

    return sliding_window_max(nums, k, i + 1, big_boys)



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

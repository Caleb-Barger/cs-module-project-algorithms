'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):


    for i in range(len(arr)):
        # wall is at 0
        wall = i
        
        # iterate from current iterator + 1 to len(arr) - 1
        for j in range(i+1, len(arr)):
            if arr[j] == 0:
                wall = j

        arr[i], arr[wall] = arr[wall], arr[i]
        
    
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
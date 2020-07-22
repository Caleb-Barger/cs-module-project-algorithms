'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # base case(s)?
    # the array has a len of 1
    if len(arr) == 1:
        return arr[0]
    # the array has a len of 0
    if len(arr) == 0:
        return -1

    # if that number appears more than once
    for i in range(1, len(arr)):
        # check the current index agenst the first number
        if arr[i] == arr[0]:
            del arr[i]
            # call self with new arr
            return single_number(arr[1:])
        else:
            return single_number([arr[0]])

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
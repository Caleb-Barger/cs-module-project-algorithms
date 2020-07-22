'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr, ex_i=0, new_arr=[]):
    # base case(s)?
    # when the excluded index (ex_i) is greater
    # or equal to length of the arr
    if ex_i >= len(arr):
        return new_arr
    
    # otherwise
    product = 1

    # itterate through the arr
    for i in range(len(arr)):
        # if current i is not the ex_i
        if i != ex_i:
            # multiply value with product
            product *= arr[i]
    # append product to new_arr
    new_arr.append(product)
    # return a call to self with (arr, ex_i + 1, new_arr)
    return product_of_all_other_numbers(arr, ex_i + 1, new_arr)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

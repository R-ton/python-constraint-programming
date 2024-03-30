
# 4_backtracking.pdf
# class Backtrack:
#     def __init__(self, set=[]) -> None:
#         if not iter(set):
#             raise "the set is not iterable"
#         self.set=set

"""
A function that finds a valid combination of elements from a given set that sums up to a given value.

Parameters:
    set (list): A list of integers representing the set.
    x (int): The value to compare the sum of elements in the set to.

Returns:
    list or None: A valid combination of elements from the set that sums up to x, or None if no valid combination is found.
"""
def x_set_combination(set=[],x=1):   
    if not iter(set):
        raise ValueError("the set is not iterable") 

    """
    Check if the sum of elements in a given set is equal to a given value.

    Parameters:
        original_set (list): A list of integers representing the set.
        x (int): The value to compare the sum of elements in the set to.

    Returns:
        bool: True if the sum of elements in the set is equal to x - 1, False otherwise.
    """
    def is_valid(original_set, x):
        # accumulate value in the set
        subset_sum = 0
        for i in original_set:
            if(subset_sum <= x - 1): #substract to one because of first element in the set as 1
                subset_sum += i
        if(subset_sum == x - 1):
            return True
        else:
            return False
    
    """
    A backtracking function to find a valid subset of a given set that satisfies certain conditions.
    
    Parameters:
        original_set (list): The original set of integers.
        sub_set (list): The subset of integers being constructed.
        x (int): The target sum to achieve.
        x_count (int): The current sum of integers in the subset.
        counter (int): The index for iterating over the original set.
    
    Returns:
        list or None: A subset that adds up to the target sum 'x', or None if no valid subset is found.
    """
    def backtrack(original_set, sub_set, x, x_count, counter):
        x_diff = x - x_count
        if is_valid(sub_set, x):
            return sub_set
        else:
            if counter >= len(original_set):
                return None
            x_count += original_set[counter]
            counter += 1
            sub_set = sub_set[1:]  # Modify the sublist directly
            return backtrack(original_set, sub_set, x, x_count, counter)

   
    x_count = 1
    counter = 0
    result = backtrack(set, set, x, x_count, counter)
    return [1] + result if result is not None else None
print(x_set_combination([1,2,3,4,5,6,7], 19))   

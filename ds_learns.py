#Solution:

# Here is a short solution with a dict comprehension.
# The lesson gives an example of how to do this with an explicit loop.
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)



Solution: A straightforward (and totally fine) solution is to replace the original print call with:
if total_candies == 1:
    print("Splitting 1 candy")
else:
    print("Splitting", total_candies, "candies")
Here's a slightly more succinct solution using a conditional expression:

print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")



#Try to identify the bug and fix it in the cell below:
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False

#fix

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
     #This will ensure We've exhausted the list without finding a lucky number
    return False
    # one-line version using a list comprehension with Python's any function
    return any([num % 7 == 0 for num in nums])
has_lucky_number([3,7,5,6,14])
# Check your answer
q1.check()

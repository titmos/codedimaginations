#to prevent RuntimeWarning
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)



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

#dictionary comprehension
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    y = []
    for j, i in enumerate(doc_list):
        listd = i.split()
        processed = [listdn.rstrip(".,?").lower() for listdn in listd]
        #listd = listd.rstrip(',.')
        print(processed)
        if keyword.lower() in processed:
            y.append(j)
    print(y)
    # list to hold the indices of matching documents
    return y
    pass


def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    y = []
    for j, i in enumerate(doc_list):
        listd = i.split()
        processed = [listdn.rstrip(".,?").lower() for listdn in listd]
        #listd = listd.rstrip(',.')
        print ('Processed list ', processed)
        if keyword.lower() in processed:
            y.append(j)
            print(keyword, ' found in ', i)
    print(y)
    # list to hold the indices of matching documents
    return y
    pass
# Check your answer
q2.check()


'''We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.

Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.

Create a series star_ratings with the number of stars corresponding to each review in the dataset.'''


def ratings(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
    pass
star_ratings = reviews.apply(ratings, axis='columns')

# Check your answer
q7.check()
star_ratings



# function to replace rows in the provided column of the provided dataframe
# that match the provided string above the provided ratio with the provided string
def replace_matches_in_column(df, column, string_to_match, min_ratio = 47):
    # get a list of unique strings
    strings = df[column].unique()
    
    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match
    
    # let us know the function's done
    print("All done!")

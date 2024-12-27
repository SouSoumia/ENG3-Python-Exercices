import math
import statistics

def length(lst):
    """Returns the number of elements in the list."""
    return len(lst)

def mean(lst):
    """Calculates the arithmetic mean of the list."""
    if not lst:  
        return None
    return sum(lst) / len(lst)

def range_of_list(lst):
    """Returns the difference between the maximum and minimum values in the list."""
    if not lst:  
        return None
    return max(lst) - min(lst)

def median(lst):
    """Returns the median of the list."""
    if not lst:  
        return None
    return statistics.median(lst)

def standard_deviation(lst):
    """Returns the standard deviation of the list."""
    if not lst:  
        return None
    mean_value = mean(lst)
    variance = sum((x - mean_value) ** 2 for x in lst) / len(lst)
    return math.sqrt(variance)

def list_statistics(lst):
    """Returns a dictionary with all statistics of the list."""
    if not isinstance(lst, list) or not all(isinstance(i, (int, float)) for i in lst):
        return "Error: Input must be a list of numeric values."

    if not lst:
        return {
            "Length": 0,
            "Mean": None,
            "Range": None,
            "Median": None,
            "Standard Deviation": None,
        }

    return {
        "Length": length(lst),
        "Mean": mean(lst),
        "Range": range_of_list(lst),
        "Median": median(lst),
        "Standard Deviation": standard_deviation(lst),
    }

# Test cases
def test():
    test_cases = [
        [],  # Empty list
        [5],  # Single element
        [-10, 0, 10, 20],  # List with negative numbers
        [1.5, 2.5, 3.5, 4.5],  # List with floating-point numbers
        [1, 2, 3, 4, 5],  # General case
    ]

    for i, case in enumerate(test_cases, 1):
        print(f"Test Case {i}: {case}")
        print("Statistics:", list_statistics(case))
        print()

# Run the tests
if __name__ == "__main__":
    test()

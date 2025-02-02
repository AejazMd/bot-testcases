def reverse_list(input_list):
    """
    Reverse a given list and return the result.

    Args:
    input_list (list): The list to be reversed.

    Returns:
    list: A new list with elements in reverse order.
    """
    return input_list[::-1]

def print_reversed_list(input_list):
    """
    Print elements of a list in reverse order.

    Args:
    input_list (list): The list to be printed in reverse order.
    """
    reversed_list = reverse_list(input_list)
    for item in reversed_list:
        print(item)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print_reversed_list(sample_list)
def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    rev_list = list1[::-1]
    return rev_list[:n]
print(main([1,2,3,4,5], 4))
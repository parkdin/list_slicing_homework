def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    reverse = list1[::-1]
    return list1.extend(reverse)

print(main([1,2,3,4,5]))
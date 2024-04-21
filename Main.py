def string_length(string):
    """ 1.a Determining the length of the string
    :param string: Input string
    :return: int Length of the string"""
    return len(string)


def concatenate_strings(first_string, second_string):
    """ 1.b Concatenate strings
    :param first_string: Input 1st string
    :param second_string: Input 2nd string
    :return: Concatenate strings"""
    return first_string + second_string


def square_number(number):
    """ 2.a Finding the square of a number
    :param number: Input number
    :return: square of a number"""
    return number ** 2


def sum_two_number(first_number, second_number):
    """ 2.b Finding the sum of a two numbers
    :param first_number: Input 1st number int or float
    :param second_number: Input 2nd number int or float
    :return: sum of a numbers"""
    return first_number + second_number


def division_with_remainder(first_number, second_number):
    """ 2.c Operations of division and return of quotient and remainder
    :param first_number: Input 1st number int or float
    :param second_number: Input 2nd number int or float
    :return: quotient and remainder"""
    quotient = first_number // second_number
    remainder = first_number % second_number
    return quotient, remainder


def average_of_list(numbers):
    """ 3.a Average value from list
    :param numbers: Input list
    :return: Average value"""
    return sum(numbers) / len(numbers)


def both_of_lists(first_list, second_list):
    """ 3.b Getting common elements of both lists
    :param first_list: Input 1st list
    :param second_list: Input 2nd list
    :return: elements of both lists"""
    return list(set(first_list) & set(second_list))


def get_keys(dictionary):
    """ 4.a Function to return all dictionary keys
    :param dictionary: Input dict
    :return: list of keys"""
    return list(dictionary.keys())


def merge_dicts(first_dictionary, second_dictionary):
    """ 4.b Function for merging two dictionaries
    :param first_dictionary: Input 1st dict
    :param second_dictionary: Input 2nd dict
    :return: merged dicts"""
    return first_dictionary | second_dictionary


def union_of_sets(first_set, second_set):
    """ 5.a Function to return union sets

    :param first_set: Input 1st set
    :param second_set: Input 2nd set
    :return: union of sets
    """
    return first_set | second_set


def is_subset(first_set, second_set):
    """ 5.b Function for determining whether one set is a subset of another

    :param first_set:
    :param second_set:
    :return: True under the condition that first set is a second set
    """
    return first_set.issubset(second_set)


def paired_or_unpaired(number):
    """ 6.a Function to determine whether a number is paired or unpaired

    :param number: Input number
    :return: Paired or unpaired number
    """
    if number % 2 == 0:
        print("Парне")
    else:
        print("Непарне")


def find_paired_numbers(numbers):
    """ 6.b For finding paired numbers

    :param numbers: Input list number
    :return: List of paired numbers
    """
    paired_numbers = []
    for number in numbers:
        if number % 2 == 0:
            paired_numbers = paired_numbers + [number]
    return paired_numbers


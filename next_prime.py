def is_prime(in_number):
    """
    Implement prime number algo
    """
    if in_number <= 3:
        return in_number > 1
    elif in_number % 2 == 0 or in_number % 3 == 0:
        return False

    for num in range(5, in_number/2):
        if in_number % num == 0:
            return False

    return True


def next_prime(in_number):
    if is_prime(in_number):
        return in_number

    while(not is_prime(in_number)):
        in_number = in_number + 1

    return in_number


def print_star(s_count=3):
    for line in range(1, s_count + 1):
        stars = (line * 2) - 1
        print("{spaces}{star}".format(
            star="*" * stars, spaces=" " * (s_count - line)))

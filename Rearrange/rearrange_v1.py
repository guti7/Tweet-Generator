import random


def reorder(list):
    result = []
    while len(list) > 1:
        random_index = random.randint(1, len(list) - 1)
        result.append(list.pop(random_index))
    return result

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        print reorder(sys.argv)

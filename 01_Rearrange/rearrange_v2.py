import random

# Randomly rearranges a set of words provided as command-line arguments
def reorder(list):
    list.pop(0)
    result = []
    while len(list) > 0:
        random_index = random.randint(0, (len(list) - 1) * 1000)
        range_index = random_index % len(list)
        result.append(list.pop(range_index))
    return result

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        list = reorder(sys.argv)
        for item in list:
            print item,

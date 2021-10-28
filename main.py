def findThreeLargestNumbers(array):
    """
    Write a function that takes in an array of at least three integers and, without sorting the input array,
    returns a sorted array of the three largest integers in the input array.
    """
    threeLargest = [None for _ in range(3)]
    for num in array:
        updateArray(threeLargest, num)
    return threeLargest


def updateArray(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)


def shiftAndUpdate(array, num, index):
    for i in range(index + 1):
        if i == index:
            array[i] = num
        else:  # All Indices BEFORE or "index"
            array[i] = array[i + 1]

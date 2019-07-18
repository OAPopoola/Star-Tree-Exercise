def startree(h):
    """
    This function draws a star tree pattern h levels high
    :param h:
    :return: None
    please not this tre
    """
    for i in range(h):
        print(" " * (h-i-1) + "x" * (1 + (2*i)))

startree(6)
'''
нужно написать программу, которая определяет, есть ли цикл в связном списке.
'''


def hasCycle(node):
    first = node
    second = node
    while first is not None and second is not None and second.next is not None:
        first = first.next
        second = second.next.next
        if first is second:
            return True
    return False

# Time: 45ms, Memory: 5.51Mb

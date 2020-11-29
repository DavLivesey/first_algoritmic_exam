'''
Калькулятор обратной польской нотации
'''

OPERATORS = {'+': lambda value_1, value_2: value_1 + value_2,
             '-': lambda value_1, value_2: value_1 - value_2,
             '*': lambda value_1, value_2: value_1 * value_2,
             '/': lambda value_1, value_2: value_1 // value_2}


class EmptyStackError(IndexError):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class IncorrectSequenceError(ValueError):
    def __init__(self, text, object):
        self.text = text
        self.object = object

    def __str__(self):
        return f'{self.text}, {self.object}'


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise EmptyStackError('Your stack is empty')


def postfix_notation(sequence):
    stack = Stack()
    for element in sequence:
        if element in OPERATORS:
            operand_first = stack.pop()
            operand_second = stack.pop()
            stack.push(OPERATORS[element](
                value_2=operand_first,
                value_1=operand_second
            ))
        else:
            try:
                stack.push(int(element))
            except ValueError:
                raise IncorrectSequenceError(
                    'Incorrect element in sequence:', element
                )
    return stack.pop()


if __name__ == '__main__':
    arithmetic_sequence = input().split(' ')
    print(postfix_notation(arithmetic_sequence))

# Time: 42ms, Memory: 4.23Mb

import math

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None


def main(string: str) -> None:
    new_string = string.strip(' ').replace(' ', '')
    L = len(new_string)
    sqrt_L = math.sqrt(L)
    rows = math.floor(sqrt_L)
    cols = math.ceil(sqrt_L)

    stack = Stack()
    for c in reversed(new_string):
        stack.push(c)

    for _ in range(0, rows):
        _string = ""
        for _ in range(0, cols):
            if stack.is_empty():
                break

            _string += stack.pop()

        print(_string + '\n')


if __name__ == "__main__":
    main(string='if man was meant to stay on the ground god would have given us roots')
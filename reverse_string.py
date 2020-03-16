class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def reversed_word(stack):
    word = []
    while not stack.isEmpty():
        word.append(stack.pop())
    return word
def reverse_mawu(word):
    word_stack = Stack()
    for letter in word:
        word_stack.push(letter)
    return reversed_word(word_stack)

print(reverse_mawu("Car"))
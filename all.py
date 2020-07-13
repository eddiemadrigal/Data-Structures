class Stack:
    def __init__(self):
        self.size = 0
        self.items = []

    def isEmpty(self):
        return self.items == []

    def __len__(self):
        return len(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.items == []:
            return None
        else:
            return self.items.pop()
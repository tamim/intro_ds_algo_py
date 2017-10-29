class Stack:
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop()


    def is_empty(self):
        if self.items == []:
            return True
        return False


def is_balanced(input_str):
    s = Stack()
    for ch in input_str:
        if ch == '(':
            s.push(ch)
        if ch == ')':
            if s.is_empty():
                return False
            previous_ch = s.pop()
            if previous_ch != '(':
                return False
    if s.is_empty():
        return True
    return False


if __name__ == "__main__":
    input_str = input() 
    if is_balanced(input_str):    
        print(input_str, "is balanced.")
    else:
        print(input_str, "is not balanced.")
 

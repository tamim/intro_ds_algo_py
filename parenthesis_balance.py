def is_balanced(input_str):
    s = list()

    for ch in input_str:
        if ch == '(':
            s.append(ch)
        if ch == ')':
            if not s:
                return False
            previous_ch = s.pop()
            if previous_ch != '(':
                return False

    return not s


if __name__ == "__main__":
    input_str = input() 

    if is_balanced(input_str):    
        print(input_str, "is balanced.")
    else:
        print(input_str, "is not balanced.")
 

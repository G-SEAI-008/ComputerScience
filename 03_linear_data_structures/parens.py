def isValid(string):

    stack = []

    mapping = {")": "(", "]": "[", "}": "{"}

    for char in string:
        if char in mapping.keys():
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        elif char in mapping.values():
            stack.append(char)

    return not stack


print(isValid("def my_func(a,x)("))

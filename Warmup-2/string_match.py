def string_match(a, b):
    # Create a list of all possible length 2 substrings for a and b.
    a = [a[i:i+2] for i in range(len(a)-1)]
    b = [b[i:i+2] for i in range(len(b)-1)]
    # Determine which string is shorter and store the length.
    length = len(a) if len(a) <= len(b) else len(b)
    # Return the number of times that a match is found.
    return len([1 for i in range(length) if a[i] == b[i]])

print(string_match2('xxcaazz', 'xxbaaz'))

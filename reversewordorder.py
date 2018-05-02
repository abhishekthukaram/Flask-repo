def reversewordorder():
    str_input = raw_input("Please enter the string")
    b = str_input.split()
    print b
    # new = b.reverse()
    new = b[::-1]
    print new
    reverse_string = " ".join(new)
    print reverse_string


reversewordorder()

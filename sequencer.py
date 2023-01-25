def count_max_elements(n, max_element, count):
    if n == 0: #base case
        print(count)
        return
    else:
        if n == max_element:
            count += 1
        max_element = max(max_element, n)
        n = int(input()) # read next number from the stream
        count_max_elements(n, max_element, count) # recursive call

n = int(input()) # read the first number from the stream
count_max_elements(n, n, 0) # call the function with the first number, the current max_element and count

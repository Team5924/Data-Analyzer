def entry(input, type):
    # Locates the index of the "="
    x = 0
    for i in input:
        if i == "=":
            x = x + 1
            break
        x = x+1
    entry = []
    # Returns the data without the header information
    for i in range(x, len(input)):
        entry.append(input[i])
    # !type = qualitative; type = quantitative
    if not type:
        return "".join(entry)
    else:
        return int("".join(entry))

def replace(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            arr[i][j] = entry(arr[i][j], True)
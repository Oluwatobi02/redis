def parse_resp(data):
    lines = data.split("\r\n")
    result = []
    idx = 0

    while idx < len(lines):
        line = lines[idx]
        if line.startswith("*"):  # Array
            array_length = int(line[1:])
            result = []  # Initialize an array
        elif line.startswith("$"):  # Bulk string
            length = int(line[1:])  # Length of the string
            idx += 1  # Move to the next line (actual string)
            result.append(lines[idx][:length])
        idx += 1

    return tuple(result)

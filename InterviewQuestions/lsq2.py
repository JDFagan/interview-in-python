

# Problem - write a basic JSON parser.  Doesn't have to process inner sub-elements.
# Example: input == '{"foo":"bar"}'; result == {'foo':'bar'}
def json_parser(input : str):
    result = {}

    pos = 0
    length = len(input)
    while pos < length:
        test1 = input[pos]
        keyStartPos = pos+2
        keyEndPos = input.find('"', keyStartPos)

        keyStart = input[keyStartPos]
        keyEnd = input[keyEndPos]

        key = input[keyStartPos:keyEndPos]

        valueStartPos = keyEndPos + 3
        valueEndPos = input.find('"', valueStartPos)
        value = input[valueStartPos:valueEndPos]

        pos = valueEndPos + 2

        result[key] = value

    print(result)
    return result

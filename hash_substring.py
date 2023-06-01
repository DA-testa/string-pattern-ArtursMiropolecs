# python3

def read_input():
    input_string = input().rstrip()
    if "F" in input_string:
        with open('./tests/06', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
            return pattern, text
    elif "I" in input_string:
        pattern = input().rstrip()
        text = input().rstrip()
        return pattern, text
    else:
        print("Input error")

def print_occurrences(output):
    for pos in output:
        print(pos, end=' ')

def get_occurrences(pattern, text):
    p = 1000000007
    x = 263
    result = []
    p_hash = poly_hash(pattern, p, x)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != poly_hash(text[i:i+len(pattern)], p, x):
            continue
        if pattern == text[i:i+len(pattern)]:
            result.append(i)
    return result

def poly_hash(s, p, x):
    hash_value = 0
    for i in reversed(range(len(s))):
        hash_value = (hash_value * x + ord(s[i])) % p
    return hash_value

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
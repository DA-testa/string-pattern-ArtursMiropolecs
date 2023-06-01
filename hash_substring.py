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
    p = 1000000007 #mainigie pol.hash algoritma.
    x = 263
    result = [] #tuksa skaita
    p_hash = poly_hash(pattern, p, x) #modela pol.vert
    for i in range(len(text) - len(pattern) + 1):  # Salīdziniet pašreizējā segmenta jaucējvērtību ar modeļa jaucējvērtību
        if p_hash != poly_hash(text[i:i+len(pattern)], p, x): # Ja jaucējvērtības nav vienādas, pārejiet uz nākamo segmentu
            continue # Ja jaucējvērtības sakrīt, salīdziniet faktiskās virknes, lai nodrošinātu atbilstību
        if pattern == text[i:i+len(pattern)]: # Ja virknes sakrīt, rezultātu sarakstam pievienojiet segmenta sākuma pozīciju
            result.append(i)
    return result # Atgriezt pozīciju sarakstu

def poly_hash(s, p, x):
    hash_value = 0 # Inicializējiet jaucējvērtību kā nulli
    for i in reversed(range(len(s))): # Atkārtojiet virknes rakstzīmes apgrieztā secībā
        hash_value = (hash_value * x + ord(s[i])) % p # Atjauniniet jaucējvērtību, izmantojot polinoma jaukšanas formulu
    return hash_value # Atgriezt galīgo

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
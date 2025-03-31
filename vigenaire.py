import json
def vigenere_encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext
def chiffreJSON(f, output, key):
    with open(f, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    data2 = {}
    for k, v in data.items():
        newKey = vigenere_encrypt(k.upper(), key.upper())
        data2[newKey] = v
    
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(data2, f, ensure_ascii=False, indent=4)


f = "dictionnairE_old.json"
output = "dico.json"
key = "jaiperdu"  

chiffreJSON(f, output, key)

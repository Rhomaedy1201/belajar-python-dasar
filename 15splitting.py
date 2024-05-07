text = "Belajar Python Dasar"
listku = []
kata = ""

for huruf in text:
    if huruf != ' ':
        kata += huruf
    else:
        listku.append(kata)
        kata = ''
listku.append(kata)
print(f'text {text}')
print(f'listku {listku}')
print(f'kata {kata}')

# simple

teks = "Belajar python kedua"
listku2 = text.split(' ')
print(listku2)
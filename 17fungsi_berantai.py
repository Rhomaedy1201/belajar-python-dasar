def kali(x , y):
    return x * y

def tambah(x, y):
    return x + y

x, y = 10, 20
kondisi = True

if kondisi:
    hasil = tambah(x, y)
else: 
    hasil = kali(x, y)

print(f'Hasil: {hasil} ')
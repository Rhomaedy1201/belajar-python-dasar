data1 = {'nim': 'E41213', 'nama': 'Magas'}
data2 = {'alamat': 'Bondowoso', 'semester': 5}
data3 = {'ipk': 2.5, 'hobi': 'makan'}

hasil = {**data1, **data2, **data3}
print(hasil)
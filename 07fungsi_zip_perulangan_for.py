nim = ["001", "002", "003"]
nama = ["AJI", "SUSI", "NITA"]
hoby = ["Mancing", "Masak", "Jalan-jalan"]

for d_nim, d_nama, d_hoby in zip(nim, nama, hoby):
    print(f'{d_nim} -- {d_nama} -- {d_hoby}')
fileku = open('pesan.txt', 'w')
fileku.write('Selamat Datang\n')
fileku.write('Selamat belajar\n')
fileku.close()

# code lebih pythonic
with open('pesan2.txt', 'a') as fileku2:
    fileku2.write('Selamat Datang\n')
    fileku2.write('Selamat belajar\n')
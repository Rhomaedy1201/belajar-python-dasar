def lipat_ganda(x):
    return x * 2

listku = [10, 20, 30]
listmu = []

# penggunaan loop biasa
for item in listku:
    listmu.append(lipat_ganda(item))

print(f'listku = {listku}')
print(f'listmu = {listmu}')

# penggunaan map

listku2 = [10, 20, 30]
listmu2 = list(map(lipat_ganda, listku2))

print(f'listku map = {listku2}')
print(f'listmu map = {listmu2}')
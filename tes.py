agama = input("masukkan agama anda (islam/kristen/hindu/budha katolik): ").lower()
if agama == "islam":
    print("selamat merayakan hari raya idul fitri")
elif agama == "kristen":
    print("selamat merayakan hari natal")
elif agama == "hindu":
    print("selamat merayakan hari raya nyepi")
elif agama == "budha":
    print("selamat merayakan hari waisak")
elif agama == "katolik":
    print("selamat merayakan hari natal")
else:
    print("agama anda tidak terdaftar")

    # 1. Variabel nama
nama = "zalfi"

# 2. Cetak tiap karakter dengan while
i = 0
while i < len(nama):
    print(nama[i])
    i += 1

print("-----")

# 3. Cetak tiap karakter dengan for
for huruf in nama:
    print(huruf)

print("-----")

# 4. Cetak terbalik dengan while
i = len(nama) - 1
while i >= 0:
    print(nama[i])
    i -= 1

print("-----")

# 5. Cetak terbalik dengan for
for i in range(len(nama) - 1, -1, -1):
    print(nama[i])


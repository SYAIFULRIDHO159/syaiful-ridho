def input_usia():
    while True:
        try:
            usia = int(input("Berapakah usia anda? "))
            return usia
        except ValueError:
            print("Masukkan angka yang valid!")


def klasifikasi_usia(usia):
    if usia <= 10:
        return "Anda masih anak-anak"
    elif usia <= 19:
        return "Anda remaja"
    elif usia <= 50:
        return "Anda dewasa"
    else:
        return "Anda lansia"


def main():
    usia = input_usia()
    hasil = klasifikasi_usia(usia)
    print(hasil)


main()

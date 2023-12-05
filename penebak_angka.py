# Created By Atsiila Arya Nabiih
# Politeknik Negeri Semarang

def guess_number():
    secret_number = 9
    guess
    guess_limit = 3

    while guess < guess_limit:
        user = int(input("Masukkan angka > "))
        if user == secret_number:
            print("Selamat, anda berhasil menemukan angkanya")
            break
        else:
            print("Salah!")
            guess += 1

    else:
        print(f"Anda tidak menemukan angkanya, angka rahasianya adalah {secret_number}")
from Source_func import celcius_fahrenheit, celcius_reamur, celcius_kelvin, reamur_celcius, reamur_kelvin, reamur_fahrenheit, fahrenheit_celcius, fahrenheit_reamur, kelvin_celcius, kelvin_reamur

def celcius():
    while True:
        print("\nMenu Konversi Celcius:")
        print("1. Konversi Celcius ke Kelvin")
        print("2. Konversi Celcius ke Reamur")
        print("3. Konversi Celcius ke Fahrenheit")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")
        if pilihan == "1":
            celcius_kelvin()
        elif pilihan == "2":
            celcius_reamur()
        elif pilihan == "3":
            celcius_fahrenheit()
        elif pilihan == "4":
            print("Terima kasih! kembail ke Menu Awal.")
            break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

def reamur():
    while True:
        print("\nMenu Konversi Reamur:")
        print("1. Konversi Reamur ke Kelvin")
        print("2. Konversi Reamur ke Celcius")
        print("3. Konversi Reamur ke Fahrenheit")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")
        if pilihan == "1":
            reamur_kelvin()
        elif pilihan == "2":
            reamur_celcius()
        elif pilihan == "3":
            reamur_fahrenheit()
        elif pilihan == "4":
            print("Terima kasih! kembail ke Menu Awal.")
            break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

def fahrenheit():
    while True:
        print("\nMenu Konversi fahrenheit:")
        print("1. Konversi Fahrenheit ke Celcius")
        print("2. Konversi Fahrenheit ke Reamur")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        if pilihan == "1":
            fahrenheit_celcius()
        elif pilihan == "2":
            fahrenheit_reamur()
        elif pilihan == "3":
            print("Terima kasih! kembail ke Menu Awal.")
            break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

def kelvin():
    while True:
        print("\nMenu Konversi kelvin:")
        print("1. Konversi Kelvin ke Celcius")
        print("2. Konversi Kelvin ke Reamur")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        if pilihan == "1":
            kelvin_celcius()
        elif pilihan == "2":
            kelvin_reamur()
        elif pilihan == "3":
            print("Terima kasih! kembail ke Menu Awal.")
            break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__=='__celcius__':
    celcius()
if __name__=='__reamur__':
    reamur()
if __name__=='__fahrenheit__':
    fahrenheit()
if __name__=='__kelvin__':
    kelvin()
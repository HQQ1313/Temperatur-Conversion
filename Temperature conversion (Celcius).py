print('TEMPERATURE CONVERSION')
print('='*10)
'''
This is for learning python and make simple program
'''
from Cel_to_All import cel_to_kel, cel_to_rea, cel_to_fah

def celcius_kelvin():
    print('\nMenghitung Celcius ke Kelvin')
    suhu1= input('suhu Celcius yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Kelvin =', cel_to_kel(suhu=suhu2))

def celcius_reamur():
    print('\nMenghitung Celcius ke Reamur')
    suhu1= input('suhu Celcius yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Reamur=', cel_to_rea(suhu=suhu2))

def celcius_fahrenheit():
    print('\nMenghitung Celcius ke Fahrenheit')
    suhu1= input('suhu Celcius yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Fahrenheit =', cel_to_fah(suhu=suhu2))

def main():
    while True:
        print("\nMenu:")
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
            print("Terima kasih! Keluar dari program.")
            break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
if __name__ == "__main__":
    main()

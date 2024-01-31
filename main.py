from List import celcius, reamur, fahrenheit, kelvin
print('TEMPERATURE CONVERSION')
print('='*10)
'''
This is for learning python and make simple program
'''

def main():
    while True:
        print('\nMenu Temperature Conversion:')
        print("1. Konversi Celcius")
        print("2. Konversi Reamur")
        print("3. Konversi Fahrenheit")
        print("4. Konversi Kelvin")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        if pilihan == "1":
            celcius()
        elif pilihan == "2":
            reamur()
        elif pilihan == "3":
            fahrenheit()
        elif pilihan == "4":
            kelvin()
        elif pilihan == "5":
            print("Terima kasih! Keluar dari program.")
            break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
if __name__ == "__main__":
    main()

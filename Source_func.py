from Cel_to_All import cel_to_kel, cel_to_rea, cel_to_fah

def celcius_kelvin():
    print('\nMenghitung Celcius ke Kelvin')
    suhu1= input('suhu Celcius yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Kelvin =', cel_to_kel(suhu=suhu2), 'K')

def celcius_reamur():
    print('\nMenghitung Celcius ke Reamur')
    suhu1= input('suhu Celcius yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Reamur=', cel_to_rea(suhu=suhu2), 'ºR')

def celcius_fahrenheit():
    print('\nMenghitung Celcius ke Fahrenheit')
    suhu1= input('suhu Celcius yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Fahrenheit =', cel_to_fah(suhu=suhu2), 'ºF')


from Rea_to_All import rea_to_kel, rea_to_cel, rea_to_fah

def reamur_kelvin():
    print('\nMenghitung Reamur ke Kelvin')
    suhu1= input('suhu Reamur yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Kelvin =', rea_to_kel(suhu=suhu2), 'K')

def reamur_celcius():
    print('\nMenghitung Reamur ke Celcius')
    suhu1= input('suhu Reamur yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Celcius=', rea_to_cel(suhu=suhu2), 'ºC')

def reamur_fahrenheit():
    print('\nMenghitung Reamur ke Fahrenheit')
    suhu1= input('suhu Reamur yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Fahrenheit =', rea_to_fah(suhu=suhu2), 'ºF')


from Fah_to_All import fah_to_cel, fah_to_rea

def fahrenheit_celcius():
    print('\nMenghitung Fahrenheit ke Celcius')
    suhu1= input('suhu Fahrenheit yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Celcius =', fah_to_cel(suhu=suhu2), 'ºC')

def fahrenheit_reamur():
    print('\nMenghitung Fahrenheit ke Reamur')
    suhu1= input('suhu Fahrenheit yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Reamur =', fah_to_rea(suhu=suhu2), 'ºR')


from Kel_to_All import kel_to_cel, kel_to_rea

def kelvin_celcius():
    print('\nMenghitung Kelvin ke Celcius')
    suhu1= input('suhu Kelvin yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Celcius =', kel_to_cel(suhu=suhu2), 'ºC')

def kelvin_reamur():
    print('\nMenghitung Kelvin ke Reamur')
    suhu1= input('suhu Kelvin yg akan dikonversi:')
    suhu2 = float(suhu1)
    print('Suhu Reamur =', fah_to_rea(suhu=suhu2), 'ºR')


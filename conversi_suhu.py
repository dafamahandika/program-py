def conv_reamur(celcius):
     convert_reamur = 4 * celcius / 5
     return convert_reamur

def conv_fahrenheit(celcius):
     convert_fahrenheit = 9 * celcius / 5 + 32
     return convert_fahrenheit

def conv_kelvin(celcius):
     convert_kelvin = celcius  + 273
     return convert_kelvin

def main():
     print("Program Konversi Suhu")
     print("=====================")
     print("SMK Wikrama Bogor")

     temperature = int(input("Masukan Skala Celcius :"))
     
     print('='*20)
     print(f'Hasil Konnversi Suhu {temperature} C adalah {conv_reamur(temperature)} Reamur')
     print(f'Hasil Konnversi Suhu {temperature} C adalah {conv_fahrenheit(temperature)} Fahrenheit')
     print(f'Hasil Konnversi Suhu {temperature} C adalah {conv_kelvin(temperature)} Kelvin')
     print('='*20)

if __name__=='__main__':
     main()


def int_to_roman(x):
    roman_numerals = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
    for key in roman_numerals:
        a = x // key
        b = x % key
        if (a != 0):
            #print(f"key = {key}, a = {a}, b = {b}")
             print(roman_numerals[key])
             x = b


    
    return 'RomanNumeralString'

def main():
    var1 = 5
    var2 = 145
    print(int_to_roman(var2))

if __name__ == '__main__':
    main()

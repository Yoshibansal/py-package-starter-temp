from pyfiglet import figlet_format

def main():
    print(figlet_format("SIMPLE"))
    number  = int(input('Enter the number (only +ve allowed): '))
    print(f'{number} square is {number**2}')

if __name__ == '__main__':
    main()

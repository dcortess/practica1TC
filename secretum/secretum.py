#!/bin/python3

"""Methods to decrypt the secretum."""

import sys


def decrypt(value):
    while value > 9:
        value = sum(int(i) for i in str(value))
    return value


def decryptRecursive(value):
    value = str(value)
    suma = 0
    for i in value:
        suma += int(i)
    if (suma <= 9):
        return suma
    else:
        value = suma
        return decryptRecursive(value)


def main():
    """Main function to parse input/output
    and decrypt the secretum."""
    digits = str(sys.argv[1])
    last = int(sys.argv[2])
    result = decrypt(0)
    print('La clau per utilitzar el descodificador és {0}'.format(result))


if __name__ == '__main__':
    main()

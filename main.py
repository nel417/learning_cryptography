import math

SYMBOLS: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def caesar(message: str, key: int) -> str:
    translated: str = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index: int = SYMBOLS.find(symbol)
            translated_index: int = symbol_index + key
            if translated_index >= len(SYMBOLS):
                translated_index = translated_index - len(SYMBOLS)
            elif translated_index < 0:
                translated_index = translated_index + len(SYMBOLS)
            translated = translated + SYMBOLS[translated_index]
        else:
            translated = translated + symbol
    return translated


print(caesar('super secret message woooo', 35))


def crack_secret(message: str) -> None:
    for key in range(len(SYMBOLS)):
        cracked: str = ''
        for symbol in message:
            if symbol in SYMBOLS:
                symbol_index: int = SYMBOLS.find(symbol)
                cracked_index: int = symbol_index - key
                if cracked_index < 0:
                    cracked_index = cracked_index + len(SYMBOLS)

                cracked += SYMBOLS[cracked_index]
            else:
                cracked += symbol
        print(f"key is {key}, cracked message is {cracked}")
        # return cracked


def transpose(message: str, key: int) -> str:
    # each string is a column in a grid
    cipher_text = [''] * key
    for column in range(key):
        current = column
        while current < len(message):
            cipher_text[column] += message[current]
            current += key
    return ''.join(cipher_text)


def decrypt_transpose(message: str, key: int) -> str:
    num_of_columns = int(math.ceil(len(message) / float(key)))
    num_of_rows: int = key
    empty_box: int = (num_of_columns * num_of_rows) - len(message)

    text: list[str] = [''] * num_of_columns
    column: int = 0
    row: int = 0

    for symbol in message:
        text[column] += symbol
        column += 1
        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - empty_box):
            column = 0
            row += 1
    return ''.join(text)




crack_secret('NPK.MfN.!M.OfH.NN0B.fRJJJJ')
print(transpose('Common sense is not so Common', 8) + '|')
print(decrypt_transpose('Cenoonommstmme oo snnio s s C', 8))

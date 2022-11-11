
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


crack_secret('NPK.MfN.!M.OfH.NN0B.fRJJJJ')

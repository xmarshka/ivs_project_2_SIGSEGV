from sys import stdin

if __name__ == '__main__':
    inputs = []
    # nacitaj cisla zo stdin oddelene medzerami
    for line in stdin:
        inputs.extend(line.split())
        if not inputs:
            break # prazdny riadok
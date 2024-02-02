import filecmp
import tkinter as tk
from tkinter import filedialog

def LZWcompress(input_file):
    global original_file
    original_file = input_file
    dict_size = 4096
    dictionary = {chr(i): i for i in range(256)}

    with open(input_file, 'r') as input_file:
        data = input_file.read()

    compressed_data = []
    code = 256
    current = data[0]
    next_char = ''

    for char in data[1:]:
        if code == dict_size:
            compressed_data.append(dictionary[current])
            dictionary.clear()
            dictionary = {chr(i): i for i in range(256)}
            code = 256
            next_char = ''
            current = char
            continue

        next_char += char

        if str(current) + next_char in dictionary:
            current += next_char
        else:
            compressed_data.append(dictionary[current])
            dictionary[str(current) + next_char] = code
            current = next_char
            code += 1

        next_char = ''

    compressed_data.append(dictionary[current])

    compressed_file_size = len(compressed_data) * 2
    with open("compressed.bin", 'wb') as output_file:
        for number in compressed_data:
            output_file.write(number.to_bytes(2, byteorder='big'))

    input_file_size = len(data)
    print("---------------------------------------------")
    print("Kompresja udana.")
    print(f"Rozmiar oryginalnego pliku: {input_file_size} bajtow.")
    print(f"Rozmiar skompresowanego pliku: {compressed_file_size} bajtow.")
    print(f"Współczynnik kompresji wynosi: {compressed_file_size / input_file_size * 100}%")

def LZWdecompress(input_file):
    dict_size = 4096
    dictionary = {i: chr(i) for i in range(256)}

    with open(input_file, 'rb') as input_file:
        data = input_file.read()

    to_decode = [int.from_bytes(data[i:i+2], byteorder='big') for i in range(0, len(data), 2)]

    output_data = []
    code = 256
    prev = to_decode.pop(0)
    current = dictionary[prev]
    output_data.append(current)

    for next_code in to_decode:
        if code == dict_size + 1:
            dictionary.clear()
            dictionary = {i: chr(i) for i in range(256)}
            code = 256

        if next_code not in dictionary:
            current = dictionary[prev] + dictionary[prev][0]
        else:
            current = dictionary[next_code]

        # Dodawanie nowego ciągu znaków do słownika
        dictionary[code] = dictionary[prev] + current[0]

        prev = next_code
        code += 1
        output_data.append(current)

    with open("decompressed.txt", 'w') as output_file:
        output_file.write(''.join(map(str, output_data)))

    print("---------------------------------------------")
    print("Dekompresja udana.")
    print("---------------------------------------------")

def are_files_equal(file1, file2):
    return filecmp.cmp(file1, file2)

def load_file_for_compression():
    filename = filedialog.askopenfilename()
    LZWcompress(filename)
    tk.messagebox.showinfo("Powodzenie", "Plik został pomyślnie skompresowany.")


def load_file_for_decompression():
    global original_file
    filename = filedialog.askopenfilename()
    LZWdecompress(filename)
    print(filename)
    if are_files_equal(original_file, "decompressed.txt"):
        print("Pliki są identyczne po kompresji i dekompresji.")
        tk.messagebox.showinfo("Powodzenie", "Plik został pomyślnie zdekompresowany. Pliki są identyczne.")
    else:
        print("Pliki różnią się po kompresji i dekompresji.")
        tk.messagebox.showinfo("Niepowodzenie", "Plik nie został pomyślnie zdekompresowany. Pliki się różnią.")
    print("---------------------------------------------")

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Kompresja LZW")
    root.geometry("300x100")

    compress_button = tk.Button(root, text="Wczytaj plik do kompresji", command=load_file_for_compression)
    compress_button.pack()
    compress_button.place(relx=0.5, rely=0.3, anchor="center")

    decompress_button = tk.Button(root, text="Wczytaj plik do dekompresji", command=load_file_for_decompression)
    decompress_button.pack()
    decompress_button.place(relx=0.5, rely=0.7, anchor="center")

    root.mainloop()

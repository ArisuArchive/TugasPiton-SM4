while True:
    action = input("Pilih Program A atau B (atau 'X' untuk keluar): ").lower()

    if action == "a":
        while True:
            num = int(input("Input Angka (1-20): "))
            if num >= 1 and num <= 20:
                for i in range(num):
                    print(i * i)
                break
            elif num > 20:
                print(f"Diluar constrain: {num}")
            else:
                print(f"Angka tidak bisa negatif: {num}")

    elif action == "b":
        while True:
            num = int(input("Input Angka (1-20): "))
            if num >= 1 and num <= 20:
                for i in range(num):
                    if i % 2 == 1:
                        print(i * i)
                break
            elif num > 20:
                print(f"Diluar constrain: {num}")
            else:
                print(f"Angka tidak bisa negatif: {num}")


    elif action == "x":
        print("Keluar...")
        break

    else:
        print(f"Tidak ada program dengan kode : {action}")

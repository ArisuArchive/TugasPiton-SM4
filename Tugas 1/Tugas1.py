def total_na(input_tugas, input_uts, input_uas):
    tugas = 0.25
    uts = 0.35
    uas = 0.4
    nilai_akhir = (tugas * input_tugas) + (uts * input_uts) + (uas * input_uas)
    return nilai_akhir


def hitung_pa(nilai_akhir):

    if nilai_akhir >= 85:
        predikat = "A"
    elif nilai_akhir >= 80 and nilai_akhir <= 84:
        predikat = "A-"
    elif nilai_akhir >= 71 and nilai_akhir <= 79:
        predikat = "B+"
    elif nilai_akhir >= 66 and nilai_akhir <= 70:
        predikat = "B"
    elif nilai_akhir >= 61 and nilai_akhir <= 65:
        predikat = "B-"
    elif nilai_akhir >= 56 and nilai_akhir <= 60:
        predikat = "C+"
    elif nilai_akhir >= 51 and nilai_akhir <= 55:
        predikat = "C"
    elif nilai_akhir >= 31 and nilai_akhir <= 50:
        predikat = "C-"
    elif nilai_akhir >= 30:
        predikat = "D"
    else:
        predikat = "E"

    return predikat


def main():
    while True:
        input_tugas = float(input("Masukkan nilai tugas: "))
        input_uts = float(input("Masukkan nilai UTS: "))
        input_uas = float(input("Masukkan nilai UAS: "))

        nilai_akhir = total_na(input_tugas, input_uts, input_uas)
        predikat = hitung_pa(nilai_akhir)

        print(f"Nilai akhir: {nilai_akhir:.2f}")
        print(f"Predikat: {predikat}")

        restart = input("Apakah anda mau menghitung lagi? (y/n): ")
        if restart.lower() != 'y':
            break


main = main()

# ARI SATRIO MURDOKO ANDJALMO
# 41822010025

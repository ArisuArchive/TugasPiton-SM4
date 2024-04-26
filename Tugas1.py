def total_nilai_akhir(input_tugas,input_uts, input_uas):
  tugas = 0.25
  uts = 0.35
  uas = 0.4

  nilai_akhir = (tugas * input_tugas) + (uts * input_uts) + (uas * input_uas)

  if nilai_akhir >= 85:
    predikat = "A"
  elif nilai_akhir >= 80:
    predikat = "A-"
  elif nilai_akhir >= 75:
    predikat = "B+"
  elif nilai_akhir >= 70:
    predikat = "B"
  elif nilai_akhir >= 65:
    predikat = "B-"
  elif nilai_akhir >= 60:
    predikat = "C+"
  elif nilai_akhir >= 55:
    predikat = "C"
  elif nilai_akhir >= 50:
    predikat = "C-"
  elif nilai_akhir >= 30:
    predikat = "D"
  else:
    predikat = "E"


  return nilai_akhir, predikat

def main():
  input_tugas = float(input("Masukkan nilai tugas: "))
  input_uts = float(input("Masukkan nilai UTS: "))
  input_uas = float(input("Masukkan nilai UAS: "))

  nilai_akhir, predikat = total_nilai_akhir(input_tugas, input_uts, input_uas)

  print(f"Nilai akhir: {nilai_akhir:.2f}")
  print(f"Predikat: {predikat}")

main = main()
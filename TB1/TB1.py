import re

filename = "script.txt"

with open(filename, "r") as f:
    lebarinput = f.readline().rstrip().split()
    n = int(lebarinput[0])
    m = int(lebarinput[1])

    matriks = [f.readline().rstrip() for _ in range(n)]

output_decode = ""
for i in range(m):
    for j in range(n):
        try:
            output_decode += matriks[j][i]
        except IndexError:
            pass

pattern = r'(?<=[\w])[^\w]+(?=[\w])'
check = re.findall(pattern, output_decode)

for x in check:
    output_decode = output_decode.replace(x, ' ', 1)

# Ari Satrio Murdoko Andjalmo
# 41822010004

print("Output file : output.txt")
print("Hasil:", output_decode)

output_file = open("output.txt", "w")
output_file.write(output_decode)
output_file.close()

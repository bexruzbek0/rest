student = {
  "Samandar": 18,
  "Muzaffar": 19,
  "Xojiakbar": 16,
  "Islom": 20,
  "Asomiddin": 14,
  "Sobitjon": 17,
  "Shoxruh": 20
}

les1 = []
for k, v in student.items():
    if v>=18:
        les1.append(k)
print(",".join(les1))   

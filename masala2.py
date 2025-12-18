import os
os.system("cls")

login = {
  "jeymsBond" : "agent007",
  "tony_stark": "ironman101",
   "piterParker": "spider.12.12",
  "sherlok": "sher.l04"
  }

kirish = input("Logini kiriting: ")
parol = input("Parolni kiriting: ")
if kirish in login:
    if login[kirish] == parol:
        print("Xisobga kirdingiz")
    else:
        print("Parol notori")
else:
    print("hisob topilmadi")

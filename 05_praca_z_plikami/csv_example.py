#import csv

# slownik - przechowuje pary

#uzytkownicy = {}


# with open("../logi.csv") as csvfile:
#     reader = csv.reader(csvfile, delimiter=";")
#     for row in reader:
#         uzytkownicy[row[0]] = uzytkownicy.get()

"""
na podstawie logow okresl ile kazdy z uzytkownikow spedzil czasu w systemie
"""
import csv
import pandas as pd 
import matplotlib.pyplot as plt
# uzytkownicy = {}

# with open("../logi.csv") as csvfile:
#     reader = csv.reader(csvfile, delimiter=";")
#     for row in reader:
#         login = row[0]
#         czas = row[2]
#         uzytkownicy[login] = uzytkownicy.get(login,"")+ czas 

# print(uzytkownicy)

czas_ostatniego_zalogowania ={}
czas_przebywania_wsystemie ={}
with open("../logi.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
        login = row[0]
        akcja = row[1]
        czas = row[2]
        if akcja == "LOGIN":
            czas_ostatniego_zalogowania[login]=int(czas)
        if akcja == "LOGOUT":
            czas_przebywania_wsystemie[login]= (czas_przebywania_wsystemie.get(login,0) + 
                        int(czas)-czas_ostatniego_zalogowania[login])


wyniki = (sorted(czas_przebywania_wsystemie.items(), key=lambda x: x[1], reverse=True))

df = pd.DataFrame(wyniki)
df.columns = ["login","time"]
df.plot(kind="bar")
plt.show()
#print(df)

#df.to_excel("czas_w_systemie.xlsx", header=False, index=False)




# with open ("wyniki.csv","w", newline="") as outcsv:
#     writer = csv.writer(outcsv, delimiter=";")
#     # for row in wyniki:
#     #     writer.writerow(row)
#     writer.writerows(wyniki)

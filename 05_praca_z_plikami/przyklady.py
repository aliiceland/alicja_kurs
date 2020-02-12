"""
f = open ("c:text.txt") # przy takim zapisie pronujemy otworzyc plik ktorego nie ma
f.close()
"""

#f = open ("text.txt", "w") # "w" tworzy od razu plik wiec jest co otwierac
#f.close()
"""
f = open ("../text.txt")
print(f.read())
f.close()
"""
with open("test.txt","w") as f:
    f.write("deszczowy dzien")


# f = open ("../emails.txt")
# print(f.read())
# f.close()

# #context manager dba o zakmniecie pliku po wyjsciu

# with open("../text.txt") as f:
#     print(f.read())
# print(f)
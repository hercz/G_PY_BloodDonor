__author__ = 'herczkumihalybalazs'

id = 1

# file = open("./Data/Donor_Data.csv", "r+")
# lines = file.readlines()
# file.seek(0)
# for i in lines:
#     if i != id:
#         file.write(i)
# file.truncate()
# file.close()





file = open("./Data/Donor_Data.csv", "r")
lines = file.readlines()
file.close()

for i in lines:
    print(i)

file = open("./Data/Donor_Data.csv", "r+")

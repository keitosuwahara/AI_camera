import os 
import glob



dbs = [os.path.basename(file) for file in glob.glob("./database/*.db")]

for index, db in enumerate(dbs):
    print(dbs[index][:-3])
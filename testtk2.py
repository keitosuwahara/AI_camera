import os 
import glob



dbs = [os.path.basename(file) for file in glob.glob("./database/*.db")]
print(dbs)
for index, db in enumerate(dbs):
    print(dbs[index][:-3])
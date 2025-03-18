from fnmatch import fnmatch
for i in range(1203450670890 - 1203450670890 %206,1293459670899,206):
    if fnmatch(str(i), '12?345?67089?'):
        print(i,i//206)
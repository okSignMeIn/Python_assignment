import os
import shutil

path = "/home/shtlp_0039/Python_assignment"
file_and_dirs = os.listdir(path)
# print(file_and_dirs)
files = [f for f in file_and_dirs if os.path.isfile(f)]
# print(files)
dict={}
extensions = [f.split('.')[1] for f in files]
# print(extensions)
for ext in extensions:
    if os.path.exists(path+"/%s" %ext):
        pass
    else:
        os.mkdir(path+"/%s" %ext)
for f,e in zip(files,extensions):
    print(f)
    if e in f:
        if os.path.exists(path+"/%s" %(e+"/"+f)):
            pass
        else:
            source = path+"/%s" %f
            dest = path+"/%s" %(e+"/"+f)
            shutil.move(source,dest)
        
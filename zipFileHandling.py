import zipfile,os
os.chdir("/home/hasnat/Desktop/automate_boring_stuff/Chapter 9")
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
spamInfo=exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
exampleZip.extractall('example_folder')

# creating and adding to zip files
newZip = zipfile.ZipFile('new.zip','w')
newZip.write('delicious/spam.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
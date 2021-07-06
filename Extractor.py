# importing the "tarfile" module
import tarfile
  
# open file
file = tarfile.open('C:/Users/saidh/Downloads/lfw.tgz')
  
# extracting file
file.extractall('./Destination_FolderName')
  
file.close()

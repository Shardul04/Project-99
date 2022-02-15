import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
         for filename in files: 
             # construct the full local path 
              local_path = os.path.join(root, filename) 
              # construct the full Dropbox path 
              relative_path = os.path.relpath(local_path, file_from) 
              dropbox_path = os.path.join(file_to, relative_path)
              
               # upload the file 
              with open(local_path, 'rb') as f:
                   dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'iR730fH1lGUAAAAAAAAAAVyetIPlMRIapr0MjG2fA54sP3PMyiWHzjgiXL0XPftT'
    transferData = TransferData(access_token)

   # file_from = 'test.txt'
   # file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    file_from = input("Enter your file path: ")
    file_to = input("Enter the full path to upload to drop box: ")

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
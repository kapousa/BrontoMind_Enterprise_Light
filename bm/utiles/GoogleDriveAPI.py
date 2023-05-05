# import the required libraries
from __future__ import print_function

import io
import os.path
import os.path
import pickle
import shutil
from mimetypes import MimeTypes




class GoogleDriveAPI:
    global SCOPES

    # Define the scopes
    SCOPES = ['https://drive.google.com/drive/folders/0B64XAselCis_R0dmNW9jVXF5RE0?resourcekey=0-XmN5_nP23Wtt6n9Q0s5arQ&usp=sharing']

    def __init__(self):

        # Variable self.creds will
        # store the user access token.
        # If no valid token found
        # we will create one.
        self.creds = None


    def FileDownload(self, file_id, file_name):
        return ""

    def getFileList(N):

        return "result"


# # Get list of first 5 files or
# # folders from our Google Drive Storage
# result_dict = getFileList(5)
#
# # Extract the list from the dictionary
# file_list = result_dict.get('files')
#
# # Print every file's name
# for file in file_list:
#     print(file['name'])

# if __name__ == "__main__":
#     obj = GoogleDriveAPI()
#     i = int(input("Enter your choice:"
#                   "1 - Download file, 2- Upload File, 3- Exit.\n"))
#
#     if i == 1:
#         f_id = input("Enter file id: ")
#         f_name = input("Enter file name: ")
#         obj.FileDownload(f_id, f_name)
#
#     elif i == 2:
#         f_path = input("Enter full file path: ")
#         obj.FileUpload(f_path)
#
#     else:
#         exit()

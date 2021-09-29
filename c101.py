import dropbox
class TransferData : 
    def __init__(self,accessToken):
        self.accessToken = accessToken
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.accessToken)

        f = open(file_from,"rb")
        dbx.files_upload(f.read(), file_to)

def main():
    accessToken = 'jPrRu6r21jIAAAAAAAAAAe2Bjm3l2z0aMvOTmSEKpQ_kOi_-0fSnQS3AaKZk5m8_'
    transferData = TransferData(accessToken)
    file_from = input("enter the file path to transfer")
    file_to = input("enter the path to upload to dropbox")
    transferData.upload_file(file_from , file_to)
    print("file has been moved")

main()
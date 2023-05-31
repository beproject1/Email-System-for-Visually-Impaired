import imaplib
import csv

class ImapServerClass:
    
    def __init__(self):

        self.my_mail = None
        self.setUpImapServer()
        self.initiateLogin()
        
    
    def setUpImapServer(self):
        self.imap_url = 'imap.gmail.com'
        self.my_mail = imaplib.IMAP4_SSL(self.imap_url)

    def initiateLogin(self):
        with open("your_email_id_and_password.txt", mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.my_mail.login(row["email_id"], row["password"])

    def returnImapServer(self):
        return self.my_mail

if __name__ == "__main__":

    imap_obj = ImapServerClass()
    

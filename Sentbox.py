import imaplib
import email
import ImapServer
import AudioManager
import sys
import os

audio_input_handler = AudioManager.AudioInputHandler()
program_talkback = AudioManager.ProgramTalkback()


class CheckMailbox(ImapServer.ImapServerClass):

    def __init__(self):
        self.emails_in_the_form_of_lists_all = []
        self.normal_emails_all = []
        self.normal_emails_all_temp = []
        self.my_mail = ImapServer.ImapServerClass()
        self.my_mail = self.my_mail.returnImapServer()
        
        
    def createListContainingAllEmails(self):
        self.selectAppropriateMailbox()
        self.fetchAllEmailIdNumbers()
        self.generateRawEmailList(self.emails_in_the_form_of_lists_all)
        self.generateNormalEmailList(self.emails_in_the_form_of_lists_all, self.normal_emails_all)

   
        
    def checkMailboxForAllEmails(self):

        if(self.normal_emails_all == []):
                self.createListContainingAllEmails()
        
        for email_message in self.normal_emails_all:
                self.displayEmail(email_message)
                
    def checkEmailForRecipientAndSubject(self, particular_phrase_t):
        if(self.normal_emails_all == []):
                self.createListContainingAllEmails()

        self.normal_emails_all_temp = self.normal_emails_all
        
        for email_message in self.normal_emails_all_temp:
                
                if((particular_phrase_t.casefold() in email_message['from'].casefold()) or (particular_phrase_t.casefold() in email_message['subject'].casefold())):
                        self.displayEmail(email_message)
                        self.normal_emails_all_temp.remove(email_message)
                        
    def checkMailboxForParticularPhrase(self, particular_phrase):

        self.checkEmailForRecipientAndSubject(particular_phrase)
        #if(self.normal_emails_all == []):
        #        self.createListContainingAllEmails()
        
        for email_message in self.normal_emails_all_temp:
                for part in email_message.walk():    
                        if part.get_content_type() == 'text/plain':
                                if particular_phrase.casefold() in part.get_payload().casefold():
                                        self.displayEmail(email_message)
        self.normal_emails_all_temp = []
        
                                
    def selectAppropriateMailbox(self):
        self.my_mail.select('"[Gmail]/Sent Mail"')

    def fetchAllEmailIdNumbers(self):
        _, self.email_id_list = self.my_mail.search(None, "All")

    def generateRawEmailList(self, rawEmailList):
        for self.email_id_number in self.email_id_list[0].split():
            _, self.email_in_the_form_of_list = self.my_mail.fetch(self.email_id_number, "(RFC822)")
            rawEmailList.append(self.email_in_the_form_of_list)

    def generateNormalEmailList(self, rawEmailList, normalEmailList):
        for raw_email in rawEmailList[::-1]:
            for individual_component in raw_email:
                if(type(individual_component) is tuple):
                   normal_email = email.message_from_bytes(individual_component[1])
                   normalEmailList.append(normal_email)
                   
    def displayEmail(self, email_message):
        print("_________________________________________")
        print("From:", email_message['from'])
        print("Subject:", email_message['subject'])
        print("Body:")

        
        for part in email_message.walk():    
                if part.get_content_type() == 'text/plain':
                        print(part.get_payload())
                        program_talkback.speak("From: {0}".format(email_message['from']))
                        program_talkback.speak("Subject: {0}".format(email_message['subject']))
                        program_talkback.speak("Body: {0}".format(part.get_payload()))

        print("Do you want to continue to next email? Say one for yes and zero for no")
        program_talkback.speak("Do you want to continue to next email? Say one for yes and zero for no")
        print("Speak Now")
        program_talkback.speak("Speak Now")
        new_choice = audio_input_handler.startListening()
        program_talkback.speak(new_choice)
        print(new_choice)
        if(("1".casefold() in new_choice.casefold()) or ("one".casefold() in new_choice.casefold())):
            return
        else:
            print("Do you want to run the program again? Say one for yes and zero for no")
            program_talkback.speak("Do you want to run the program again? Say one for yes and zero for no")
            print("Speak Now")
            program_talkback.speak("Speak Now")
            user_choice = audio_input_handler.startListening()
            print(user_choice)
            program_talkback.speak(user_choice)
            if(("1".casefold() in user_choice.casefold()) or ("one".casefold() in user_choice.casefold())):
                os.system("cls")
                os.system("python " + r'"Voice Based Email.py"')
            else:
                os.system("cls")
                sys.exit()
        



if __name__ == "__main__":

    check_mailbox = CheckMailbox()
    #check_inbox.checkMailboxForAllEmails()
    check_mailbox.checkMailboxForParticularPhrase("Random")
    
    

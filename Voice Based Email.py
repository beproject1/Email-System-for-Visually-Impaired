import AudioManager
import Compose
import Inbox
import Sentbox
import Drafts
import Spam
import Thrash
import ImapServer
def input_receiver_user_credentials_for_sending_email(compose_mail):
        print("To whom do you want to send this Email?")
        program_talkback.speak("To whom do you want to send this Email?")
        print("Speak Now")
        program_talkback.speak("Speak Now")
        compose_mail.receiver = audio_input_handler.startListening()
        print(compose_mail.receiver)

        print("Speak the subject of the Email")
        program_talkback.speak("Speak the subject of the Email")
        print("Speak Now")
        program_talkback.speak("Speak Now")
        
        compose_mail.subject = audio_input_handler.startListening()
        print(compose_mail.subject)

        print("Speak the body of the Email")
        program_talkback.speak("Speak the Body of the Email")
        print("Speak Now")
        program_talkback.speak("Speak Now")
        compose_mail.body = audio_input_handler.startListening()
        print(compose_mail.body)
        
        compose_mail.sendEmail()
        
audio_input_handler = AudioManager.AudioInputHandler()
program_talkback = AudioManager.ProgramTalkback()

class mainInput:
        def __init__(self):
                self.compose_mail = ""
                self.check_inbox = ""
                self.check_spam = ""
                self.check_sentbox = ""
                self.check_thrash = ""
                self.check_drafts = ""
        def searchFunctionForMainProgram(self, mailbox_object):
                print("Speak the phrase you want to search")
                program_talkback.speak("Speak the phrase you want to search")
                phrase_to_be_searched = audio_input_handler.startListening()
                print(phrase_to_be_searched)
                mailbox_object.checkMailboxForParticularPhrase(phrase_to_be_searched)

                
##
##        def displaySeenEmails(self, mailbox_obj):
##
##                
##                # Search for all emails in the INBOX
##                response, message_ids = mailbox_obj.search(None, 'SEEN')
##
##                # Iterate over the message IDs and fetch the email content
##                for message_id in message_ids[0].split():
##
##                        # Fetch the email using its ID
##                        response, data = mailbox_obj.fetch(message_id, '(RFC822)')
##
##                        # Parse the email content using the email module
##                        email_message = email.message_from_bytes(data[0][1])
##
##                        # Print the email subject and sender
##                        print('From:', email_message['From'])
##                        print('Subject:', email_message['Subject'])
##                        
##
##                        # Print the email body
##                        for part in email_message.walk():
##                            if part.get_content_type() == 'text/plain':
##                                print(part.get_payload())
##                                program_talkback.speak("From: {0}".format(email_message['From']))
##                                program_talkback.speak("Subject: {0}".format(email_message['Subject']))
##                                program_talkback.speak("Body: {0}".format(part.get_payload()))
##                                break
                        
                                
        def beginMainProgram(self):
                
                print("What action do you want to perform?")
                program_talkback.speak("What action do you want to perform?")
                print("1. Compose Mail\n2. Check Inbox\n3. Check Sentbox \n4. Check Spam\n5. Check Trash\n6. Check Drafts\n7. Exit")
                program_talkback.speak("1. Compose Mail, 2. Check Inbox, 3. Check Sentbox, 4. Check Spam, 5. Check Trash, 6. Check Drafts, 7. Exit")
                print("Speak Now")
                program_talkback.speak("Speak Now")

                self.textSpokenByUser = audio_input_handler.startListening()

                print(self.textSpokenByUser)
                program_talkback.speak(self.textSpokenByUser)
                
                if(("one".casefold() in self.textSpokenByUser.casefold()) or ("1".casefold() in self.textSpokenByUser.casefold()) or ("compose".casefold() in self.textSpokenByUser.casefold()) or ("compose a mail".casefold() in self.textSpokenByUser.casefold()) or ("compose mail".casefold() in self.textSpokenByUser.casefold())):
                        self.compose_mail = Compose.ComposeMail()
                        input_receiver_user_credentials_for_sending_email(self.compose_mail)
                        

                elif(("2".casefold() in self.textSpokenByUser.casefold()) or ("two".casefold() in self.textSpokenByUser.casefold()) or ("second".casefold() in self.textSpokenByUser.casefold()) or ("to".casefold() in self.textSpokenByUser.casefold()) or ("tu".casefold() in self.textSpokenByUser.casefold())or ("inbox".casefold() in self.textSpokenByUser.casefold()) or ("check inbox".casefold() in self.textSpokenByUser.casefold()) or ("inbox mail".casefold() in self.textSpokenByUser.casefold())):
                        self.check_inbox = Inbox.CheckMailbox()
                        print("Do you want to display\n1. seen emails\n2. unseen emails\n3. recent emails\n4. Search an email")
                        program_talkback.speak("Do you want to display 1. seen mails, 2. unseen mails, 3. Recent 5 mails, 4. Search an email")
                        print("Speak Now")
                        program_talkback.speak("Speak Now")
                        user_choice = audio_input_handler.startListening()
                        print(user_choice)
                        program_talkback.speak(user_choice)
                        
                        if(("1".casefold() in user_choice.casefold()) or ("seen".casefold() in user_choice.casefold()) or ("seen mails".casefold() in user_choice.casefold()) or ("seen mail".casefold() in user_choice.casefold())):
                                self.check_inbox.checkMailboxForSeenEmails()
                        elif(("2".casefold() in user_choice.casefold()) or ("two".casefold() in user_choice.casefold()) or ("second".casefold() in user_choice.casefold()) or ("unseen".casefold() in user_choice.casefold()) or ("unseen mails".casefold() in user_choice.casefold()) or ("unseen mail".casefold() in user_choice.casefold())):   
                                self.check_inbox.checkMailboxForUnseenEmails()
                        elif(("3".casefold() in user_choice.casefold()) or ("third".casefold() in self.textSpokenByUser.casefold()) or ("recent".casefold() in user_choice.casefold())):
                                self.check_inbox.checkMailboxForAllEmails()
                        elif(("4".casefold() in user_choice.casefold()) or ("search".casefold() in user_choice.casefold()) or ("search mails".casefold() in user_choice.casefold()) or ("search mail".casefold() in user_choice.casefold())):
                                program_talkback.speak("Speak the phrase you want to search")
                                phrase = audio_input_handler.startListening()
                                self.check_inbox.checkMailboxForParticularPhrase(phrase)
                        
                elif(("3".casefold() in self.textSpokenByUser.casefold()) or ("3rd".casefold() in self.textSpokenByUser.casefold()) or ("third".casefold() in self.textSpokenByUser.casefold()) or ("sent".casefold() in self.textSpokenByUser.casefold()) or ("send".casefold() in self.textSpokenByUser.casefold()) or ("sandbox".casefold() in self.textSpokenByUser.casefold()) or ("sent mail".casefold() in self.textSpokenByUser.casefold()) or ("send mail".casefold() in self.textSpokenByUser.casefold())):
                        self.check_sentbox = Sentbox.CheckMailbox()
                        print("Do you want to\n1. display all mails\n2. search mail")
                        program_talkback.speak("Do you want to 1. display all mails, 2. search mail")
                        print("Speak Now")
                        program_talkback.speak("Speak Now")
                        user_choice = audio_input_handler.startListening()
                        print(user_choice)
                        program_talkback.speak(user_choice)
                        if(("1".casefold() in user_choice.casefold()) or ("one".casefold() in user_choice.casefold()) or ("all".casefold() in user_choice.casefold()) or ("first".casefold() in user_choice.casefold())):
                                self.check_sentbox.checkMailboxForAllEmails()
                        elif(("2".casefold() in user_choice.casefold()) or ("two".casefold() in user_choice.casefold()) or ("search".casefold() in user_choice.casefold()) or ("search mail".casefold() in user_choice.casefold()) or ("second".casefold() in user_choice.casefold())):
                                print("Speak the phrase you want to search")
                                program_talkback.speak("Speak the phrase you want to search")
                                phrase = audio_input_handler.startListening()
                                print(phrase)
                                program_talkback.speak(phrase)
                                self.check_sentbox.checkMailboxForParticularPhrase(phrase)
                        
                elif(("4".casefold() in self.textSpokenByUser.casefold()) or ("scam".casefold() in self.textSpokenByUser.casefold()) or ("fake".casefold() in self.textSpokenByUser.casefold()) or ("forth".casefold() in self.textSpokenByUser.casefold()) or ("four".casefold() in self.textSpokenByUser.casefold()) or ("spam".casefold() in self.textSpokenByUser.casefold()) or ("check spam".casefold() in self.textSpokenByUser.casefold()) or ("spam mail".casefold() in self.textSpokenByUser.casefold()) or ("check spam mails".casefold() in self.textSpokenByUser.casefold())):
                        self.check_spam = Spam.CheckMailbox()
                        print("Do you want to\n1. display all mails\n2. search mail")
                        program_talkback.speak("Do you want to 1. display all mails, 2. search mail")
                        print("Speak Now")
                        program_talkback.speak("Speak Now")
                        user_choice = audio_input_handler.startListening()
                        print(user_choice)
                        if(("1".casefold() in user_choice.casefold()) or ("one".casefold() in user_choice.casefold()) or ("all".casefold() in user_choice.casefold()) or ("first".casefold() in user_choice.casefold())):
                                self.check_spam.checkMailboxForAllEmails()
                        elif(("2".casefold() in user_choice.casefold()) or ("two".casefold() in user_choice.casefold()) or ("search".casefold() in user_choice.casefold()) or ("saerch mail".casefold() in user_choice.casefold()) or ("second".casefold() in user_choice.casefold())):
                                print("Speak the phrase you want to search")
                                program_talkback.speak("Speak the phrase you want to search")
                                phrase = audio_input_handler.startListening()
                                print(phrase)
                                program_talkback.speak(phrase)
                                self.check_spam.checkMailboxForParticularPhrase(phrase)
                        
                        
                elif(("5".casefold() in self.textSpokenByUser.casefold()) or ("five".casefold() in self.textSpokenByUser.casefold()) or ("delete".casefold() in self.textSpokenByUser.casefold()) or ("check deleted".casefold() in self.textSpokenByUser.casefold()) or ("deleted mail".casefold() in self.textSpokenByUser.casefold()) or ("check deleted mails".casefold() in self.textSpokenByUser.casefold()) or ("thrash".casefold() in self.textSpokenByUser.casefold())):
                        self.check_thrash = Thrash.CheckMailbox()
                        print("Do you want to\n1. display all mails\n2. search mail")
                        program_talkback.speak("Do you want to 1. display all mails, 2. search mail")
                        print("Speak Now")
                        program_talkback.speak("Speak Now")
                        user_choice = audio_input_handler.startListening()
                        print(user_choice)
                        program_talkback.speak(user_choice)
                        if(("1".casefold() in user_choice.casefold()) or ("one".casefold() in user_choice.casefold()) or ("all".casefold() in user_choice.casefold()) or ("first".casefold() in user_choice.casefold())):
                           
                                self.check_thrash.checkMailboxForAllEmails()
                        elif(("2".casefold() in user_choice.casefold()) or ("two".casefold() in user_choice.casefold()) or ("search".casefold() in user_choice.casefold()) or ("search mail".casefold() in user_choice.casefold()) or ("second".casefold() in user_choice.casefold())):
                         
                                print("Speak the phrase you want to search")
                                program_talkback.speak("Speak the phrase you want to search")
                                phrase = audio_input_handler.startListening()
                                print(phrase)
                                program_talkback.speak(phrase)
                                self.check_thrash.checkMailboxForParticularPhrase(phrase)
                        

                elif(("6".casefold() in self.textSpokenByUser.casefold()) or ("six".casefold() in self.textSpokenByUser.casefold()) or ("sex".casefold() in self.textSpokenByUser.casefold()) or ("drafts".casefold() in self.textSpokenByUser.casefold()) or ("check drafts".casefold() in self.textSpokenByUser.casefold()) or ("saved mails".casefold() in self.textSpokenByUser.casefold()) or ("check saved mails".casefold() in self.textSpokenByUser.casefold()) or ("saved".casefold() in self.textSpokenByUser.casefold()) or ("save".casefold() in self.textSpokenByUser.casefold())):
                        self.check_drafts = Drafts.CheckMailbox()
                        print("Do you want to\n1. display all mails\n2. search mail")
                        program_talkback.speak("Do you want to 1. display all mails, 2. search mail")
                        user_choice = audio_input_handler.startListening()
                        print(user_choice)
                        program_talkback.speak(user_choice)
                        if(("1".casefold() in user_choice.casefold()) or ("one".casefold() in user_choice.casefold()) or ("all".casefold() in user_choice.casefold()) or ("first".casefold() in user_choice.casefold())):
                           
                                self.check_drafts.checkMailboxForAllEmails()
                        elif(("2".casefold() in user_choice.casefold()) or ("two".casefold() in user_choice.casefold()) or ("search".casefold() in user_choice.casefold()) or ("search mail".casefold() in user_choice.casefold()) or ("second".casefold() in user_choice.casefold())):
                         
                                print("Speak the phrase you want to search")
                                program_talkback.speak("Speak the phrase you want to search")
                                phrase = audio_input_handler.startListening()
                                print(phrase)
                                program_talkback.speak(phrase)
                                self.check_drafts.checkMailboxForParticularPhrase(phrase)
                        
                elif(("7".casefold() in self.textSpokenByUser.casefold()) or ("seven".casefold() in self.textSpokenByUser.casefold()) or ("quit".casefold() in self.textSpokenByUser.casefold()) or ("exit".casefold() in self.textSpokenByUser.casefold())):
                        program_talkback.speak("Exiting Program")
                        print("Exiting Program")
                        exit
                        
                else:
                        program_talkback.speak("Couldn't recognize")
                        print("Couldn't recognize")
                        print("ERROR")
                
if __name__ == "__main__":

       obj = mainInput()
       obj.beginMainProgram()
       

       
        

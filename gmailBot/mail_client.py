import pythoncom
from win32com.client import DispatchWithEvents
import re
import telebot
from db_init import *

bot = telebot.TeleBot("6931652129:AAEjipnLIJI3t_bA3pezCnkxUCE52RbbqL0")

def start():
    # Event handler class for Outlook events
    class OutlookEventHandler(object):
        @staticmethod
        def OnNewMailEx(EntryIDCollection):
            for ID in EntryIDCollection.split(","):
                item = Outlook.Session.GetItemFromID(ID)
                # check item class, 43 = MailItem
                if item.Class == 43:
                    body = item.Body
                    lines = body.split("\n")
                    if(len(lines) < 3):
                        continue

                    from_str = lines[3]
                    from_mail_r = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', from_str)

                    if(from_mail_r == None):
                        continue
                    
                    from_mail = from_mail_r.group(0)

                    main_lines = "\n".join(lines[6:])

                    print("SENDER:", from_mail)
                    print("BODY:", main_lines)

                    res = get_user_by_email(from_mail)
                    print(res)
                    (user_id, _, _) = res

                    bot.send_message(user_id, 'You are admin of this group!', main_lines)

    Outlook = DispatchWithEvents("Outlook.Application", OutlookEventHandler)
    pythoncom.PumpMessages()

start()
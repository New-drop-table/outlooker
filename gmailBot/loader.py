import sqlite3

from gmail_class import GmailApi

con = sqlite3.connect("test.db", check_same_thread=False)

gmail_client = GmailApi()
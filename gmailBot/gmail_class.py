import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from auth_function import authenticate


class GmailApi:
    def __init__(self):
        # alternatively, we could pass credentials to constructor
        # to decouple the code.
        creds = authenticate()
        self.service = build("gmail", "v1", credentials=creds)

    def find_emails(self, sender: str):
        request = (
            self.service.users()
            .messages()
            .list(userId="me", q=f"from:{sender}", maxResults=200)
        )

        result = self._execute_request(request)
        try:
            messages = result["messages"]
            print(f"Retrieved messages matching the '{sender}' query: {messages}")
        except KeyError:
            print(f"No messages found for the sender '{sender}'")
            messages = []

        return messages

    def find_all_emails(self):
        request = (
            self.service.users()
            .messages()
            .list(userId="me", maxResults=10)
        )

        result = self._execute_request(request)
        try:
            messages = result["messages"]
        except KeyError:
            messages = []

        return messages


    def get_email(self, email_id):
        request = (
            self.service.users()
            .messages()
            .get(userId="me", id = email_id)
        )

        result = self._execute_request(request)
        # print(result)

        return result

    def send_email(self, to : str, subject : str, body_text : str):

        message = MIMEText(body_text)
        message['to'] = to
        message['subject'] = subject
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        request = (
            self.service.users()
            .messages()
            .send(userId="me", body = create_message)
        )

        result = self._execute_request(request)


    @staticmethod
    def _execute_request(request):
        try:
            return request.execute()
        except HttpError as e:
            print(f"An error occurred: {e}")
            raise RuntimeError(e)
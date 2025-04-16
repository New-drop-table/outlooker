import base64

from gmail_class import GmailApi

def parse_msg(msg):
    if msg.get("payload").get("body").get("data"):
        return base64.urlsafe_b64decode(msg.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")
    return msg.get("snippet")

def process_message(msg):
    email_data = msg["payload"]["headers"]
    for values in email_data:
        name = values["name"]
        if name == "From":
            from_name = values["value"]
            print(from_name)
            subject = [j["value"] for j in email_data if j["name"] == "Subject"]
            print(subject)

    # I added the below script.
    for p in msg["payload"]["parts"]:
        if p["mimeType"] in ["text/plain", "text/html"]:
            data = base64.urlsafe_b64decode(p["body"]["data"]).decode("utf-8")
            print(data)

def main():
    client = GmailApi()

    client.send_email("d23125128@mytudublin.ie", "Auth Code", "123")



if __name__ == "__main__":
    main()
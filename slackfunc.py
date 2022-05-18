import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def slack_post_msg():
    client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
    try:
        #oracle fetch code
        response = client.chat_postMessage(channel='testbot', text="Hi Eswar!")
        assert response["message"]["text"] == "Hi Eswar!"
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

def slack_post_file():
    client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
    try:
        filepath="C:\\Users\\L\\Downloads\\test_data.csv"
        print(filepath)
        fd=open(filepath,'r')
        print(fd.read())
        response = client.files_upload(channel='testbot',file=open(filepath,'rb'),filetype='csv',
                                       title='Sample',filename='test_data.csv',as_user=True)
        print("fileupload response: ",response)
        assert response["ok"]
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
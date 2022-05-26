import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import re
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

@app.event("app_mention")
def event_test(say):
    say("Hi there!")

# Listens for messages containing "knock knock" and responds with an italicized "who's there?"
@app.message("knock knock")
def ask_who(message, say):
    response = client.chat_postMessage(channel='testbot', text="_Who's there?_")
    assert response["message"]["text"] == "_Who's there?_"
    say("_Who's there?_")

@app.message(re.compile("(hi|hello|hey)"))
def say_hello_regex(say, context):
    # regular expression matches are inside of context.matches
    greeting = context['matches'][0]
    say(f"{greeting}, how are you?")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

from sanic import Sanic
from sanic.response import json
from slackfunc import slack_post_msg,slack_post_file
from slack_sdk.errors import SlackApiError

app = Sanic(name="slackapp")

@app.route('/',methods=['POST'])
async def test(request):
    try:
        payload=request.json
        print(payload)
        if "challenge" in payload:
            challenge=payload['challenge']
        else:
            challenge="test"
        slack_post_msg()
        slack_post_file()
        return json({"challenge":challenge})
    except SlackApiError as e:
        return json({'message': f"Failed due to {e.response['error']}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
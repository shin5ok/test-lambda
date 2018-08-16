import json
import datetime
import os


def handler(event, context):
    data = {
        'ip': os.environ.get('REMOTE_ADDR', "None"),
        'output': 'Hello World!!',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

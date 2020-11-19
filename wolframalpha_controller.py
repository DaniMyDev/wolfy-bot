import wolframalpha
import os
from os import environ

wolframalpha_api_key = environ['WOLFRAM_API_KEY']
wfclient = wolframalpha.Client(wolframalpha_api_key)

def fetchWolframAlpha(query):
    res = wfclient.query(query)
    answer = next(res.results)
    message = answer.title + '\n'
    if answer.numsubpods >= 2:
        message += answer['subpod'][0]['img']['@src'] + '\n'
        message += answer['subpod'][0]['img']['@alt']
    else:
        message += answer['subpod']['img']['@src'] + '\n'
        message += answer['subpod']['img']['@alt']

    return message

import gpt4free
from gpt4free import Provider
import logging

a = input()


def GPT_free(user):
    logging.basicConfig(level=logging.DEBUG)

    # usage You
    response = bytes(
        gpt4free.Completion.create(Provider.You, prompt=user), "utf-8").decode('unicode-escape')
    print(response)


GPT_free(a)
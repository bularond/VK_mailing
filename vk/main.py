import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import random
import requests

token = "ce86a9ff70cba8689dc71626f03cc77b7fcc5d6db40bd98e77519194c81deebd12d3defca65e8cd17c6c7"

vk_session = vk_api.VkApi(token=token)

vk_session._auth_token()
vk = vk_session.get_api()
longpoll = vk_api.longpoll.VkLongPoll(vk_session)

print("Server started")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            for id in open("user_list.txt", 'r'):
                vk_session.method('messages.send', {'user_id': int(id), 'forward_messages': event.message_id, 'random_id': random()})

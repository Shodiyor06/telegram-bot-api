from time import sleep
import requests
from settings import TOKEN

BASE_URL = f'https://api.telegram.org/bot{TOKEN}'


def get_updates(offset: int | None):
    params = {
        'offset': offset
    }
    getupdates_url = f'{BASE_URL}/getUpdates'
    response = requests.get(getupdates_url, params=params)

    return response.json()["result"]


def send_message(chat_id: int, text: str):
    params = {
        'chat_id': chat_id,
        'text': text
    }

    sendmessage_url = f'{BASE_URL}/sendMessage'
    requests.get(sendmessage_url, params=params)


def send_contact(chat_id: int, first_name: str, phone_number: str):
    params = {
        'chat_id': chat_id,
        'first_name': first_name,
        'phone_number': phone_number,
    }

    sendmessage_url = f'{BASE_URL}/sendContact'
    requests.get(sendmessage_url, params=params)


def send_photo(chat_id: int, photo: str):
    params = {
        'chat_id': chat_id,
        'photo': photo,
    }

    sendmessage_url = f'{BASE_URL}/sendPhoto'
    requests.get(sendmessage_url, params=params)


def setn_audio(chat_id: int, audio: None):
    params = {
        'chat_id': chat_id,
        'audio': audio,
    }

    sendmessage_url = f'{BASE_URL}/sendAudio'
    requests.get(sendmessage_url, params=params)


def send_documents(chat_id: int, document: None):
    params = {
        'chat_id': chat_id,
        'document': document,
    }

    sendmessage_url = f'{BASE_URL}/sendDocument'
    requests.get(sendmessage_url, params=params)


def send_video(chat_id: int, video: None):
    params = {
        'chat_id': chat_id,
        'video': video,
    }

    sendmessage_url = f'{BASE_URL}/sendVideo'
    requests.get(sendmessage_url, params=params)


def send_animation(chat_id: int, animation: None):
    params = {
        'chat_id': chat_id,
        'animation': animation,
    }

    sendmessage_url = f'{BASE_URL}/sendAnimation'
    requests.get(sendmessage_url, params=params)

def send_voice(chat_id: int, voice: None):
    params = {
        'chat_id': chat_id,
        'voice': voice,
    }

    sendmessage_url = f'{BASE_URL}/sendVoice'
    requests.get(sendmessage_url, params=params)

import requests

BASE_URL = "https://api.telegram.org/bot<YOUR_TOKEN>"

def send_video_note(chat_id: int, video_note: None):
    params = {
        'chat_id': chat_id,
        'video_note': video_note,
    }
    sendmessage_url = f'{BASE_URL}/sendVideoNote'
    requests.get(sendmessage_url, params=params)

def send_paid_media(chat_id: int, media: None):
    params = {
        'chat_id': chat_id,
        'media': media,
    }
    sendmessage_url = f'{BASE_URL}/sendPaidMedia'
    requests.get(sendmessage_url, params=params)

def send_media_group(chat_id: int, media: None):
    params = {
        'chat_id': chat_id,
        'media': media,
    }
    sendmessage_url = f'{BASE_URL}/sendMediaGroup'
    requests.get(sendmessage_url, params=params)

def send_location(chat_id: int, latitude: float, longitude: float):
    params = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude,
    }
    sendmessage_url = f'{BASE_URL}/sendLocation'
    requests.get(sendmessage_url, params=params)

def send_venue(chat_id: int, latitude: float, longitude: float, title: str, address: str):
    params = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude,
        'title': title,
        'address': address,
    }
    sendmessage_url = f'{BASE_URL}/sendVenue'
    requests.get(sendmessage_url, params=params)


def send_poll(chat_id: int, question: str, options: list):
    params = {
        'chat_id': chat_id,
        'question': question,
        'options': options,
    }
    sendmessage_url = f'{BASE_URL}/sendPoll'
    requests.get(sendmessage_url, params=params)

def send_checklist(chat_id: int, checklist: list):
    params = {
        'chat_id': chat_id,
        'checklist': checklist,
    }
    sendmessage_url = f'{BASE_URL}/sendChecklist'
    requests.get(sendmessage_url, params=params)

def send_dice(chat_id: int):
    params = {
        'chat_id': chat_id,
    }
    sendmessage_url = f'{BASE_URL}/sendDice'
    requests.get(sendmessage_url, params=params)

def send_chat_action(chat_id: int, action: str):
    params = {
        'chat_id': chat_id,
        'action': action,
    }
    sendmessage_url = f'{BASE_URL}/sendChatAction'
    requests.get(sendmessage_url, params=params)


def updater(token: str):

    offset = None

    while True:

        updates = get_updates(offset)

        for update in updates:
            
            if 'message' in update:
                message = update['message']
                user = update['message']['from']

                if 'text' in message:
                    text = message['text']
                    send_message(user['id'], text)
                elif 'contact' in message:
                    contact = message['contact']
                    send_contact(user['id'], contact['first_name'], contact['phone_number'])
                elif 'photo' in message:
                    photo = message['photo'][0]
                    send_photo(user['id'], photo['file_id'])

                elif 'audio' in message:
                    audio = message['audio']
                    setn_audio(user['id'], audio['file_id'])

                elif 'document' in message:
                    document = message['document']
                    send_documents(user['id'], document['file_id'])

                elif 'video' in message:
                    video = message['video']
                    send_video(user['id'], video['file_id'])

                elif 'animation' in message:
                    animation = message['animation']
                    send_animation(user['id'], animation['file_id'])
            offset = update['update_id'] + 1

        sleep(1)

if __name__ == '__main__':
    updater(TOKEN)

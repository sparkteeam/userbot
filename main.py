#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json, os
from time import sleep
import sys
import re
import urllib
import methods as bot
reload(sys)
sys.setdefaultencoding("utf-8")
"""
handler message              _____'_____
start & copy right negative / super team\ MIT
                           |______'______|
"""
def run ():
    last_update = 0
    while True:
        get_updates = bot.getUpdates()
        for update in get_updates['result']:
            if last_update < update['update_id']:
                last_update = update['update_id']
                if 'message' in update or 'text' in update:
                    try:
                        chat_id = update['message']['chat']['id']
                        text = update['message']['text']
                        message = update['message']
                        command = text
                        if(command == '/start' or command == '/help'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'typing')
                            key = json.dumps(
                            {'inline_keyboard':[[
                            {'text':'Developer 👓','url':'https://telegram.me/helpsudo_tv'},
                            {'text':'team 🔌','url':'https://telegram.me/superspark'}
                            ],
                            [
                            {'text':'Your Info 🕶','url':'https://telegram.me/userinfobot'}
                            ],
                            [
                            {'text':'my dev','url':'https://telegram.me/m_1_h'}
                            ]
                            ]
                            })
                            bot.send_msg(chat_id,'<b>help sudo Development</b>\ncommands : \n/about\n/info',reply_markup=key)
                        if(command == '/frends' or command == '/team'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'typing')
                            key = json.dumps(
                            {'inline_keyboard':[[
                            {'text':'المعلم','url':'https://telegram.me/m_1_h'},
                            {'text':'محمد','url':'https://telegram.me/'}
                            ],
                            [
                            {'text':'كاسبر','url':'https://telegram.me/kasper_dev'}
                            ],
                            [
                            {'text':'حمادة','url':'https://telegram.me/HI_DEBYE'}
                            ]
                            ]
                            })
                            bot.send_msg(chat_id,'<b>this is my frends</b>',reply_markup=key)
                        if(command == '/time'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'typing')
                            time = urllib.urlopen('http://api.gpmod.ir/time/').read()
                            data = json.loads(time)
                            en = data['ENtime']
                            msgg = '<b>Time iraq :</b> {}'.format(en)
                            bot.send_msg(chat_id,msgg,reply_to_message_id=update['message']['message_id'])
                        if(command == '/about'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'upload_photo')
                            markup = json.dumps({
                            'inline_keyboard':[
                            [
                            {'text':'👇 helpsudo_tv 👇','callback_data':'1'}
                            ],
                            [
                            {'text':'Developer 🕶','url':'https://telegram.me/superspark'},
                            {'text':'Channel','url':'https://telegram.me/helpsudo_tv'}
                            ]
                            ]
                            })
                            bot.send_photo(chat_id,open('photo_2016-10-14_17-31-55.jpg'),caption='ch @helpsudo_tv',reply_markup=markup)
                        if(command == '/info' or command == '/start info'):
                            bot.getUpdates(last_update+1)
                            bot.send_action(chat_id,'typing')
                            user_id = update['message']['from']['id']
                            username = update['message']['from']['username']
                            s = bot.getUserProfilePhotos(update['message']['from']['id'])
                            markup = json.dumps(
                            {
                            'inline_keyboard':[
                            [
                            {'text':'{}'.format(username),'url':'https://telegram.me/{}'.format(username)}
                            ]
                            ]
                            }
                            )
                            bot.send_photo_file_id(chat_id,photo=s['result']['photos'][0][2]['file_id'],caption='🔺- ID : {}\n🔺- Username : @{}\n🔺- ch :  @helpsudo_tv'.format(user_id,username),reply_markup=markup)
                        if(command == '/type'):
                            if(update['message']['reply_to_message']['entities'][0]['type']):
                                msg = update['message']['reply_to_message']['entities'][0]['type']
                                bot.send_msg(chat_id,'<b>{}</b>'.format(msg))
                    except KeyError:
                        print 'error'

run()

#البوت قيد التطوير ماحاجة تغير الحقوق مو جاهل
#⚠️Sudo Source : @m_1_h
#🚭Channel 1 : @helpsudo_tv
#🌐Channel 2 : @dev_kasper
#🎦Channel 3 : @superspark
#🛄Channel 4 : @action_ch

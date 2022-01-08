import logging
import os
from datetime import datetime, timedelta

import telegram
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

import psycopg2

from telegram import *

TOKEN = os.getenv('TOKEN')

from telegram.ext import *
import Responses as r
import re


print('Bot started')

victim = "semak status"
about = "tujuan pkob"

def isValidIC(ic_no):
    regex = "(([[0-9]{2})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01]))([0-9]{2})([0-9]{4})";
    p = re.compile(regex)
    if (ic_no == ''):
        return False;
    m = re.match(p, ic_no)
    if m is None:
        return False
    else:
        return True

def isValidPhone(phone_no):
    regex = "[0-9]";
    p = re.compile(regex)
    if (phone_no == ''):
        return False;
    m = re.match(p, phone_no)
    if m is None:
        return False
    else:
        return True

def help_command (update, context) :
         update.message.reply_text(f"""Hi {update['message']['chat']['first_name']}, below actions might be helping you:\n\n1. Enter /start to start the bot\n2. Please make sure you are inputing the required information and format\n3. Select the above function to continue bot service. """)


def start(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(victim)], [KeyboardButton(about)]]
    update.message.reply_text(
        f"""Hi {update['message']['chat']['first_name']}, Selamat datang ke PKOB HelloWorld Bot.\nAnda boleh dapatkan maklumat melalui pilihan yang disediakan:\n\n1.Masukkan *"semak status"* untuk menyemak status permohonan. \n\n2.Masukkan *"tujuan pkob"* untuk mengetahui maksud Pusat Kawalan Operasi Bencana (PKOB). """, reply_markup=ReplyKeyboardMarkup(buttons), parse_mode=telegram.ParseMode.MARKDOWN)

def daftar_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""Hi {update['message']['chat']['first_name']},anda boleh daftar di laman web berikut:\nhttps://pkobsystemhelloworld.herokuapp.com/pkob/request/""")

def semak_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""Hi {update['message']['chat']['first_name']},sila masukkan nombor ic and nombor telefon anda dengan format berikut:\nExample:990506106144-0123324567""")

def handle_message(update: Update, context: CallbackContext):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)
    update.message.reply_text(response)

    ic_no, phone_no = text.split("-")

    if isValidIC(ic_no) and isValidPhone(phone_no):
        conn = psycopg2.connect("postgres://bxuslnuwrasaoh:8122a2b9eaba94ec6b190c3166df75127e1e84049ce88c3fb9d8b2c22e64eaa7@ec2-35-169-119-56.compute-1.amazonaws.com:5432/d6m5mc61mh1dfj")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM \"App_PKOB_receive\" WHERE ic_no = '{}' and \"phone_no\" = '{}'".format(ic_no,phone_no))
        conn.commit()
        result = cursor.fetchall()
        print(result)

        for x in result:
            birthday = str(x[4])[:6]
            date_time_obj = datetime.strptime(birthday, '%y%m%d')
            if date_time_obj > datetime.now():
                date_time_obj -= timedelta(weeks=5124, days=2)
            age = datetime.now() - date_time_obj
            ageYears = int(age.days / 365)

            update.message.reply_text(
                         f"""Hi {update['message']['chat']['first_name']}, berikut adalah maklumat anda: \n \n*Nama:* {str(x[2])} \n*Umur:* {str(ageYears)} \n*No. Kad Pengenalan:* {str(x[4])} \n*No. Telefon:* {str(x[3])} \n*Status:* Bantuan Telah Diterima""", parse_mode=telegram.ParseMode.MARKDOWN)


        cursor.close()

    if result ==[]:
        conn = psycopg2.connect("postgres://bxuslnuwrasaoh:8122a2b9eaba94ec6b190c3166df75127e1e84049ce88c3fb9d8b2c22e64eaa7@ec2-35-169-119-56.compute-1.amazonaws.com:5432/d6m5mc61mh1dfj")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM \"App_PKOB_victim\" WHERE ic_no = '{}' and \"phone_no\" = '{}'".format(ic_no,phone_no))
        conn.commit()
        result = cursor.fetchall()
        print(result)

        for x in result:
            birthday = str(x[4])[:6]
            date_time_obj = datetime.strptime(birthday, '%y%m%d')
            if date_time_obj > datetime.now():
                date_time_obj -= timedelta(weeks=5124, days=2)
            age = datetime.now() - date_time_obj
            ageYears = int(age.days / 365)

            update.message.reply_text(
                         f"""Hi {update['message']['chat']['first_name']}, berikut adalah maklumat anda: \n \n*Nama:* {str(x[2])} \n*Umur:* {str(ageYears)} \n*No. Kad Pengenalan:* {str(x[4])} \n*No. Telefon:* {str(x[3])} \n*Status:* Pendaftaran Teleh Diterima""", parse_mode=telegram.ParseMode.MARKDOWN)

    if result ==[]:
        conn = psycopg2.connect("postgres://bxuslnuwrasaoh:8122a2b9eaba94ec6b190c3166df75127e1e84049ce88c3fb9d8b2c22e64eaa7@ec2-35-169-119-56.compute-1.amazonaws.com:5432/d6m5mc61mh1dfj")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM \"App_PKOB_request\" WHERE ic_no = '{}' and \"phone_no\" = '{}'".format(ic_no,phone_no))
        conn.commit()
        result = cursor.fetchall()
        print(result)

        for x in result:
            birthday = str(x[4])[:6]
            date_time_obj = datetime.strptime(birthday, '%y%m%d')
            if date_time_obj > datetime.now():
                date_time_obj -= timedelta(weeks=5124, days=2)
            age = datetime.now() - date_time_obj
            ageYears = int(age.days / 365)

            update.message.reply_text(
                         f"""Hi {update['message']['chat']['first_name']}, berikut adalah maklumat anda: \n \n*Nama:* {str(x[2])} \n*Umur:* {str(ageYears)} \n*No. Kad Pengenalan:* {str(x[4])} \n*No. Telefon:* {str(x[3])} \n*Status:* Pendaftaran Sedang Diproses""", parse_mode=telegram.ParseMode.MARKDOWN)

    if result ==[]:
        conn = psycopg2.connect("postgres://bxuslnuwrasaoh:8122a2b9eaba94ec6b190c3166df75127e1e84049ce88c3fb9d8b2c22e64eaa7@ec2-35-169-119-56.compute-1.amazonaws.com:5432/d6m5mc61mh1dfj")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM \"App_PKOB_decline\" WHERE ic_no = '{}' and \"phone_no\" = '{}'".format(ic_no,phone_no))
        conn.commit()
        result = cursor.fetchall()
        print(result)

        for x in result:
            birthday = str(x[4])[:6]
            date_time_obj = datetime.strptime(birthday, '%y%m%d')
            if date_time_obj > datetime.now():
                date_time_obj -= timedelta(weeks=5124, days=2)
            age = datetime.now() - date_time_obj
            ageYears = int(age.days / 365)

            update.message.reply_text(
                         f"""Hi {update['message']['chat']['first_name']}, berikut adalah maklumat anda: \n \n*Nama:* {str(x[2])} \n*Umur:* {str(ageYears)} \n*No. Kad Pengenalan:* {str(x[4])} \n*No. Telefon:* {str(x[3])} \n*Status:* Pendaftaran Telah Ditolak""", parse_mode=telegram.ParseMode.MARKDOWN)
    if result ==[]:
        update.message.reply_text(
            f"""Hi {update['message']['chat']['first_name']}, maklumat anda tidak didapati, anda boleh daftarkan bantuan mangsa di laman web berikut:\n\nhttps://pkobsystemhelloworld.herokuapp.com/pkob/request/""")

if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("help", help_command)),
    dp.add_handler(CommandHandler("daftar", daftar_command)),
    dp.add_handler(CommandHandler("semak", semak_command)),
    dp.add_handler(CommandHandler("start", start)),

    dp.add_handler(MessageHandler(Filters.text, handle_message))


    updater.start_polling(1.0)
    updater.idle()

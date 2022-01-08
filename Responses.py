import re


def isValidIC(ic_no):
    regex = "(([[0-9]{2})(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01]))([0-9]{2})([0-9]{4})-*[0-9]";
    p = re.compile(regex)
    if (ic_no == ''):
        return False;
    m = re.match(p, ic_no)
    if m is None:
        return False
    else:
        return True


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if "semak status" in input_text:
            message =f"""Sila anda masukkan nombor Kad Pengenalan and nombor Telefon anda dengan format berikut:\n\nContoh: 990506106144-0123324567"""
            return message

    if "tujuan pkob" in input_text:
            message ="Pusat Kawalan Operasi Bencana (PKOB) dibangunkan untuk mangsa yang mengalami bencana banjir di kampung Mukim Bujang Merbok, Kedah, yang menghadapi masalah seperti kerosakan harta benda atau kemerosotan keadaan kesihatan. \n\nPengguna sistem termasuk mangsa banjir yang boleh membuat permohonan bantuan material atau kewangan untuk mendapatkan barangan atau pembiayaan melalui sistem web PKOB dan Penghulu Kampung yang menguruskan senarai nama dan kebajikan pengedaran melalui sistem tersebut."
            return message

    if"-"in input_text:
       if isValidIC(user_message):
        return "Kami sedang mencari maklumat anda, sila tunggu dan terima kasih."

    return "PKOB_HelloWorld_Bot tidak faham mesej anda, sila masukkan mesej dengan mengikuti format yang ditetapkan.\n\nAtau anda boleh masukkan /start untuk aktif semula PKOB_HelloWorld_Bot"
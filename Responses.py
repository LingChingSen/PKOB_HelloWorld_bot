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

    if "pendaftaran bantuan mangsa" in input_text:
            message =f"""Pendaftaran bantuan mangsa perlu dilaksanakan melalui laman web kita.\nAnda boleh daftar di laman web berikut:\nhttps://pkobsystemhelloworld.herokuapp.com/pkob/request/"""
            return message

    if "semakkan status permohonan" in input_text:
            message =f"""Sila anda masukkan nombor KadPengenalan and nombor Telefon anda dengan format berikut:\nExample:990506106144-0123324567"""
            return message

    if "mengetahukan tujuan pkob" in input_text:
            message ="Pusat Kawalan Operasi Bencana (PKOB) dibangunkan untuk mangsa yang mengalami bencana banjir di kampung Mukim Bujang Merbok, Kedah, yang menghadapi masalah seperti kerosakan harta benda atau kemerosotan keadaan kesihatan. Pengguna sistem termasuk mangsa banjir yang boleh membuat permohonan bantuan material atau kewangan untuk mendapatkan barangan atau pembiayaan melalui sistem web PKOB dan Penghulu Kampung yang menguruskan senarai nama dan kebajikan pengedaran melalui sistem tersebut."
            return message

    if"-"in input_text:
       if isValidIC(user_message):
        return "Kami sedang mencari maklumat anda, sila tunggu dan terima kasih."

    return "Penyelamat Bencana Bot menghadapi kesilapan!\n\nSila masukkan /start untuk aktif semula PKOB Bot"
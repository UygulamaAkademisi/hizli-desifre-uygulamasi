import ses_tanima_modulu as r

if r.transcribe():
    print("Sesiniz işlenmeye başlıyor. Lütfen bekleyiniz")
    r.finish_recognize_info()
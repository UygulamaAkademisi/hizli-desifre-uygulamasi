import speech_recognition as sr

def transcribe(audio_file="kayit.wav"):
    r = sr.Recognizer()
    file = sr.AudioFile(audio_file)
    with file as source:
        r.adjust_for_ambient_noise(source)
        audio =  r.record(source)
        result = r.recognize_google(audio,language='tr')
        return result    



def finish_recognize_info():
    f = open("cevirilmis-metin.txt","w")
    convert_process_audio_from_text = transcribe("kayit.wav") 
    if convert_process_audio_from_text:
        #print("Ses işleme başladı")
        print(convert_process_audio_from_text,file=f)    
        print("İşlem tamamlandı. Çıkmak için enter tuşuna basınız.")
        input()
    else:
        Print("Sesiniz işlenemedi")




if __name__ == '__main__':
    transcribe("kayit.wav")
    finish_recognize_info()    
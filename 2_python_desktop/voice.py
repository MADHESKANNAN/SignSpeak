import threading, tempfile, os, uuid, sys

on_error = None          # main.py sets this to show errors on screen
_lock = threading.Lock() # one sound at a time
_stop = threading.Event()

def _err(msg):
    print("voice error:", msg)
    if on_error:
        try: on_error(msg)
        except Exception: pass

def speak(text, lang="en"):
    text = (text or "").strip()
    if text:
        threading.Thread(target=_speak, args=(text, lang), daemon=True).start()

# ---------- play an mp3 file ----------
def _play_mp3(path):
    if sys.platform.startswith("win"):               # Windows: built-in MCI, no extra install needed
        import ctypes
        mci = ctypes.windll.winmm.mciSendStringW
        mci("close ssvoice", None, 0, 0)
        if mci(f'open "{path}" type mpegvideo alias ssvoice', None, 0, 0) != 0:
            raise RuntimeError("Windows could not open the audio file")
        mci("play ssvoice wait", None, 0, 0)
        mci("close ssvoice", None, 0, 0)
    else:                                            # Linux / Mac
        import pygame, time
        if not pygame.mixer.get_init(): pygame.mixer.init()
        pygame.mixer.music.load(path); pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): time.sleep(0.1)

def _speak(text, lang):
    with _lock:
        f = None
        try:
            if lang == "ta":                          # Tamil voice (Google TTS - needs internet)
                from gtts import gTTS
                f = os.path.join(tempfile.gettempdir(), f"ss_{uuid.uuid4().hex}.mp3")
                gTTS(text, lang="ta").save(f)
                _play_mp3(f)
            else:                                     # English voice (offline)
                import pyttsx3
                e = pyttsx3.init(); e.say(text); e.runAndWait(); e.stop()
        except Exception as ex:
            msg = str(ex) or ex.__class__.__name__
            if lang == "ta" and ("gTTS" in msg or "Failed to connect" in msg or "Connection" in msg or "HTTP" in msg or "404" in msg or "429" in msg):
                msg = "Tamil voice needs INTERNET. (" + msg[:80] + ")"
            elif lang == "ta" and isinstance(ex, ImportError):
                msg = "Run:  pip install gTTS   (then restart)"
            _err(msg)
        finally:
            if f:
                try: os.remove(f)
                except Exception: pass

def listen(lang, callback):
    """Mic -> text in a thread. callback(text, error)"""
    def run():
        try:
            import speech_recognition as sr
            r = sr.Recognizer()
            with sr.Microphone() as src:
                r.adjust_for_ambient_noise(src, 0.5)
                audio = r.listen(src, timeout=6, phrase_time_limit=12)
            callback(r.recognize_google(audio, language="ta-IN" if lang == "ta" else "en-US"), None)
        except Exception as ex:
            callback(None, str(ex) or "Could not understand")
    threading.Thread(target=run, daemon=True).start()

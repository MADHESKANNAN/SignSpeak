<div align="center">

<img src="1_web_pwa_app/icon-512.png" width="120" alt="SignSpeak logo">

# SignSpeak · சைகை

**Real-time sign-language & expression translator with Tamil + English voice.**
Camera sees your hands and face → SignSpeak types the word → and speaks it out loud.

![Platform](https://img.shields.io/badge/platform-Web%20%7C%20Android%20%7C%20Windows-68ebff)
![Python](https://img.shields.io/badge/python-3.11-c55fff)
![MediaPipe](https://img.shields.io/badge/AI-MediaPipe-0a1030)
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

## ✨ Features

| | |
|---|---|
| 🖐️ **One-hand signs** | Hello, Yes, Good, Bad, Peace, I love you, Wait, OK, Call me, Three … |
| 🙌 **Two-hand signs** | Thank you (palms together), Together (two fists touching) |
| 🙂 **Face expressions** | Happy, Surprised, Sleepy |
| ➕ **Teach your own** | Record any one-hand sign, two-hand sign or face expression in 5 seconds |
| 🔊 **Tamil + English voice** | Speaks recognised words aloud (auto-speak or tap Speak) |
| 🎤 **Voice → Text** | Speak in Tamil/English and it is typed in the notepad (for two-way talking) |
| 📝 **Notepad** | Build sentences, undo, copy, save as `.txt` |
| 📦 **Export / Import** | Share your custom signs as a `.json` file |
| 🔒 **Private** | Camera is processed **on your device only**. Nothing is uploaded. |
| 📴 **Offline** | After first load the web app works offline (Tamil online voice needs internet) |

---

## 📁 Project structure

```
SignSpeak_Complete/
├── 1_web_pwa_app/        Website + installable PWA (+ Android / Windows wrapper)
│   ├── index.html        Whole app (UI + AI logic)
│   ├── sw.js             Service worker (offline cache)
│   ├── manifest.webmanifest
│   ├── icon-192.png / icon-512.png
│   ├── main.js           Electron entry (optional .exe build)
│   ├── capacitor.config.json   Android wrapper config
│   └── package.json
├── 2_python_desktop/     Python desktop software
│   ├── main.py           GUI (CustomTkinter)
│   ├── engine.py         Hand / face / two-hand recognition
│   ├── voice.py          Text-to-speech + speech-to-text
│   ├── requirements.txt
│   ├── run.bat / build_exe.bat
│   └── assets/, icon.ico
└── README_ALL.md         Short deployment notes
```

---

## 🚀 Quick start

### Option 1 · Web / PWA (easiest)

1. Go to <https://app.netlify.com/drop>
2. Drag the **`1_web_pwa_app`** folder into the page.
3. Open the https link → tap **Start Camera**.
4. On phone/PC: browser menu → **Install app**.

> Camera and microphone need **https** (or `localhost`). Opening `index.html` by double-click will not work.

Run locally:
```bash
cd 1_web_pwa_app
python -m http.server 8000
# open http://localhost:8000
```

### Option 2 · Python desktop (Windows / Linux / Mac)

Requires **Python 3.11** (tick *Add to PATH* on Windows).

```bash
cd 2_python_desktop
pip install -r requirements.txt
python main.py
```

Build a Windows `.exe`: double-click **`build_exe.bat`** → `dist/SignSpeak/SignSpeak.exe`

### Option 3 · Android app

**Easiest (PWABuilder):** open <https://pwabuilder.com> → paste your Netlify link → *Package for stores* → *Android* → download `.aab` + signing key (keep it safe).
Test the `.apk` on your phone first, then upload the `.aab` to Google Play Console.

**Capacitor (Android Studio):**
```bash
cd 1_web_pwa_app
mkdir www && cp index.html sw.js manifest.webmanifest icon-*.png www/
npm i @capacitor/core @capacitor/cli @capacitor/android
npx cap add android
npx cap open android
```

### Option 4 · Windows app from the web version

- Easiest: Chrome/Edge → open your link → **Install** (microphone works).
- Electron `.exe`: `cd 1_web_pwa_app && npm install && npm run build` → `dist/`
  *(microphone does not work inside Electron – use the PWA if you need Voice→Text)*

---

## 🧭 How to use

1. **Start the camera.** Show a sign and **hold it for 1 second** – the bar fills, the word is typed and spoken.
2. Pick **English / தமிழ்** at the top to change the typing + speaking language.
3. **Speak** button reads the whole notepad aloud.
4. **Mic / Voice→Text** types what the other person says.

### ➕ Teach a new sign

1. Open the **Teach** tab.
2. Choose type: **Hand sign**, **Two-hand sign** or **Face expression**.
3. Type the English word and Tamil word.
4. Press **Record** → 3-second countdown → hold the sign steady for 2.5 seconds.
5. Record the same word again from a different angle / light to improve accuracy.

> For **two-hand signs keep BOTH hands visible** in the camera while recording.

Use the **Sensitivity** slider in *Library* – lower = stricter, higher = more forgiving.

---

## 🤟 Built-in signs

| Sign | English | தமிழ் |
|---|---|---|
| ✋ Open palm | Hello | வணக்கம் |
| ✊ Fist | Yes | ஆம் |
| 👍 Thumb up | Good | நல்லது |
| 👎 Thumb down | Bad | மோசம் |
| ✌️ Victory | Peace | அமைதி |
| 🤟 I-love-you | I love you | நான் உன்னை நேசிக்கிறேன் |
| ☝️ Index up | Wait | காத்திரு |
| 👌 OK | OK | சரி |
| 🤙 Call | Call me | எனக்கு அழை |
| 3 fingers | Three | மூன்று |
| 4 fingers *(desktop)* | Four | நான்கு |
| 🙏 Both palms together | Thank you | நன்றி |
| 🤝 Both fists touching | Together | ஒன்றாக |
| 😊 Smile | Happy | மகிழ்ச்சி |
| 😮 Mouth open + brows up | Surprised | ஆச்சரியம் |
| 😴 Eyes closed | Sleepy | தூக்கம் |

---

## 🔊 Tamil voice – how it works

| Platform | Tamil voice source | Needs internet? |
|---|---|---|
| Web / PWA | Device Tamil voice if installed, otherwise Google online voice | Only for fallback |
| Python desktop | gTTS (Google) | Yes |
| English voice | Device voice / pyttsx3 | No |

To get an **offline** Tamil voice on Android: *Settings → Text-to-speech output → Google engine → Install voice data → Tamil*.

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| Camera does not start | Use **https** or `localhost`; allow camera permission |
| Tamil voice silent | Connect to internet or install a Tamil voice (see above). Desktop shows the error under the notepad |
| Voice→Text not working | Use Chrome / Edge / Android Chrome. Desktop needs `PyAudio` + internet |
| `PyAudio` fails to install | `pip install pipwin && pipwin install pyaudio` (Windows) |
| Sign not detected | Better light, plain background, hold 1 second, raise Sensitivity |
| Two-hand sign not detected | Keep both hands fully in frame, record it again from 2–3 angles |
| Old version still shows after update | Open site, refresh twice (service worker cache) |

---

## 🧱 Tech stack

- **MediaPipe** – Gesture Recognizer, Hand Landmarks, Face Landmarker / Face Mesh
- **Web:** HTML + vanilla JS, Web Speech API, Service Worker (PWA), Capacitor / Electron wrappers
- **Desktop:** Python, OpenCV, CustomTkinter, pyttsx3, gTTS, SpeechRecognition
- Custom signs = nearest-neighbour match on normalised landmark vectors (one hand, two hands, or face)

---

## 🔐 Privacy

All camera processing happens locally on your device. No video, images or landmarks are sent anywhere.
Only the text to be spoken is sent to Google when the **online Tamil voice** is used, and the audio when **Voice→Text** is used in the browser/desktop.

---

## 🗺️ Roadmap

- [ ] Continuous (moving) signs – full sentences
- [ ] More built-in Tamil Sign Language (ISL) words
- [ ] Offline Tamil voice on desktop
- [ ] iOS build
- [ ] Shared community sign packs

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit: `git commit -m "Add my feature"`
4. Push and open a Pull Request

Sharing sign packs (`my-signs.json`) is very welcome too.

---

## 📄 License

MIT – see [LICENSE](LICENSE).

<div align="center">Made with ❤️ for the deaf & hard-of-hearing community · தமிழ் 💜</div>

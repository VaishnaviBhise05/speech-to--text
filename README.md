
#  Speech to Text

A simple Python project that converts spoken words into text using the **SpeechRecognition** library and **Google Speech Recognition API**.

##  Features

- 🎙️ Captures voice input from your microphone
- 📝 Converts speech into text
- 🔊 Adjusts for background noise
- ⚠️ Handles common errors:
  - No speech detected
  - Unrecognized speech
  - Internet connection issues

##  Technologies Used

- Python 3
- SpeechRecognition
- PyAudio
- Google Speech Recognition API

## 📂 Project Structure

```
speech-to-text/
│── speech_to_text.py
│── README.md
```

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/speech-to-text.git
```

2. Navigate to the project folder:

```bash
cd speech-to-text
```

3. Install the required packages:

```bash
pip install SpeechRecognition PyAudio
```

## ▶️ Usage

Run the Python script:

```bash
python speech_to_text.py
```

Example Output:

```
Adjusting for background noise...
Speak Now...
Recognizing...
You said: Hello, welcome to Speech to Text.
```

## 📋 Requirements

- Python 3.x
- Microphone
- Internet connection (required for Google Speech Recognition API)

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.


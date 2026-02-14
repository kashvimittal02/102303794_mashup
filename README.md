# Mashup Generation Using Audio Processing Techniques

---

## Objective

The objective of this project is to design and implement an automated mashup generation system that downloads multiple songs of a specified singer, extracts a fixed duration from each track, merges them into a single audio file, compresses it, and delivers the final output to the user via email using a web-based interface.

---

## System Description

The system consists of two main components:

- **Program 1:** Command-line based mashup generator.
- **Program 2:** Web-based mashup service using Flask that generates the mashup and sends the ZIP file to the user via email.  

The application performs the complete pipeline from user input to final output generation.

---

## Methodology

The project follows a structured pipeline approach:

### User Input

The user provides:

- Singer Name  
- Number of Videos (>10)  
- Duration in seconds (>20)  

Input is taken either:
- Through command-line arguments (Program 1)
- Through an HTML form (Program 2)

---

### YouTube Search and Audio Download

The system uses the `yt-dlp` library to:

- Search YouTube using:
  
  ytsearchN:Singer Name official song

- Download the best available audio format  
- Convert audio into MP3 using FFmpeg  

Downloaded audio files are stored in:

audios/

---

### Audio Processing

Using the `pydub` library:

- Each downloaded MP3 file is loaded  
- First Y seconds are extracted  
- Trimmed audio segments are concatenated sequentially  
- Final mashup is exported as:

mashup.mp3

---

### File Compression (Web Version)

The mashup file is compressed into:

mashup.zip

The web application automatically sends this ZIP file as a downloadable response to the user.

---

### Email Delivery (Web Version)

Using Flask-Mail and Gmail SMTP:

The ZIP file is attached to an email.

Gmail App Password authentication is used.

The mashup is sent to the user’s provided email address.

---

## System Architecture

User Input  
↓  
YouTube Search (yt-dlp)  
↓  
Audio Extraction (FFmpeg)  
↓  
Audio Trimming (pydub)  
↓  
Audio Merging  
↓  
Mashup File Generation  
↓  
ZIP Creation  
↓  
Email Delivery (Flask-Mail + Gmail SMTP)  

---

## Technologies Used

- Programming Language: Python  
- YouTube Download: yt-dlp  
- Audio Processing: pydub  
- Audio Conversion: FFmpeg  
- Web Framework: Flask  
- Email Service: Flask-Mail  
- Email Validation: email-validator  
- File Compression: zipfile  
- Frontend Interface: HTML Form   

---

## Result Table

| Test Case | Singer | Videos | Duration | Email Sent | Result |
|------------|---------|---------|-----------|--------------|---------|
| 1 | Sharry Mann | 11 | 30 sec | Yes | Success |
| 2 | Arijit Singh | 12 | 25 sec | Yes | Success |
| 3 | Sharry Mann | 5 | 30 sec | Yes | Failed (Invalid video count) |
| 4 | Sharry Mann | 12 | 10 sec | Yes | Failed (Invalid duration) |

---

## Result Analysis

Observations:

- Processing time increases as the number of videos increases.
- Larger duration increases final mashup file size.
- System performance depends on internet speed.
- Input validation prevents incorrect parameters.

### Performance Trend

| Videos | Approx Processing Time |
|----------|-------------------------|
| 11 | 2–3 minutes |
| 12 | 3–4 minutes |
| 15 | 5–6 minutes |

Graph Representation:

Processing Time  
↑  
|  
|        *  
|     *  
|  *  
|________________  
     11  12  15  
         Videos  

---

## Input Validation

The system ensures:

- Number of videos must be greater than 10  
- Duration must be greater than 20 seconds  
- All required fields must be filled  

Error messages are displayed for invalid inputs.

---

## Installation and Setup

Follow the steps below to set up and run the project locally:

### 1. Clone or Download the Project

Download the project folder and open it in VS Code.

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

For Windows:
```bash
venv\Scripts\activate
```
For macOS/Linux:
```bash
source venv/bin/activate
```

### 4. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 5. Install FFmpeg (System Dependency)

Download and install FFmpeg from:

https://www.gyan.dev/ffmpeg/builds/

Add the bin folder path to your system environment variables (PATH).

Verify Installation:
```bash
ffmpeg -version
```

### 6. Configure Email (Gmail App Password)
- Enable 2-Step Verification in your Google account.

- Generate an App Password from:
  https://myaccount.google.com/apppasswords

- Update the following in app.py:
```python
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_16_character_app_password'
```

### 7. Run the Application

```bash
python app.py
```

Open browser and visit:
```cpp
http://127.0.0.1:5000
```

---

## Output
### Output Webpage:
<img width="472" height="290" alt="output_webpage" src="https://github.com/user-attachments/assets/4e4b86ac-7065-449f-ae03-5fc2bd86273e" />

### Final generated output structure via email:
<img width="668" height="361" alt="image" src="https://github.com/user-attachments/assets/02904986-8c6c-4010-afdf-d248738fd002" />

mashup.zip  
└── mashup.mp3  

The mashup contains trimmed segments merged sequentially.

---

## Conclusion

The project successfully integrates automated YouTube data retrieval, audio processing techniques, file compression, and web-based service deployment. The system fulfills all assignment requirements and demonstrates practical implementation of Python-based automation and web development.

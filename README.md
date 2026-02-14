# Mashup Generation Using Audio Processing Techniques

---

## Objective

The objective of this project is to design and implement an automated mashup generation system that downloads multiple songs of a specified singer, extracts a fixed duration from each track, and merges them into a single audio file. The system demonstrates the integration of web scraping, audio processing, file compression, and web-based service development using Python technologies.

---

## System Description

The system consists of two main components:

- **Program 1:** Command-line based mashup generator  
- **Program 2:** Web-based mashup service using Flask  

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
Download via Web Interface  

---

## Technologies Used

- Programming Language: Python  
- YouTube Download: yt-dlp  
- Audio Processing: pydub  
- Audio Conversion: FFmpeg  
- Web Framework: Flask  
- File Compression: zipfile  
- Frontend Interface: HTML Form  

---

## Result Table

| Test Case | Singer | Videos | Duration | Result |
|------------|---------|---------|-----------|---------|
| 1 | Sharry Mann | 11 | 30 sec | Success |
| 2 | Arijit Singh | 12 | 25 sec | Success |
| 3 | Sharry Mann | 5 | 30 sec | Failed (Invalid video count) |
| 4 | Sharry Mann | 12 | 10 sec | Failed (Invalid duration) |

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

## Limitations

- Requires stable internet connection  
- YouTube rate limits may affect large downloads  
- Processing time increases with video count  
- Only publicly available YouTube content can be accessed  

The project successfully integrates automated YouTube data retrieval, audio processing techniques, file compression, and web-based service deployment. The system fulfills all assignment requirements and demonstrates practical implementation of Python-based automation and web development.

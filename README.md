# Emotion Detection Application

## Project Description
A web-based emotion detection application built using **Watson NLP** and **Flask**.
It analyzes text input and returns emotion scores and the dominant emotion.

## Features
- Emotion analysis using IBM Watson NLP API
- Web interface powered by Flask
- Unit tested with Python unittest
- Error handling for blank/invalid input
- Static code analysis compliant (Pylint)

## Project Structure
```
emotion_detection_project/
|-- EmotionDetection/
|   |-- __init__.py
|   |-- emotion_detection.py
|-- templates/
|   |-- index.html
|-- test_emotion_detection.py
|-- server.py
|-- README.md
```

## Installation
```bash
pip install flask requests pylint
```

## Usage
### Run the Flask Server
```bash
python server.py
```
Open browser: http://localhost:5000

### Run Unit Tests
```bash
python -m unittest test_emotion_detection.py -v
```

### Run Static Code Analysis
```bash
pylint server.py
```

## Technologies Used
- Python 3.x
- Flask
- IBM Watson NLP API
- Pylint
- Unittest

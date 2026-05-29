# Mean Median Mode Calculator

A Flask-based web application that calculates **Mean**, **Median**, and **Mode** from user input and displays a statistical graph using Matplotlib.

## Features

- Calculate Mean
- Calculate Median
- Calculate Mode
- Generate statistical graph
- Simple and responsive UI
- Flask backend
- Matplotlib graph visualization

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Matplotlib
- Statistics Module

---

## Project Structure

```bash
Mean-Median-Mode-Calculation/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   └── graph.png
│
├── templates/
│   └── index.html
```

---

## Installation

### Clone Repository

```bash
git clone (https://alamgirkhan48692.pythonanywhere.com/)
```

### Go to Project Directory

```bash
cd Mean-Median-Mode-Calculation
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Application will run on:

```text
http://127.0.0.1:5000
```

---

## Deployment

This project is deployed on PythonAnywhere using Flask and WSGI configuration.

---

## Example Input

```text
1,2,3,4,5,6,7
```

### Output

```text
Mean = 4.0
Median = 4.0
Mode = 1
```

---

## Requirements

```text
Flask
matplotlib
numpy
```

---

## Author

Alamgir Khan

---

## License

This project is open-source and available for educational purposes.

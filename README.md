# Sudoku Solver with Image Recognition

A web-based Sudoku solver that can generate puzzles, solve them, and even extract Sudoku puzzles from images using OCR technology.

## 🚀 Features

- **Interactive Sudoku Grid** - Play Sudoku directly in your browser
- **Puzzle Generation** - Generate new Sudoku puzzles with varying difficulties
- **Smart Solver** - Solve any Sudoku puzzle instantly using backtracking algorithm
- **Image Recognition** - Upload photos of Sudoku puzzles and automatically extract them
- **Real-time OCR** - Uses Tesseract.js to read Sudoku puzzles from images
- **Visual Feedback** - Cell highlighting, animations, and loading indicators
- **Responsive Design** - Works perfectly on desktop and mobile devices

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **OCR**: Tesseract OCR
- **Image Processing**: OpenCV, Pillow
- **Styling**: CSS Grid, Flexbox, Animations

## 📦 Installation

### Prerequisites
- Python 3.7+
- Tesseract OCR

### Windows Tesseract Installation
1. Download Tesseract from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
2. Install to `C:\Program Files\Tesseract-OCR\`
3. Add to System PATH

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/sudoku-solver.git
cd sudoku-solver

# Install Python dependencies
pip install flask opencv-python pillow numpy pytesseract

# Run the application
python app.py

*Image Upload Support*
The app can process:

1. Screenshots of Sudoku puzzles
2. Photos of newspaper/magazine Sudokus
3. Camera pictures of printed Sudoku puzzles
4. Digital Sudoku images

🎨 Features in Detail :
Smart Grid: Cell highlighting, input validation, visual feedback

Loading Animations: Smooth processing indicators for image uploads

OCR Technology: Advanced image processing for accurate digit recognition

Mobile Responsive: Optimized for all screen sizes

Modern UI: Beautiful gradients, animations, and intuitive controls
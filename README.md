# GradeGaze

GradeGaze is a simple web application that predicts a student's final mark and grade based on their internal assessment scores. It uses machine learning models and provides a clean user interface for input and result display.

## Features

- Input form for student name and internal marks (G1, G2)
- Predicts final marks using a regression model
- Predicts final grade using a classification model
- Displays result in a styled result card
- Built using Flask, HTML, and CSS

## Technologies Used

- Python
- Flask
- HTML & CSS
- Scikit-learn
- Pandas

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/gradegaze.git
   cd gradegaze

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
gradegaze/
├── app.py               # Flask app entry point
├── gradegaze.py         # Model loading and prediction logic
├── models/              # Trained ML models (.pkl files)
├── templates/
│   └── index.html       # HTML template
├── static/
│   └── style.css        # CSS styles
└── README.md
```

## Usage

* Enter a student’s name, G1, and G2 marks.
* Submit the form to get predicted final mark and grade.
* Results are shown in a styled card on the same page.

## Author

**Sreeram V Gopal**
📧 [sreeramvg100@gmail.com](mailto:sreeramvg100@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/sreeram-v-gopal-7477082a0/)


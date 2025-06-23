# GradeGaze

**GradeGaze** is a simple web application that uses a machine learning regression model to predict a student's final marks and academic grade based on internal assessments. It provides a clean, user-friendly interface where users can input student details and receive immediate predictions.

## Features

- Input form for student name and internal marks (G1 and G2)
- Predicts final mark using a trained regression model
- Converts the predicted mark into a letter grade using defined rules
- Displays results in a clean, styled result card
- Built using Python, Flask, and basic front-end tools (HTML & CSS)

## Machine Learning Overview

At the core of GradeGaze is a machine learning regression model trained on historical academic data. The model learns patterns between internal assessment scores and final marks, enabling it to make informed predictions. Letter grades are derived from the predicted mark using simple grade boundaries.

This approach makes the app lightweight, fast, and easy to interpret.

## Technologies Used

- Python
- Flask
- Scikit-learn (for regression model)
- Pandas
- HTML & CSS

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


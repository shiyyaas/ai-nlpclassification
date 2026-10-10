# NLP in Practice
## Text Analysis and Classification Using Machine Learning

This project implements two Natural Language Processing (NLP) tasks: rule-based resume information extraction and sentiment classification using machine learning.

## Objectives

### 1. Resume Information Extractor

A Python script that extracts email addresses and Indian mobile phone numbers from sample resumes using regular expressions (`re`).

**Features**
- Extracts email addresses and phone numbers.
- Validates Indian mobile number formats.
- Processes three sample resumes.
- Saves extracted information in a structured `output.json` file.

**Technologies:** Python, Regular Expressions, JSON

### 2. Sentiment Classification

A sentiment analysis system trained on a custom dataset containing 50,000 movie reviews.

**Dataset**
- Total reviews: 50,000
- Positive reviews: 25,000
- Negative reviews: 25,000
- Missing values: None

**Workflow**
1. Load and inspect the dataset.
2. Clean review text and remove HTML tags.
3. Split the data into training and testing sets (80:20).
4. Convert text into numerical features using TF-IDF.
5. Establish a baseline using TextBlob.
6. Train and evaluate multiple machine learning models.
7. Compare model performance using evaluation metrics and visualizations.

**Models used**
- TextBlob — baseline sentiment analysis
- Multinomial Naive Bayes
- Support Vector Machine (LinearSVC)
- Random Forest Classifier

**Evaluation metrics**
- Accuracy
- Precision
- Recall
- F1-score

Visualizations include a model performance comparison chart and confusion matrices.

## Project Structure

```text
NLP-Task12/
├── resume_extractor.py
├── output.json
├── sentiment_analysis.ipynb
└── README.md
```

## Technologies Used

- Python
- Google Colab / Jupyter Notebook
- Pandas
- Scikit-learn
- NLTK
- TextBlob
- Matplotlib
- Seaborn
- Regular Expressions (`re`)
- JSON

## Getting Started

### Resume Extractor

Run the script using Python:

```bash
python resume_extractor.py
```

The script generates `output.json` containing the extracted email addresses and phone numbers from the sample resumes.

### Sentiment Analysis

The sentiment analysis notebook can be opened and executed in Google Colab.

1. Open [Google Colab](https://colab.research.google.com/).
2. Open `sentiment_analysis.ipynb`.
3. Run the dataset download and installation cells.
4. Execute the notebook cells in order.
5. Review the evaluation results and visualizations.

Install the required libraries if running locally:

```bash
pip install pandas scikit-learn nltk textblob matplotlib seaborn jupyter
```

The dataset is loaded directly into the Colab runtime and does not need to be stored in this repository.

## Results

The notebook compares TextBlob, Naive Bayes, SVM and Random Forest using accuracy, precision, recall and F1-score. The executed notebook contains the measured results and visualizations for comparing the models.

## Deliverables

- `resume_extractor.py` — Resume information extraction script.
- `output.json` — Structured extraction results.
- `sentiment_analysis.ipynb` — Sentiment classification, evaluation and visualizations.
- `README.md` — Project documentation.

## Conclusion

This project demonstrates rule-based information extraction using regular expressions and supervised sentiment classification using traditional machine learning techniques. It compares different approaches to text classification and evaluates their performance using standard classification metrics.

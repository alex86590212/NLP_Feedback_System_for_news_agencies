from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
import pandas as pd
import os
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from classification import process_feedback, add_feedback, data_file, output_file

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        feedback = request.form['feedback']
        if feedback:
            add_feedback(feedback)
            flash('Feedback added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Please enter some feedback before submitting.', 'warning')

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    process_feedback()
    return jsonify(success=True)

@app.route('/suggestions', methods=['GET'])
def suggestions():
    if os.path.exists(output_file):
        df = pd.read_csv(output_file)
        suggestions = df.to_dict(orient='records')
    else:
        suggestions = []
    return render_template('suggestions.html', suggestions=suggestions)

@app.route('/department_overview', methods=['GET'])
def department_overview():
    if os.path.exists(output_file):
        df = pd.read_csv(output_file)
        departments = df.groupby('Additional Category').apply(lambda x: x.to_dict(orient='records')).to_dict()
    else:
        departments = {}
    return render_template('department_overview.html', departments=departments)

@app.route('/keyword_overview', methods=['GET'])
def keyword_overview():
    if os.path.exists(output_file):
        df = pd.read_csv(output_file)
        all_keywords = df['Keywords'].apply(lambda x: x.strip('[]').replace("'", "").split(', ')).tolist()
        all_keywords_flat = [item for sublist in all_keywords for item in sublist]

        excluded_keywords = ['sport', 'economics', 'politics']
        filtered_keywords = [kw for kw in all_keywords_flat if kw.lower() not in excluded_keywords]

        keyword_counts = Counter(filtered_keywords)
        most_common_keywords = keyword_counts.most_common(10)


        return render_template('keywords.html', keywords=most_common_keywords)
    else:
        return render_template('keywords.html', keywords=[])

if __name__ == '__main__':
    app.run(debug=True)

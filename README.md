# NLP_Feedback_System_for_news_agencies

Overview
This web application allows users to submit feedback, which is then processed by an AI model to classify the feedback and extract keywords. The feedback is categorized into positive feedback, negative feedback, and suggestions for improvement. The suggestions are further categorized into departments such as Sport, Economics, and Politics. The application also provides a visual overview of the most frequent keywords.

Features
Feedback Submission: Users can submit their feedback through a form.
AI Processing: The feedback is processed by an AI model to classify it and extract keywords.
Categorization: Feedback is categorized into different types and departments.
Keyword Frequency Graph: A visual representation of the most frequent keywords is provided.
Scrollable Containers: Suggestions, department overview, and keyword overview are presented in scrollable containers.

Installation
Prerequisites:
->Python 3.6 or higher
->Flask
->pandas
->transformers
->keybert
->matplotlib
->wordcloud
Usage : 
  Submitting Feedback:
    Open the web application in your browser.
    Enter your feedback in the text area and click "Submit Feedback".
    Click the "Process Feedback" button to process the feedback.
    Viewing Results
    Suggestions: After processing, you will be redirected to the suggestions page where you can view categorized feedback and keywords.
    Department Overview: Click on "Department Overview" to see feedback categorized by department.
    Keyword Overview: Click on "Keyword Overview" to see a visual representation of the most frequent keywords.
Contributions
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any improvements or bugs you find.

License
This project is licensed under the MIT License. See the LICENSE file for details.

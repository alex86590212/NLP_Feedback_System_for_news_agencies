# NLP_Feedback_System_for_news_agencies

# AI Feedback Processing Web Application

## Overview

This web application allows users to submit feedback, which is then processed by an AI model to classify the feedback and extract keywords. The feedback is categorized into positive feedback, negative feedback, and suggestions for improvement. The suggestions are further categorized into departments such as Sport, Economics, and Politics. The application also provides a visual overview of the most frequent keywords.

## Features

- **Feedback Submission:** Users can submit their feedback through a form.
- **AI Processing:** The feedback is processed by an AI model to classify it and extract keywords.
- **Categorization:** Feedback is categorized into different types and departments.
- **Keyword Frequency Graph:** A visual representation of the most frequent keywords is provided.
- **Scrollable Containers:** Suggestions, department overview, and keyword overview are presented in scrollable containers.

## Installation

### Prerequisites

- Python 3.6 or higher
- Flask
- pandas
- transformers
- keybert
- matplotlib
- wordcloud

### Clone the Repository

```bash
git clone https://github.com/yourusername/feedback-processing-app.git
cd feedback-processing-app

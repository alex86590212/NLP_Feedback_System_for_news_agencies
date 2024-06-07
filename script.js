function processFeedback() {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('feedback-container').style.display = 'none';

    fetch('/process', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loading').style.display = 'none';
        if (data.success) {
            window.location.href = '/suggestions';
        } else {
            alert('Failed to process feedback');
            document.getElementById('feedback-container').style.display = 'block';
        }
    })
    .catch(error => {
        document.getElementById('loading').style.display = 'none';
        console.error('Error:', error);
        alert('Failed to process feedback');
        document.getElementById('feedback-container').style.display = 'block';
    });
}

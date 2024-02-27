from flask import Flask, request, jsonify
import joblib
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt', quiet=True)

app = Flask(__name__)

# Stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('turkish'))

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    comment = data.get('comment')

    if not comment:
        return jsonify({'error': 'No comment provided'}), 400

    # Yorumu işleme ve vektörleştirelme
    processed_comment = " ".join([word for word in word_tokenize(comment) if not word in stop_words])

    # Model ve vektörleştiriciyi yükleme
    clf = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')

    # Yorum için duygu analizi
    X = vectorizer.transform([processed_comment])
    y = clf.predict(X)

    sentiment = {0: 3, 1: 2}.get(y[0], "Invalid prediction")

    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

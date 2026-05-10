from flask import Flask, request, render_template
import joblib
import PyPDF2  

app = Flask(__name__)

# تحميل الموديل والـ vectorizer (استخدمت r عشان تتجنب مشاكل المسارات)
model = joblib.load("best_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

def predict(text):
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    # التأكد إن المستخدم رفع ملف
    if 'resume' not in request.files:
        return "No file part in the request"
    
    file = request.files['resume']
    
    if file.filename == '':
        return "No selected file"

    if file and file.filename.endswith('.pdf'):
        # 1. استخراج النص من الـ PDF
        text = extract_text_from_pdf(file)
        
        # 2. عمل الـ Prediction
        result = predict(text)
        
        return render_template('index.html', prediction=result)
    else:
        return "Please upload a valid PDF file"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
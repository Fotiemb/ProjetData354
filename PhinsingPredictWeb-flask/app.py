# import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


model = pickle.load(open('phishingLR.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

     # Récupérer l'URL depuis le formulaire
    url = request.form.get('url')

    # output = round(prediction[0], 2)

     # Effectuer une prédiction sur l'URL (vous devez ajuster cela en fonction de la logique de votre modèle)
    prediction = model.predict([url])

    return render_template('index.html', prediction_text='ANALYSE D\'URL: {}'.format(prediction[0]))

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run()
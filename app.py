# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 19:56:11 2022

@author: Admin
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

import bz2file as bz2
import _pickle as cPickle


from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
##M1 model = pickle.load(open('random_forest_regression_model1.pbz2', 'rb')) ###M1
###M2
def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data
model = decompress_pickle('random_forest_regression_model10.pbz2') ###M2
###M3
# Load any compressed pickle file
# def decompress_pickle(file):
#     data = bz2.BZ2File(file, 'rb')
#     data = cPickle.load(data)
#     return data
#model = decompress_pickle('rfr1.pbz2')  ###M3

# import bz2
# #data = model
# with bz2.open("dog.bz2", "wb") as f:
#     # Write compressed data to file
#     unused = f.write('rfr1.pbz2')  ###M3
# with bz2.open("dog.bz2", "rb") as f:
#     # Decompress data from file
#     model1 = f.read()
 ###model1 

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        property_size= int(request.form['property_size'])
        # Present_Price=float(request.form['Present_Price'])
        # Kms_Driven=int(request.form['Kms_Driven'])
        # Kms_Driven2=np.log(Kms_Driven)
        # Owner=int(request.form['Owner'])
        bedrooms=request.form['bedrooms']
        if(bedrooms=='1'):
            bedrooms=1
        elif(bedrooms=='2'):
            bedrooms=2
        elif(bedrooms=='3'):
            bedrooms=3
        elif(bedrooms=='4'):
            bedrooms=4
        else:
            bedrooms=5
        bathroom=request.form['bathroom']
        if(bathroom=='1'):
            bathroom=1
        elif(bathroom=='2'):
            bathroom=2
        elif(bathroom=='3'):
            bathroom=3
        elif(bathroom=='4'):
            bathroom=4
        elif(bathroom=='5'):
            bathroom=5
        else:
            bathroom=6
        furnishingDesc=request.form['furnishingDesc']
        if(furnishingDesc=='0'):
            furnishingDesc=0
        elif(furnishingDesc=='1'):
            furnishingDesc=1
        else:
            furnishingDesc=2
        parking=request.form['parking']
        if(parking=='1'):
            parking=1
        elif(parking=='2'):
            parking=2
        else:
            parking=4
       
        Lift=request.form['Lift']
        if(Lift=='1'):
            Lift=1
        else:
            Lift=0	
        Security=request.form['Security']
        if(Security=='1'):
            Security=1
        else:
            Security=0
        locality=request.form['locality']
        if(locality=='0'):
            locality=0
        elif(locality=='1'):
            locality=1
        elif(locality=='2'):
            locality=2
        elif(locality=='3'):
            locality=3
        elif(locality=='4'):
            locality=4
        elif(locality=='5'):
            locality=5
        elif(locality=='6'):
            locality=6
        elif(locality=='7'):
            locality=7
        elif(locality=='8'):
            locality=8
        else:
            locality=9
        
        
        prediction=model.predict([[property_size,bedrooms,bathroom,furnishingDesc,parking,Lift,Security,locality]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot stay in rented house")
        else:
            return render_template('index.html',prediction_text="You should pay INR of  ₹{}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)


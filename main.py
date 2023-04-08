from flask import Flask,render_template,request,redirect,url_for
import joblib
import numpy as np
model = joblib.load('Mumbai_house_prediction')

places = ['Agripada',
 'Airoli',
 'Ambernath East',
 'Andheri East',
 'Andheri West',
 'Badlapur East',
 'Badlapur West',
 'Bandra Kurla Complex',
 'Bandra West',
 'Bhandup East',
 'Bhandup West',
 'Bhayandar East',
 'Bhiwandi',
 'Borivali East',
 'Borivali West',
 'Byculla',
 'Chembur',
 'Dahisar',
 'Diva Gaon',
 'Dombivali',
 'Dombivali East',
 'Dombivli (West)',
 'Ghansoli',
 'Ghatkopar East',
 'Ghatkopar West',
 'Goregaon East',
 'Jogeshwari West',
 'Kalamboli',
 'Kalwa',
 'Kalyan West',
 'Kamothe',
 'Kandivali East',
 'Kandivali West',
 'Karanjade',
 'Karjat',
 'Khar West',
 'Kharghar',
 'Koper Khairane',
 'Kurla',
 'Lower Parel',
 'Malad East',
 'Malad West',
 'Mazgaon',
 'Mira Road East',
 'Mulund West',
 'Naigaon East',
 'Nala Sopara',
 'Neral',
 'Palghar',
 'Panvel',
 'Powai',
 'Rasayani',
 'Santacruz East',
 'Seawoods',
 'Sion',
 'Taloja',
 'Thakurli',
 'Thane West',
 'Ulwe',
 'Vasai',
 'Vashi',
 'Vichumbe',
 'Vikhroli',
 'Virar',
 'Wadala']
bed = [1,2,3,4,5]
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',places = places)

@app.route('/predict',methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        beds = int(request.form.get('bed'))
        place_given = request.form.get('place')
        place = places.index(place_given)
        sqft_given = request.form.get('sqft')
        sqft = sqft_given.split('-')
        sqft = np.mean([int(i) for i in sqft])
        clas_given= request.form.get('class')
        clas = clas_given.split('-')
        if clas == '4':
            req_clas = 10000
        elif clas == '3':
            req_clas = 20000
        elif clas == '2':
            req_clas = 30000
        elif clas == "1":
            req_clas = 40000
        else:
            req_clas = 20000
        final = round(model.predict([[sqft,beds,req_clas,place]])[0],3)
        pla = place_given
        return render_template('predict.html',sqft = sqft_given,bed = beds,clas = clas_given,place = pla,final = final)




if __name__ == '__main__':
    app.run(debug = True)
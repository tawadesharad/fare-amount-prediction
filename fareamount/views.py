from pydoc import render_doc
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import joblib
import xgboost as xgb
import sklearn.model_selection
import pickle
# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    XGB_optimal_model = joblib.load('finalized_model1.sav')
    # XGB_optimal_model = pickle.load(open('finalized_model.sav', 'rb'))
# result = loaded_model.score(X_test, Y_test)

    lis = []

    lis.append(float(request.GET['pickup_longitude']))
    lis.append(float(request.GET['pickup_latitude']))
    lis.append(float(request.GET['dropoff_longitude']))
    lis.append(float(request.GET['dropoff_latitude']))
    lis.append(float(request.GET['passenger_count']))
    lis.append(float(request.GET['day']))
    lis.append(float(request.GET['month']))
    lis.append(float(request.GET['year']))
    lis.append(float(request.GET['hour']))
    lis.append(float(request.GET['distance']))

    ans = XGB_optimal_model.predict([lis])


    return render(request, 'result.html',{'ans':ans,'lis':lis})

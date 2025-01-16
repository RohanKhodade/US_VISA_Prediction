from django.shortcuts import render,redirect

from django.http import HttpResponse

import datetime

import os

import pickle

import pandas as pd
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREPROCESSOR_PATH = os.path.join(BASE_DIR, 'Ml_Models', 'preprocessor.pkl')
MODEL_PATH = os.path.join(BASE_DIR, 'Ml_Models', 'knn_model.pkl')

with open(MODEL_PATH,"rb") as model_file:
    model=pickle.load(model_file)
    
with open(PREPROCESSOR_PATH,"rb") as preprocessor_file:
    preprocessor=pickle.load(preprocessor_file)


# Create your views here.

def predict(request):
    
    if request.method=="POST":
        # get input from form
        continent = request.POST.get('continent')
        education_of_employee = request.POST.get('education_of_employee')
        has_job_experience = request.POST.get('has_job_experience')
        requires_job_training = request.POST.get('requires_job_training')
        no_of_employees = request.POST.get('no_of_employees')
        region_of_employment = request.POST.get('region_of_employment')
        prevailing_wage = request.POST.get('prevailing_wage')
        full_time_position = request.POST.get('full_time_position')
        yr_of_estab = request.POST.get('yr_of_estab')
        unit_of_wage = request.POST.get('unit_of_wage')
        
        current_year=datetime.datetime.now().year
        company_age=current_year-int(yr_of_estab)
        
        #data conversion 
        yesno=[has_job_experience, requires_job_training,full_time_position]
        
        
        
        
        data={
            
        "continent": continent,
        'education_of_employee' :education_of_employee,
        "has_job_experience":has_job_experience,
        "requires_job_training":requires_job_training ,
        "no_of_employees": int( no_of_employees),
        "region_of_employment":region_of_employment,
        "prevailing_wage" :float(prevailing_wage),
        "full_time_position" :full_time_position,
        "company_age": company_age,
        "unit_of_wage" :unit_of_wage,
        }
        data = {key: 'Y' if value == 'YES' else 'N' if value == 'NO' else value for key, value in data.items()}

        
        data=pd.DataFrame([data])
        
        transformed_data=preprocessor.transform(data)
        
        predict=model.predict(transformed_data)
        
        status=""
        if predict==1:
            status="NotAllowed"
            print("Denied")
        else:
            status="Allowed"
            print("Allowed")
            
        request.session["status"]=status
            
            
        return redirect("result") 
        
    return render(request,"prediction.html")

def predicted(request):
    
    
    status = request.session.get("status", "")
    
    # Clear the session after displaying the result to avoid unnecessary session data persistence
    del request.session["status"]
    return render(request,"result.html",{"status":status})
                          
                          
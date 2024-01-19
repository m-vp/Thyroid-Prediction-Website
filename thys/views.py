from django.shortcuts import render , HttpResponse ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import os
import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

from .models import Feedback

def signuppage(request):
    if request.method == 'POST':
        username = request.POST['username']#username = request.POST.get('username')
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password != cpassword:
            return HttpResponse('passwords do not match')
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error_message': 'Username is not unique'})
        my_user = User.objects.create_user(username,email,password)
        my_user.save()

        print(username)
        return redirect('login') #name of url shud be written
    return render(request,'signup.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']#username = request.POST.get('username')
        password = request.POST['password']

        user = authenticate(request,username = username,password = password) #lhs is table col.
        if user is not None:
            login(request,user)
            return render(request,'home.html')
        else:
            return HttpResponse("username or password is incorrect")
    return render(request,'login.html')



def predict(request):
    return render(request, 'predict.html')


def home(request):
    return render(request,'home.html')



from .models import ThyroidResult

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import joblib

def result(request):
    if request.method == 'POST':
        print("Inside result view")

        # Load the joblib model
        data = pd.read_csv('Preprocessed_data_new.csv')

# Divide the dataset into features (X) and target variable (Y)
        X = data.drop('classes', axis=1)
        Y = data['classes']

# Encode categorical features using OrdinalEncoder
        ordinal_encoder = OrdinalEncoder()
        X_encoded = pd.DataFrame(ordinal_encoder.fit_transform(X.select_dtypes(exclude='number')))
        X_encoded.columns = X.select_dtypes(exclude='number').columns

# Encode 'referral source' and 'classes' using LabelEncoder
        label_encoder = LabelEncoder()
        Y_encoded = label_encoder.fit_transform(Y)

# Combine encoded features with numerical features
        X_final = pd.concat([X.select_dtypes(exclude='O').reset_index(drop=True), X_encoded], axis=1)

# Split the data into training and testing sets
        X_train, X_test, Y_train, Y_test = train_test_split(X_final, Y_encoded, test_size=0.2, random_state=1)

# Create and train the Random Forest model
        rf_model = RandomForestClassifier(n_estimators=100, max_depth=5)
        rf_model.fit(X_train, Y_train)
        # Rest of your code
        val_user = request.POST.get('user')
        val_age = int(request.POST.get('age'))
        val_sex = int(request.POST.get('sex'))
        val_on_thyroxine = int(request.POST.get('on_thyroxine'))
        val_query_on_thyroxine = int(request.POST.get('query_on_thyroxine'))
        val_on_antithyroid_medication = int(request.POST.get('on_antithyroid_medication'))
        val_sick = int(request.POST.get('sick'))
        val_pregnant = int(request.POST.get('pregnant'))
        val_thyroid_surgery = int(request.POST.get('thyroid_surgery'))
        val_I131_treatment = int(request.POST.get('I131_treatment'))
        val_query_hypothyroid = int(request.POST.get('query_hypothyroid'))
        val_query_hyperthyroid = int(request.POST.get('query_hyperthyroid'))
        val_lithium = int(request.POST.get('lithium'))
        val_goitre = int(request.POST.get('goitre'))
        val_tumor = int(request.POST.get('tumor'))
        val_hypopituitary = int(request.POST.get('hypopituitary'))
        val_psych = int(request.POST.get('psych'))
        val_TSH_measured = int(request.POST.get('TSH_measured'))
        val_TSH = float(request.POST.get('TSH'))
        val_T3_measured = int(request.POST.get('T3_measured'))
        val_T3 = float(request.POST.get('T3'))
        val_TT4_measured = int(request.POST.get('TT4_measured'))
        val_TT4 = int(request.POST.get('TT4'))
        val_T4U_measured = int(request.POST.get('T4U_measured'))
        val_T4U = float(request.POST.get('T4U'))
        val_FTI_measured = int(request.POST.get('FTI_measured'))
        val_FTI = int(request.POST.get('FTI'))
        val_TBG_measured = int(request.POST.get('TBG_measured'))
        val_referral_source = int(request.POST.get('referral_source'))

        pred = rf_model.predict([[val_age, val_sex, val_on_thyroxine, val_query_on_thyroxine, val_on_antithyroid_medication,
                               val_sick, val_pregnant, val_thyroid_surgery, val_I131_treatment, val_query_hypothyroid,
                               val_query_hyperthyroid, val_lithium, val_goitre, val_tumor, val_hypopituitary, val_psych,
                               val_TSH_measured, val_TSH, val_T3_measured, val_T3, val_TT4_measured, val_TT4,
                               val_T4U_measured, val_T4U, val_FTI_measured, val_FTI, val_TBG_measured,val_referral_source]])

        result1 = "5"

        if pred == [0]:
            result1 = "compensated hypothyroid"
        elif pred == [1]:
            result1 = "negative"
        elif pred == [2]:
            result1 = "primary hypothyroid"
        elif pred == [3]:
            result1 == "secondary hypothyroid"
            
            
        pred=int(pred[0])

        # Save the result to the database
        ThyroidResult.objects.create(
            user=request.user,#user = val_user
            age=val_age,
            sex=val_sex,
            on_thyroxine=val_on_thyroxine,
            query_on_thyroxine=val_query_on_thyroxine,
            on_antithyroid_medication=val_on_antithyroid_medication,
            sick=val_sick,
            pregnant=val_pregnant,
            thyroid_surgery=val_thyroid_surgery,
            I131_treatment=val_I131_treatment,
            query_hypothyroid=val_query_hypothyroid,
            query_hyperthyroid=val_query_hyperthyroid,
            lithium=val_lithium,
            goitre=val_goitre,
            tumor=val_tumor,
            hypopituitary=val_hypopituitary,
            psych=val_psych,
            TSH_measured=val_TSH_measured,
            TSH=val_TSH,
            T3_measured=val_T3_measured,
            T3=val_T3,
            TT4_measured=val_TT4_measured,
            TT4=val_TT4,
            T4U_measured=val_T4U_measured,
            T4U=val_T4U,
            FTI_measured=val_FTI_measured,
            FTI=val_FTI,
            TBG_measured=val_TBG_measured,
            referral_source=val_referral_source,
            result_value=pred
)



        return render(request, "result.html", {"result2": result1})
    else:
        print('wooooooooooooooooooooooooooo')

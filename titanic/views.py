from django.shortcuts import render
from. import titanic_model
def home(request):
    return render(request, 'index.html')

def prediction(request):
    pclass = request.GET['pclass']
    sex = request.GET['sex']
    age = request.GET['age']
    sibhp = request.GET['sibhp']
    parch = request.GET['parch']
    fare = request.GET['fare']
    mbarked = request.GET['mbarked']
    title = request.GET['title']


    pred, prediction = titanic_model.rfc(pclass,sex,age,sibhp,parch,fare,mbarked,title)

    return render(request, 'prediction.html', {'pred': pred,
                                               'prediction': prediction})
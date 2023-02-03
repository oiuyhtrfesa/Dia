from django.shortcuts import render

def home(request):
    return render(request,'result.html')

def getPredictions(high_bp,highchol,cholcheck,bmi,smoker,stroke,heartdisease_attack,Phys_activity,fruits,veggies,hvyalcoholconsump,anyhealthcare,NoDocbcCost,GenHlth,MentHlth,PhysHlth,DiffWalk,sex,age,education,income):
    import pickle
    model=pickle.load(open(rb"C:\Users\Dell\Downloads\diabetes_prediction_model.sav","rb"))
    prediction=model.predict([[high_bp,highchol,cholcheck,bmi,smoker,stroke,heartdisease_attack,Phys_activity,fruits,veggies,hvyalcoholconsump,anyhealthcare,NoDocbcCost,GenHlth,MentHlth,PhysHlth,DiffWalk,sex,age,education,income]])
    if(prediction==0):
        return "u dont have diabetes"
    else:
        return "u have diabetes"

def result(request):
    high_bp=int(request.GET['high_bp'])
    highchol=int(request.GET['highchol'])
    cholcheck=int(request.GET['cholcheck'])
    bmi=int(request.GET['bmi'])
    smoker=int(request.GET['smoker'])
    stroke=int(request.GET['stroke'])
    heartdisease_attack=int(request.GET['heartdisease_attack'])
    phys_activity=int(request.GET['phys_activity'])
    fruits=int(request.GET['fruits'])
    veggies=int(request.GET['veggies'])
    hvyalcoholconsump=int(request.GET['hvyalcoholconsump'])
    anyhealthcar=int(request.GET['anyhealthcare'])
    NoDocbcCost=int(request.GET['NoDocbcCost'])
    GenHlth=int(request.GET['GenHlth'])
    MentHlth=int(request.GET['MentHlth'])
    PhysHlth=int(request.GET['PhysHlth'])
    DiffWalk=int(request.GET['DiffWalk'])
    sex=int(request.GET['sex'])
    age=int(request.GET['age'])
    education=int(request.GET['education'])
    income=int(request.GET['income'])

    result=getPredictions(high_bp,highchol,cholcheck,bmi,smoker,stroke,heartdisease_attack,phys_activity,fruits,veggies,hvyalcoholconsump,anyhealthcar,NoDocbcCost,GenHlth,MentHlth,PhysHlth, DiffWalk,sex,age,education,income)
    return render(request,'index.html',{'result':result})

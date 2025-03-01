from django.shortcuts import render
import pickle
import numpy as np

# Cargar modelo guardado
filename = 'static/classification_svc_sklearn_1_2_2.pickle'
with open(filename, 'rb') as f:
    loaded_model_classification = pickle.load(f)

filename = 'static/regression_rf_sklearn_1_2_2.pickle'
with open(filename, 'rb') as f:
    loaded_model_regression = pickle.load(f)

# Vista Index
def index(request):
    template = 'portfolio_app/index.html'
    return render(request, template)

# Vista Iris
def iris(request):

    pred_label = ""
    pred_image_name = ""

    if request.method == "POST":

        slength = float(request.POST.get('slength'))
        swidth = float(request.POST.get('swidth'))
        plength = float(request.POST.get('plength'))
        pwidth = float(request.POST.get('pwidth'))

        lista_iris = [slength, swidth, plength, pwidth]
        x_new = np.array([lista_iris])
        y_pred = int(loaded_model_classification.predict(x_new))

        dictionary = {0:('Iris Setosa', 'iris-setosa.png'), 
                      1:('Iris Versicolor', 'iris-versicolor.png'), 
                      2:('Iris Virginica', 'iris-virginica.png')}
        
        pred_label = dictionary[y_pred][0]
        pred_image_name = dictionary[y_pred][1]    

    template = 'portfolio_app/iris.html'
    context = {'pred_label': pred_label, 
               'pred_image_name': pred_image_name}
    
    return render(request, template, context)


# Vista Casa
def casa(request):

    pred_label = ""

    if request.method == "POST":

        overall_quality = int(request.POST.get('OverallQual'))
        above_ground_living_area = int(request.POST.get('GrLivArea'))
        first_floor_sf = int(request.POST.get('1stFlrSF'))
        full_bath = int(request.POST.get('FullBath'))
        year_built = int(request.POST.get('YearBuilt'))

        lista_casa = [overall_quality, above_ground_living_area, first_floor_sf, full_bath, year_built]

        x_new = np.array([lista_casa])
        y_pred = float(loaded_model_regression.predict(x_new))
        
        pred_label = f"{y_pred:.2f}"

    template = 'portfolio_app/casa.html'
    context = {'pred_label': pred_label}
    
    return render(request, template, context)
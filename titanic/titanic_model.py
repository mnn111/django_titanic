
def rfc(pclass, sex, age, sibhp, parch, fare, mbarked, title):
    import pickle
    # titanic_model_nnkeras.sav
    with open('titanic_model.sav', 'rb') as m:
        randomforest = pickle.load(m)
        x = [[pclass, sex, age, sibhp, parch, fare, mbarked, title]]
        pred = randomforest.predict(x)
        # pred =123
        if pred == 0:
            pred = 'will not survive'
        elif pred == 1:
            pred = "survive"
        else:
            pred = "Error"

    import numpy as np
    from keras.models import load_model

    model_predict = load_model('titanic_nn_keras.h5')


    person = np.array([[1,2,30,2,2,50,2,1]])
    prediction_rate = model_predict.predict(person)
    # print(prediction_rate)


    if prediction_rate >.5 :
        prediction = "Survived"
    else:
        prediction = "not Survived"
    # print(prediction)

    return pred, prediction

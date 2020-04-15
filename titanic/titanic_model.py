
def rfc(pclass, sex, age, sibhp, parch, fare, mbarked, title):
    import pickle
    # titanic_model_nnkeras.sav
    with open('titanic_model.sav', 'rb') as m:
        randomforest = pickle.load(m)
        x = [[pclass, sex, age, sibhp, parch, fare, mbarked, title]]
        pred = randomforest.predict(x)
        # pred =123
        if pred == 0:
            pred = 'Will not Survive'
        elif pred == 1:
            pred = "Survive"
        else:
            pred = "Error"
    return pred


def keras_nn(pclass, sex, age, sibhp, parch, fare, mbarked, title):
    import numpy as np
    from keras.models import load_model

    model_predict = load_model('titanic_nn_keras.h5')


    person = np.array([[pclass, sex, age, sibhp, parch, fare, mbarked, title]])
    prediction_rate = model_predict.predict(person)
    # print(prediction_rate)


    if prediction_rate >.5 :
        prediction = "Survive"
    else:
        prediction = "Will not Survive"
    # print(prediction)
    prediction_rate = round(prediction_rate[0][0]*100, 2)
    return prediction, prediction_rate

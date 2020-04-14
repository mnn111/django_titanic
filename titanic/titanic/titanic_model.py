
def rfc(pclass, sex, age, sibhp, parch, fare, mbarked, title):
    import pickle

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
        return pred



import pickle


def predict(data):
    clf = pickle.load(open('irismodel.pkl', 'rb'))
    return clf.predict(data)



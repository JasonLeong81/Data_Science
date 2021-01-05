import matplotlib.pyplot as plt


def plotting():
    x = [i for i in range(10)]
    print(x)
    y = [2*i for i in range(10)]
    print(y)
    plt.plot(x,y)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()

    plt.scatter(x,y)
    plt.show()
# plotting()

def features_and_labels():
    # features, aka attributes, are independent
    # number of features is known as the dimension
    # label is the output of our model (dependent). For example, f1,f2,f3,label
    # number of rows is known as the number of instances
    # For features, we use capital cases for variables and for label we use lower case variables.
    # features is preferred to be within -1,1
    pass
# features_and_labels()

def saving_and_opening_model():
    import joblib
    filename = 'model.sav'
    clf = 'our model'
    joblib.dump(clf,filename)
    # clf = joblib.load(filename) # opening the model
# saving_and_opening_model()

def classification():
    # algorithmns that find a way to seperate labels
    pass
# classification()

def tt_split():
    from sklearn import datasets
    from sklearn.model_selection import train_test_split
    import numpy as np
    iris = datasets.load_iris()
    # split into features and labels
    x = iris.data
    y = iris.target
    print(x) # features
    print(y) # labels
    # print(x.shape,y.shape)
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
    print(x_train.shape,x_train[0])
    print(x_test.shape,x_test[0])
    print(y_train.shape,y_train[0])
    print(y_test.shape,y_test[0])
    # Vetting is the process of thoroughly investigating an individual
    # x_train is the training data set.
    # y_train is the set of labels to all the data in x_train.
    # The test set is a subset of the data set that you use to test your model after the model has gone through initial vetting by the validation set.
    # x_test is the test data set.
    # y_test is the set of labels to all the data in x_test.
# tt_split()

def KNN():
    import numpy as np
    import pandas as pd
    from sklearn import neighbors, metrics
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder

    # part of classification and regression
    # How it works: Calculate distance between new point and 15 nearest points. If majority of 15 points is green, then the new point is green. We can change 15 to any number, this number is the known as k.
    # Advise: K should be odd, weights = uniform (gives equal chances to all points) or distance (shortest one wins)

    data = pd.read_csv('car.data')
    # print(data.head())

    x = data[['buying','maint','safety']].values
    y = data[['class']]
    # print(x,y)

    # Converting the data
    le = LabelEncoder()
    for i in range(len(x[0])):
        x[:,i] = le.fit_transform(x[:,i])
    # print(x)

    label_mapping = {
        'unacc':0,
        'acc':1,
        'good':2,
        'vgood':3
    }
    y['class'] = y['class'].map(label_mapping)
    y = np.array(y)
    # print(y)

    # Create  model
    knn = neighbors.KNeighborsClassifier(n_neighbors=25,weights='uniform') # k=25, weight=uniform
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
    knn.fit(x_train,y_train) # this trains the model # this requires features and labels
    # predictions = knn.predict(x_test)
    # accuracy = metrics.accuracy_score(y_test,predictions)
    # print(predictions)
    # print(accuracy)

    print(y[-1])
    print(knn.predict(x)[-1])


KNN()
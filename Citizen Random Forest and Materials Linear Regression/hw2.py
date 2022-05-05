from pyexpat import features
from time import time
from timeit import Timer
import warnings

from sklearn import metrics
from sklearn.model_selection import GridSearchCV
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import numpy as np
import os
from sklearn import tree
from sklearn.metrics import confusion_matrix, matthews_corrcoef, f1_score, plot_confusion_matrix, roc_curve, roc_auc_score, plot_roc_curve, mean_squared_error, mean_absolute_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
import matplotlib.pyplot as plt

def fetal_health_classification():
    df = pd.read_csv("fetal_health.csv")
    train = df.iloc[:1500]      #first 1500 samples for training
    test = df.iloc[1500:]       #remaining for testing

    trainX = train[train.columns[:-1]]  #removes health index
    trainY = train["fetal_health"]      

    testX = test[test.columns[:-1]]  
    testY = test["fetal_health"]      

    clf = tree.DecisionTreeClassifier()
    clf.fit(trainX,trainY)
    depth = clf.get_depth()
    plt.figure(figsize=(15,7))
    clf_tree = tree.plot_tree(clf, max_depth=depth/2, fontsize=4, feature_names=train.columns) #use column names from train
    plt.show()

    test_predict_Y = clf.predict(testX)
    print("Confusion Matrix")
    print(confusion_matrix(testY, test_predict_Y))
    print("Matthews Correlation Coefficient")
    print(matthews_corrcoef(testY, test_predict_Y))
    print("Weighted F1 Score")
    print(f1_score(testY, test_predict_Y, average="weighted"))

    #feature importance
    feats = clf.feature_importances_
    for feat, coeff in enumerate(feats):
        print(f"Feature: {df.columns[feat]} Score: {coeff}")
    plt.figure(figsize=[7,7])
    plt.bar([x for x in trainX.columns], feats)
    plt.title("Importance of Features")
    plt.xlabel("Feature")
    plt.ylabel("Importance")
    plt.tick_params(axis='x', rotation=90)
    plt.tight_layout()
    plt.show()


def salary_random_forest():
    df = pd.read_csv("adult.data", names = ["age", "workclass", "fnlwgt", 
    "education", "education-num", "marital", "occupation", "relationship", "race", 
    "sex", "capital-gain", "capital-loss", "hours/week", "native-ctry", "50k-income"])
    df = pd.DataFrame(df)
    test = pd.read_csv("adult.test", names = df.columns)
    test = pd.DataFrame(test)
    X_train = df.drop("50k-income", axis = 1)
    X_train = X_train.replace("?",np.nan)
    X_train = X_train.fillna("na")
    #replace all ? values in object dtype cols with empty space
    X_train["workclass"] = X_train["workclass"].str.replace("?", "na")
    X_train["occupation"] = X_train["occupation"].str.replace("?", "na")
    X_train["education"] = X_train["education"].str.replace("?", "na")
    X_train["marital"] = X_train["marital"].str.replace("?", "na")
    X_train["relationship"] = X_train["relationship"].str.replace("?", "na")
    X_train["race"] = X_train["race"].str.replace("?", "na")
    X_train["sex"] = X_train["sex"].str.replace("?", "na")
    X_train["native-ctry"] = X_train["native-ctry"].str.replace("?", "na")

    Y_train = df[["50k-income"]]
    Y_train = pd.DataFrame(Y_train["50k-income"].str.replace("?", "na"))
    Y_train = pd.DataFrame(Y_train["50k-income"].str.replace("<=50K", "0"))
    Y_train = pd.DataFrame(Y_train["50k-income"].str.replace(">50K", "1"))
    Y_train = Y_train.astype(str).astype(int)
    
    X_test = test.drop("50k-income", axis = 1)
    X_test = X_test.replace("?",np.nan)
    X_test = X_test.fillna("na")
    #replace all ? values in object dtype cols with empty space
    X_test["workclass"] = X_test["workclass"].str.replace("?", "")
    X_test["occupation"] = X_test["occupation"].str.replace("?", "")
    X_test["education"] = X_test["education"].str.replace("?", "")
    X_test["marital"] = X_test["marital"].str.replace("?", "")
    X_test["relationship"] = X_test["relationship"].str.replace("?", "")
    X_test["race"] = X_test["race"].str.replace("?", "")
    X_test["sex"] = X_test["sex"].str.replace("?", "")
    X_test["native-ctry"] = X_test["native-ctry"].str.replace("?", "")

    Y_test = test[["50k-income"]]
    Y_test = pd.DataFrame(Y_test["50k-income"].str.replace("50K.", "50K"))    #remove . proceding 50K in test file
    Y_test = pd.DataFrame(Y_test["50k-income"].str.replace("?","na"))
    Y_test = pd.DataFrame(Y_test["50k-income"].str.replace("<=50K", "0"))
    Y_test = pd.DataFrame(Y_test["50k-income"].str.replace(">50K", "1"))
    Y_test = Y_test.astype(str).astype(int)


    
    features_to_encode = X_train.columns[X_train.dtypes==object].tolist()
    # print("y_train dtype: " + Y_train.dtypes.to_string())
    # print("before map")
    # print(Y_train)
    # income_map = {'<=50K':0, '>50K':1}
    # Y_train["50k-income"] = Y_train["50k-income"].map(income_map)
    # Y_test["50k-income"] = Y_test["50k-income"].map(income_map)
    # print("y_train dtype: " + Y_train.dtypes.to_string())
    # print("after map")
    # print(Y_train)

    #convert categorical vars
    col_trans = make_column_transformer((OneHotEncoder(handle_unknown="ignore"), features_to_encode), remainder="passthrough")
    rf_classifier = RandomForestClassifier(min_samples_leaf=50, oob_score=True, bootstrap=True, n_jobs=-1 ,random_state=50) #bootstrapping reduces variance, njobs = -1 uses all processor cores
    clf = make_pipeline(col_trans, rf_classifier)
    clf.fit(X_train, Y_train.values.ravel())

    #roc curve
    metrics.plot_roc_curve(clf, X_test, Y_test)
    plt.show()

    #hyperparameter search
    param_grid={'randomforestclassifier__max_depth': [3,5,7,10], 
    'randomforestclassifier__max_features': ["auto", "sqrt", "log2"]}
    grid_search_CV_clf = GridSearchCV(clf, param_grid, cv=7, n_jobs=-1)
    grid_search_CV_clf.fit(X_train, Y_train.values.ravel())
    Y_pred = grid_search_CV_clf.predict(X_test)
    print("F1 Score for GridSearchV")
    print(f1_score(Y_test, Y_pred, average="weighted"))

def materials_gaussian() :
    df = pd.DataFrame(pd.read_csv("superconductors.csv"))
    trainX = pd.DataFrame(df.drop('critical_temp', axis = 1).iloc[:int(21263*0.8)])
    testX = pd.DataFrame(df.drop('critical_temp', axis = 1).iloc[int(21263*0.8):])
    trainY = pd.DataFrame(df[["critical_temp"]].iloc[:int(21263*0.8)])
    testY = pd.DataFrame(df[["critical_temp"]].iloc[int(21263*0.8):])


    kernel = RBF()
    gpr = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=2)
    gpr.fit(trainX, trainY)
    y_pred, sigma = gpr.predict(testX, return_std=True)
    
    plt.figure()
    plt.scatter(x=testY, y=y_pred, label="True vs. Predicted Critical Temp")  
    plt.xlabel("Actual Temp")
    plt.ylabel("Predicted Temp")
    plt.show()
    print(f"R^2 Score: {gpr.score(testX, y_pred)}")
    print(f"Mean Absolute Error: {metrics.mean_absolute_error(y_true=testY, y_pred=y_pred)}")
    print(f"Root Means Squared Error: {metrics.mean_squared_error(y_true=testY, y_pred=y_pred, squared=False)}")

os.chdir(os.path.dirname(__file__))
fetal_health_classification()
salary_random_forest()
materials_gaussian()
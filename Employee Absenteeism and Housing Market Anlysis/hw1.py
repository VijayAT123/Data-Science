from audioop import avg
import numpy as np
import pandas as pd
import glob as glob
import os

os.chdir(os.path.dirname(__file__))


def glob_bbc_articles():
    print("---BBC ARTICLES---")
    filepath = os.getcwd() + "/BBC-textdata/bbc/**/*"
    #TODO relative filepath
    article_id = []
    paragraph_ct = []
    word_ct = []
    for file in glob.glob(filepath):
        with open (file, "r", encoding = "latin-1") as f:
            article_id.insert(len(article_id)-1, f.name.replace(os.getcwd() + "/BBC-textdata/bbc/", "").replace(".txt", ""))
            #print(f"Article id arr: {article_id}")
            lines = f.readlines()               # paragraphs
            paragraph_ct.insert(len(paragraph_ct)-1, len(lines))
            #print(f"Paragraph count: {paragraph_ct}")
            words = 0
            for line in lines:
                items = line.split()
                words += len(items)
            word_ct.insert(len(word_ct)-1, words)    # words
            #print(f"inserted into word_ct {word_ct}")
            #np.insert(data, len(data)-1, [f.name, word_ct, len(lines)])
        f.close()

    df = pd.DataFrame({'article-id': article_id,
                        'word-count': word_ct,
                        'paragraph-count': paragraph_ct}, 
                        columns=["article-id", "word-count", "paragraph-count"])
    df.to_csv("output-files/report.csv")

housing_filepath = os.getcwd() + "/housing.csv"

def numpy_houses():
    print("---HOUSING NUMPY---")
    data = np.genfromtxt(housing_filepath, delimiter=",", names = True, dtype=None) #produces a 1D NDArray due to nonhomogeneity in column data types
    ocean_prox = np.sort(data, order='ocean_proximity')
    print("Sorted Avg median house value based on ocean proximity")
    #avg median val
    #print(ocean_prox)

def pandas_houses():
    print("---HOUSING PANDAS---")
    df = pd.read_csv(housing_filepath)
    df.sort_values(by=["ocean_proximity"])
    ocean_prox_means = df.groupby(["ocean_proximity"]).mean()
    avg_house_val = ocean_prox_means["median_house_value"].sort_values(ascending=False)
    print(f"Sorted Avg median house value based on ocean proximity {avg_house_val}")
    avg_house_val.to_csv("output-files/avg_house_val_pandas.csv")

def absenteeism():
    print("---ABSENTEEISM---")
    absenteeism_fp = os.getcwd() + "/Absenteeism_at_work.csv"
    df = pd.read_csv(absenteeism_fp, delimiter=";")
    df = df.sample(frac = 1)    #shuffle rows
    print(f"Number of records: {df.count()[0]}")
    print(f"Number of attributes: {df.columns.size}")
    train = df[0:int(df.count()[0]*0.7)]
    train_small = pd.DataFrame(train.iloc[:,0:4])
    train.to_pickle("output-files/train.pickle")
    train_small.to_pickle("output-files/train_small.pickle")
    valid = df[int(df.count()[0]*0.7):int(df.count()[0]*0.7 + df.count()[0]*0.15)]
    valid_small = pd.DataFrame(valid.iloc[:,0:4])
    valid.to_pickle("output-files/valid.pickle")
    valid_small.to_pickle("output-files/valid_small.pickle")
    test = df[int(df.count()[0]*0.7 + df.count()[0]*0.15):]
    test_small = pd.DataFrame(test.iloc[:,0:4])
    test.to_pickle("output-files/test.pickle")
    test_small.to_pickle("output-files/test_small.pickle")

glob_bbc_articles()
numpy_houses()
pandas_houses()
absenteeism()
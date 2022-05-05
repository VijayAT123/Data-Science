import matplotlib
import pandas as pd
import os
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.preprocessing import MinMaxScaler
from openTSNE import TSNE as OTSNE


def plot_clustering(X_red, names, n_clusters, km, title=None):
    x_min, x_max = np.min(X_red, axis=0), np.max(X_red, axis=0)
    X_red = (X_red - x_min) / (x_max - x_min)

    plt.figure(figsize=(6, 4))
    for compound in names:
        plt.scatter(
            *X_red["compound" == compound].T,
            marker=f"${compound}$",
            s=50,
            c=plt.cm.nipy_spectral(km.labels_.astype(float)/n_clusters),
            alpha=0.5,
        )

    plt.xticks([])
    plt.yticks([])
    if title is not None:
        plt.title(title, size=17)
    plt.axis("off")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

os.chdir(os.path.dirname(__file__))
df = pd.DataFrame(pd.read_csv("thermal-dataset.csv", header=0))
categorical_feats = ["Name", "y-theory", "y-exp"]
names = df["Name"]
df.drop(labels= categorical_feats, axis=1, inplace=True)

#scale all vars
#scaling vars gives similar spread to all vars to prevent biasing
scaler = MinMaxScaler()
scaler.fit(df)
scaled = scaler.transform(df)

#elbow method for determining k
Sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(scaled)
    Sum_of_squared_distances.append(km.inertia_)
plt.plot(K, Sum_of_squared_distances, 'ks:')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()

#graph shows optimal k is ~11
n_clusters = 10 #assigned k
# n_clusters = 11 # better k
km = KMeans(n_clusters)
km = km.fit(scaled)

#visualize clusters in 2 dimensions
data_embedded = OTSNE(perplexity=30, metric="euclidean", n_jobs=-1, random_state=42, verbose=True).fit(scaled)
centers = km.cluster_centers_
transformed_centers = data_embedded.transform(centers)
centers = transformed_centers

fig, (ax1) = plt.subplots(1, 1)
colors = cm.nipy_spectral(km.labels_.astype(float) / n_clusters)
ax1.scatter(
    data_embedded[:, 0], data_embedded[:, 1], marker=".", s=30, lw=0, alpha=0.7, c=colors, edgecolor="k"
)
ax1.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="o",
    c="white",
    alpha=1,
    s=200,
    edgecolor="k"
)
for i, c in enumerate(centers):
    ax1.scatter(c[0], c[1], marker="$%d$" % i, alpha=1, s=50, edgecolor="k")
plt.show()


plot_clustering(X_red=data_embedded, n_clusters=n_clusters, km=km, title="", names=names)

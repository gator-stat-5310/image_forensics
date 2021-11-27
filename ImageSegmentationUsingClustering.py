from matplotlib.image import imread
image_path = r'C:\Users\JasSu\Documents\SHSU\pics for Inpainttool\Inpaint Pics\acrylic9.jpg'
image = imread(image_path)
print(image.shape)
X = image.reshape(-1,3)
kmeans = KMeans(n_clusters=8).fit(X)
segmented_image = kmeans.cluster_centers_[kmeans.labels_]
segmented_image= segmented_image.reshape(image.shape)
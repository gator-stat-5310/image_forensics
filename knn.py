import image_slicer
import numpy as np

base_path = r"C:\Users\JasSu\PycharmProjects\machinelearning\data"
inpaint_path = r'C:\Users\JasSu\PycharmProjects\machinelearning\data\test\dry_tree.jpg'

images = image_slicer.slice(inpaint_path, 9000, save=False)

x = np.ndarray((len(images),images[0].image.width*images[0].image.height*3), dtype=float)
y = np.zeros(len(x), dtype=np.longlong)

for i in range(0, len(images)):
    print(images[i].image.height, images[i].image.width)
    x[i] = np.array(images[i].image.getdata()).flatten()/255
    #y[i] = int(np.sqrt(np.sum(np.square(x[i]))/len(x[i])))
    y[i] = hash(np.sum(x[i]))

#print(f"y {y}")
#print(f"x {x}")

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)

#print(f"x_train {x_test}")
#print(f"y_train {y_test}")

knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(x_train, y_train)
y_test_pred = knn.predict(x_test)

print(f"training score {knn.score(x_train, y_train)}")
print(f"testing score {knn.score(x_test, y_test)}")
# print(f"confustion matrix {confusion_matrix(y_test, y_test_pred)}")
#print(f"classification matrix {classification_report(y_test, y_test_pred)}")
#print(f"test {y_test}")
#print(f"prediction {y_test_pred}")

# from sklearn.metrics import plot_confusion_matrix
# plot_confusion_matrix(knn, x_test, y_test, cmap='Greys')
import matplotlib.pyplot as plt # python plotting library
from sklearn.linear_model import LogisticRegressionCV # sklearn.linear_model -linear regression class logistic regression
from sklearn import metrics
from sklearn import datasets
digits =datasets.load_digits()
n_samples = len(digits.images)
images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]): #lets have a look at first four digits
  plt.subplot(2, 4, index + 1)#initial training set visualisation 
  plt.axis('off')
  plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
  plt.title('Training: %i' % label)
data = digits.images.reshape((n_samples, -1))#slicing images (slicing the last coloum of a 8*8 matrix)
n_samples = len(digits.images) #total no. of 8*8 matrices representing characteristics of n no. of handwritten digits
#logistics regression classifier part
classifier= LogisticRegressionCV(Cs=10,cv=5,n_jobs=4,dual=False,max_iter=100,solver='saga')
classifier.fit(data[:(n_samples) // 2], digits.target[:(n_samples) // 2])#//2 means integer division half of the nsamples from the end are used for fitting
expected = digits.target[(n_samples) //2 :]#first half of the the data is given as expected
predicted = classifier.predict(data[(n_samples) // 2:])##first half digits.tartget is predicted
print("Classification report for classifier %s:\n%s\n"% (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
  plt.subplot(2, 4, index + 5)
  plt.axis('off')
  plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
  plt.title('Prediction: %i' % prediction)
  plt.show()

# -linear-regression
LOGISTIC REGRESSION 
-The given script is an  alternative to a svm classification script used to classify hand written digits example dataset .



CLASSIFICATION REPORTS

Classification report for classifier LogisticRegressionCV(Cs=10, class_weight=None, cv=5, dual=False,
           fit_intercept=True, intercept_scaling=1.0, max_iter=100,
           multi_class='ovr', n_jobs=4, penalty='l2', random_state=None,
           refit=True, scoring=None, solver='saga', tol=0.0001, verbose=0):
             precision    recall  f1-score   support

          0       0.93      0.98      0.96        88
          1       0.91      0.89      0.90        91
          2       1.00      0.97      0.98        86
          3       0.97      0.84      0.90        91
          4       0.99      0.93      0.96        92
          5       0.88      0.92      0.90        91
          6       0.94      0.99      0.96        91
          7       0.94      0.96      0.95        89
          8       0.89      0.89      0.89        88
          9       0.85      0.93      0.89        92
 avg / total       0.93      0.93      0.93       899
          
 Classification report for classifier SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma=0.001, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False):
             precision    recall  f1-score   support

          0       1.00      0.99      0.99        88
          1       0.99      0.97      0.98        91
          2       0.99      0.99      0.99        86
          3       0.98      0.87      0.92        91
          4       0.99      0.96      0.97        92
          5       0.95      0.97      0.96        91
          6       0.99      0.99      0.99        91
          7       0.96      0.99      0.97        89
          8       0.94      1.00      0.97        88
          9       0.93      0.98      0.95        92
avg / total       0.97      0.97      0.97       899


CONCLUsION
as the results suggest svm is a better alternative to logistic regression.

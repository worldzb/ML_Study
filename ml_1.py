#环境测试
from sklearn import datasets;
from sklearn import svm




iris = datasets.load_iris();
print(iris);
digits = datasets.load_digits();
#print(digits.data);
digits.target;
digits.images[0];

clf = svm.SVC(gamma=0.001, C=100.);
clf.fit(digits.data[:-1], digits.target[:-1]);
clf.predict(digits.data[-1:]);



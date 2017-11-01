#数据导入
import numpy as np;
import urllib;
data_link = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(data_link)
data = np.loadtxt(raw_data,delimiter=",")
print(data.shape)
x = data[:,0:7]
y = data[:,8]
print(x);

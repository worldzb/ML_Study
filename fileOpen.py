import numpy as np;
import matplotlib.pyplot as plt;


my_matrix = np.loadtxt(open("./data/rand.csv","rb"),delimiter=",",skiprows=0);



if __name__=="__main__":
	np.save("random-matrix.npy", my_matrix);
	print(type(my_matrix));
	print(my_matrix);


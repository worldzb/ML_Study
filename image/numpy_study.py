import numpy as np;

def version():
	print(np.version.version);
	print("begin--------------------");

def returnArray():
	aList=[1,2,3];
	aPup=(1,2,3);
	aDict={"0":1,"1":2,"3":2}

def numArr():
	numArr=np.array([[1,2,3],[1,2,3]]);
	#numArr=np.zeros((5,5));
	return numArr;


aNP_A=np.array([[1,2,3],[1,2,3],[1,2,3]]);#矩阵A
aNP_B=np.array([[1,2,3],[1,2,3],[1,2,3]]);#矩阵B

def multip():
	aNP_c=aNP_A*aNP_B;
	return aNP_c;

def sum():
	aNP_c=aNP_A+aNP_B;
	return aNP_c;
def dot():
	aNP_c=aNP_A.dot(aNP_B);
	return aNP_c;


if __name__ == "__main__":
	print(type(dot()));
	print(dot());
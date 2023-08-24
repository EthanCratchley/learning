import numpy as np

# ----------------------------------

# Loading CSV Files:

# np.loadtxt or np.genfromtxt

#data = np.genfromtxt('filename.csv', delimiter=",", dtype=np.float32)
#print(data)
#print(data.shape)

# ----------------------------------

# Random Numbers:

#a = np.random.random((3,2)) #0-1
#print(a)

#a = np.random.randn(1000) #normal/Gaussian
#print(a.mean(), a.var())

#a = np.random.randint(3,10,size=(3,3))
#print(a)

#a = np.random.choice(5, size=10)
#print(a)

#a = np.random.choice(-8,-7,-6, size=10)
#print(a)

# ----------------------------------

# Generating Arrays: 

#a = np.zeros((2,3))
#print(a)
#print(a.dtype)

#a = np.full((2,3), 5.0)
#print(a)

#a = np.eye(3)
#print(a)

#a = np.arrange(20)
#print(a)

#a = np.linspace(0,10,5)
#print(a)

# ----------------------------------

# Copying: 

#a = np.array([1,2,3])
#b = a.copy()
#b[0] = 42
#print(b)
#print(a)

# ----------------------------------

# Data Types: 

#x = np.array([1.0,2.0], dtype=np.int64)
#print(x)
#print(x.dtype)

# ----------------------------------

# Functions and Axis: (min,max,sum,mean)

#a = np.array([[7,8,9,10,11,12,13], [17,18,19,20,21,22,23]])
#print(a)
#print(a.sum(axis=0))

# ----------------------------------

# Broadcasting:

#x = np.array([[1,2,3], [4,5,6], [1,2,3], [4,5,6]])
#a = np.array([1,0,1])
#y = x + a
#print(y)

# ----------------------------------

# Concatenation:

#a = np.array([1,2,3,4])
#b = np.array([5,6,7,8])

# hstack

#c = np.hstack((a,b))
#print(c)

# vstack

#d = np.vstack((a,b))
#print(d)

#a  = np.array([[1,2], [3,4]])
#print(a)
#b = np.array([[5,6]])
#c = np.concatenate((a,b.T), axis = 1)
#print(c)

# ----------------------------------

# Reshaping:

#a = np.arange(1,7)
# print(a)
#print(a.shape)

#b = a[np.newaxis, :]
#print(b.shape)


#b = a.reshape((2,3))
#print(b)
#print(b.shape)

# ----------------------------------

# Indexing and Slicing

#a = np.array([[1,2,3,4], [5,6,7,8]])
#print(a)

#b = a[0,1:3]
#print(b)

#b= a[:, 1]
#print(b)

#a = np.array([[1,2], [3,4], [5,6]])
#print(a)

#print(a[a>2])

#b = np.where(a>2 , a, -1)
#print(b) 

#a = np.array([10,19,30,41,50,61])
#print(a)
#even = np.argwhere(a%2==0).flatten()
#print(a[even])

# ----------------------------------

# Multidimensional (nd) arrays

#a = np.array([[1,2,6], [3,4,8]])
#print(a)
#print(a.shape)

#print(a[:,0])

#print(a.T)
#print(np.linalg.inv(a))

# ----------------------------------

# Dot Product:

#l1 = [1,2,3]
#l2 = [4,5,6]
#a1 = np.array(l1)
#a2 = np.array(l2)

# dot product
#dot = 0 
#for i in range(len(l1)):
#    dot += l1[i] *l2[i]
#print(dot)

#dot = np.dot(a1,a2)
#print(dot)

#sum1 = a1 * a2
#dot = np.sum(sum1)
#print(dot)

# ----------------------------------

# Array vs List:

#l = [1,2,3]
#a=np.array([1,2,3])

# l = l * 2
#print(l)
#a = a * 2
# print(a)

# Basics:

# a = np.array([1, 2, 3])
#print(a)
#print(a.shape)
#print(a.dtype)
#print(a.ndim)
#print(a.size)
#print(a.itemsize)

#print(a[0])
#a[0] = 10
#print(a)

#b = a * np.array([2,0,2])
#print(b)

# ----------------------------------
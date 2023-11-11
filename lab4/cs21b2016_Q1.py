import numpy as np

#create a 5X5 np array
A = np.array([[1,0.135,0.195,0.137,0.157]
     ,[0.135,1,0.2,0.309,0.143]
     ,[0.195,0.2,1,0.157,0.122]
     ,[0.137,0.309,0.157,1,0.195]
     ,[0.157,0.143,0.122,0.195,1]])
#crate a 5X1 np array
b = np.array([[0.5],[0.5],[-0.5],[-0.25],[-0.25]])
#compute the quadratic form distance
#first compute the transpose of b
bT = b.T

dist = np.sqrt(np.dot(bT,np.dot(A,b))) 

print("The quadratic form distance is: ",dist[0][0])

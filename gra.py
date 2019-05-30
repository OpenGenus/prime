import matplotlib.pyplot as plt 
  
# x axis values 
x = [10,100,1000,10000,100000,1000000] 
# corresponding y axis values 
y = [0,0,0,0,0.2,0.25] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 

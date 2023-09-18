
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

fh=pd.read_csv('scottish_hills.csv')
#print(fh.head(15))

#declare new dataframe with sorting the values in ascending form
sfh=fh.sort_values(by=['Height'], ascending=False)
print(sfh.head(5))

#graphblock1
x=fh.Height
y=fh.Latitude
plt.scatter(x,y)
plt.savefig('scatter_plt.png')
plt.show()

#graphblock2

plt.scatter(x,y, marker='x')
plt.savefig('scatter_plt.png')
plt.show()

#graphblock3

ss=linregress(x,y)
m= ss.slope
b= ss.intercept
plt.xlabel('Mount',fontsize=20)
plt.ylabel('Latitude',fontsize=15)
plt.plot(x,m*x +b,color='red')
plt.show()

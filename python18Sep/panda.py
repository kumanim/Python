import pandas as pd

s1=pd.Series([5,60,4.29,20.01])
print(s1)

hills = {'Ben Nevis': (1345, 56.79685, -5.003508),
                  'Ben Macdui': (1309, 57.070453, -3.668262),
                  'Braeriach': (1296, 57.078628, -3.728024),
                  'Cairn Toul': (1291, 57.054611, -3.71042),
                  'Sgòr an Lochain Uaine': (1258, 57.057999, -3.725416)}
print(hills)
f1=pd.DataFrame(hills)
print(f1)
#hills 2

hills2 = {'Hill Name': ['Ben Nevis', 'Ben Macdui', 'Braeriach', 'Cairn Toul', 'Sgòr an Lochain Uaine'],
                  'Height': [1345, 1309, 1296, 1291, 1258],
                  'Latitude': [56.79685, 57.070453, 57.078628, 57.054611, 57.057999],
                  'Longitude': [-5.003508, -3.668262, -3.728024, -3.71042, -3.725416]}
f3 =pd.DataFrame(hills2, columns=['Hill Name', 'Height', 'Latitude', 'Longitude'])
print(f3)

print(f3.head(2))
#tail(3)
print(f3['Height'])
print(f3.Height < 1300)

f4 = f3[f3.Height < 1300]
print(f4)

f3['Region'] = ['Grampian', 'Cairngorm', 'Cairngorm', 'Cairngorm', 'Cairngorm']
print(f3)
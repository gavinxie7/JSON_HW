import csv
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

open_file1=open("MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.csv","r")
csv_file1=csv.reader(open_file1,delimiter=",")
header_row1=next(csv_file1)

lat1=[]
lon1=[]
brt1=[]

for row in csv_file1:
    try:
        lat=float(row[0])
        lon=float(row[1])
        brt=float(row[2])
    except ValueError:
        print("Missing data")
    else:
        lat1.append(lat)
        lon1.append(lon)
        brt1.append(brt)

data1=[{
    'type':'scattergeo',
    'lon':lon1,
    'lat':lat1,
    'marker':{
        'size':[0.05*brt for brt in brt1],
        'color':brt1,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}]

my_layout=Layout(title="Australia Fires - November 2019")
fig={'data':data1,'layout':my_layout}
offline.plot(fig,filename='AustraliaFires_November_2019.html')
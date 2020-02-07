import csv
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

open_file2=open("MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2020026.csv","r")
csv_file2=csv.reader(open_file2,delimiter=",")
header_row2=next(csv_file2)

lat2=[]
lon2=[]
brt2=[]

for row in csv_file2:
    try:
        lat=float(row[0])
        lon=float(row[1])
        brt=float(row[2])
    except ValueError:
        print("Missing data")
    else:
        lat2.append(lat)
        lon2.append(lon)
        brt2.append(brt)

data2=[{
    'type':'scattergeo',
    'lon':lon2,
    'lat':lat2,
    'marker':{
        'size':[0.05*brt for brt in brt2],
        'color':brt2,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}]

my_layout=Layout(title="Australia Fires - January 2020")
fig={'data':data2,'layout':my_layout}
offline.plot(fig,filename='AustraliaFires_January_2020.html')
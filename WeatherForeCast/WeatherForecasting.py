import requests
import webbrowser
import os
from time import strftime, localtime
from datetime import datetime

APPID='33c14d3d4f9e8a90725d6859ba58021a'


print "Enter Country :"
country=raw_input()

print "Enter City Belongs To Country"
city=raw_input()
url ="http://api.openweathermap.org/data/2.5/weather?q="+city+","+country+"&APPID=33c14d3d4f9e8a90725d6859ba58021a"
print "URL", url
response=requests.get(url)
print "response ",response
JsonData=response.json();
Temp=JsonData['main']
Pressure=Temp['pressure']
Temperature=Temp['temp']-273.15
Humidity= Temp['humidity']

WheatherDescription=JsonData['weather']
Sunrise=JsonData['sys']['sunrise']
Sunset=JsonData['sys']['sunset']

print "Wheather Condition For ",city," In (",country,")";
print "Pressure :",Pressure," Pascal "
print "Temperature :",Temperature," Degree"
print "Humidity : ",Humidity," Hygrometer  "

Sunrise=strftime('%H:%M:%S',localtime(Sunrise)) 
Sunset=strftime('%H:%M:%S',localtime(Sunset))

print "Sunrise :",Sunrise
print "Sunset :",Sunset



WheatherDescription=WheatherDescription[0]['description']
print "Wheather Description :",WheatherDescription

htmlDisplay="<!DOCTYPE html>"\
"<html>"\
"<body>"\
"<marquee><h2  style='background-color:MediumSeaGreen;' align='center'> Current Wheather Information For ,"+city+" City Inside  In ("+country+") Country <h2> </marquee>"\
"<h3 style='background-color:Gray;' align='center'>  Temperature :"+str(Temperature)+" Degree</h3>"\
"<h3 style='background-color:Orange;' align='center'> Pressure :"+str(Pressure)+"  Pascal </h3>"\
"<h3 style='background-color:Gray;' align='center'>  Humidity : "+str(Humidity)+" Hygrometer </h3>"\
"<h3 style='background-color:Orange;' align='center'>  Sunrise  Was Happened In Morning at : "+str(Sunrise)+" </h3>"\
"<h3 style='background-color:Gray;' align='center'>  Sunset  Will Be Happened In Evening at : "+str(Sunset)+" </h3>"\
"<h3 style='background-color:Orange;' align='center'>  Wheather Condition : "+WheatherDescription+" </h3>"\
"</body>"\
"</html>"

fileName='htmlWhetaherData.html'
f= open(fileName,'w')
f.write(htmlDisplay)
f.close()

fileNamePath='file://'+os.getcwd()+"/"+fileName
flag=webbrowser.open_new_tab(fileNamePath)


print "Browser Will Open and the flag value is :",flag

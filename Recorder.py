#!/usr/bin/python
import os
import pygame, sys
import csv
from pygame.locals import *
import serial
import time
import shutil,os # copy paste icin

foldername = '/home/pi/Desktop/GPSTRACKERPROJECT/SystemFile/foldername.csv' # GpsTracker.py tarafindan .csv dosyasina kaydedilen time etiketi aliniyor
folderfile=open(foldername,'r')
getthetime=folderfile.read()
folderfile.close()

koor ='/home/pi/Desktop/GPSTRACKERPROJECT/Koordinatlar/'+getthetime+'.csv' #GpsTracker.py tarafindan kaydedilen lat long dosyasi okunacak
kml1 = '/home/pi/Desktop/GPSTRACKERPROJECT/SystemFile/GPSDATAFORMAT.kml' # Dizinde bulunan sablon teskil eden kml dosyasi okunacak
kml2 = '/home/pi/Desktop/GPSTRACKERPROJECT/TrackingResults/'+getthetime+'.kml' # Son kullaniciya verilece olan kml dosyasi kaydedilecek
originalusb = '/home/pi/Desktop/GPSTRACKERPROJECT/TrackingResults/' # bu dizinde bulunan dokumanlar .... (alt satir devami)
targetusb = '/media/pi/MC/TrackingResults' # MC isimli flash bellege kaydedilecek

gettime = time.strftime("%M%S") # Suanki Zaman etiketi aliniyor Dakika ve Saniye
#Okunan zaman etiketine bakilarak istenen dakika araliklariyla veya surekli olarak MC isimli flash bellege kopyalaniyor simdilik 10dakika araliklara ayarli
if gettime == '0000' or gettime == '1000' or gettime == '2000' or gettime == '3000' or gettime == '4000' or gettime == '5000':
 shutil.copytree(originalusb,targetusb) #pathte bulunan hersey kopyalaniyor

dosyakoor = open(koor,"r")
dosyakml1 = open(kml1,"r")
dosyakml2 = open(kml2,"w")

koordizi = dosyakoor.readlines() # lat longlarin oldugu csv dosyasi satir satir okundun
kml1dizi = dosyakml1.readlines() # sablon teskil eden kml dosyasi okundu 

totalbyte=dosyakoor.tell() # lat longlarin oldugu dosyanin kac byte oldugu bilgisi
dosyakoor.seek(0) # lat longlarin oldugu dosyada cursoru 0 inci konuma getir
koorbaslon=dosyakoor.read(9) # 9 byte oku, bu 9 byte baslangic longitude'u
dosyakoor.seek(10) # cursoru 10uncu byte gotur
koorbaslat=dosyakoor.read(9) # 9 byte daha oku bu 9byte baslangic latitude'u

dosyakoor.seek(totalbyte-22) # cursoru sondan 22inci byte gotur, lat long uzunluklari .6 formatta yazildigi icin bu 22 fix
koorsonlon=dosyakoor.read(9) # 9 byte oku bu 9 byte bitis longitude'u
dosyakoor.seek(totalbyte-12) # cursoru sondan 12nci byte gotur , 
koorsonlat=dosyakoor.read(9) # 9 byte oku bu 9 byte bitis latitude 'u

#FINAL KML DOSYASININ GEREKLI YERLERINE BU BASLANGIC BITIS VE ROTA LAT LONGLARI YAZILMAK UZERE DUZENLENIYOR
kml1dizi[82]= "<longitude>" + koorbaslon + "</longitude>" + "\n"
kml1dizi[83]= "<latitude>" + koorbaslat+ "</latitude>" + "\n"
kml1dizi[93]= "<coordinates>" + koorbaslon + "," + koorbaslat + ",0" "</coordinates>"+ "\n"

kml1dizi[100]= "<longitude>" + koorsonlon + "</longitude>" + "\n"
kml1dizi[101]= "<latitude>" + koorsonlat+ "</latitude>" + "\n"
kml1dizi[111]= "<coordinates>" + koorsonlon +","+ koorsonlat + ",0" "</coordinates>" + "\n"

elemansayisi=len(koordizi)

kml1dizi[75] = koordizi[0] + "\n" # rotayi iceren tum lat longlar kml dosyasinda ilgili yere yazildi.


for x in kml1dizi: #FINAL KML DOSYASI OLUSTURULUYOR 
 dosyakml2.write(str(x))


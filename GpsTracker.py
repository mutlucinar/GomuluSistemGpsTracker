#!/usr/bin/python
import os
import pygame, sys
import csv
from pygame.locals import *
import serial
import time
#initialise serial port on /serial0
ser = serial.Serial('/dev/serial0',9600,timeout = None)
# set font size MAX 100
fontsize = 50

# calculate window size
width = fontsize * 20
height = fontsize + 10

# initilaise pygame
pygame.init()
windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
fontObj = pygame.font.Font('freesansbold.ttf',fontsize)
pygame.display.set_caption('GPS Location')
redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
yellowColor = pygame.Color(255,255,0)
blackColor = pygame.Color(0,0,0)

getthetime = time.strftime("%Y%m%d%H%M%S") #GpsTracker.py Calistigi andaki zaman etiketi YilAyGunSaatDakikaSaniye
names ='/home/pi/Desktop/GPSTRACKERPROJECT/Koordinatlar/'+getthetime+'.csv' #Lat ve Long Bilgisi bu zaman etiketi ismiyle acilan csv dokumanina kaydedilmek uzere adresi belirtiliyor.


foldername = '/home/pi/Desktop/GPSTRACKERPROJECT/SystemFile/foldername.csv' # Acilan zaman etiketi bu foldername.csv isimli dokumana daha sonra Recorder.py tarafindan kullanilmak uzere kaydedilecek.
folderfile=open(foldername,'w')
folderfile.write(getthetime)
folderfile.close()

fix = 1
color = redColor
#Sonsuz Dongu
x = 0
while x == 0:
   
   # Tum NMEA cumleleri seri okunuyor ve ekrana yaziliyor    
   gps = ser.readline()
   print gps
   
    
   # check gps fix status #GPGSA dan 2D yada 3D fix bilgisi aliniyor 2d ise ekrana sari, 3d ise yesil font ile yazilar yaziliyor
   if gps[1:6] == "GPGSA":
      fix = int(gps[9:10]) 
      if fix == 2:
         color = yellowColor
      if fix == 3:
         color = greenColor
         
   # Zaman, Lat, Long bilgisi GPGGA cumlesinden decode ediliyor lat and long from #GPGGA string
   if gps[1 : 6] == "GPGGA":
       # clear window
       pygame.draw.rect(windowSurfaceObj,blackColor,Rect(0,0,width,height))
       pygame.display.update(pygame.Rect(0,0,width,height))
       # get time
       time = gps[7:9] + ":" + gps[9:11] + ":" + gps[11:13]
              
       # if 2 or 3D fix and if lat,long == integer,  get lat and long eger lat long elemanlarinin integer olduklari kontrol edilmezse ,virgul, gelip programi crack edebiliyor
       if fix > 1 and ord(gps[31]) >47 and ord(gps[31]) <58 and ord(gps[32]) >47 and ord(gps[32]) <58 and ord(gps[33]) >47 and ord(gps[33])<58 and ord(gps[34]) >47 and ord(gps[34])<58 and ord(gps[36]) >47 and ord(gps[36])<58 and ord(gps[37]) >47 and ord(gps[37])<58and ord(gps[38]) >47 and ord(gps[38])<58 and ord(gps[39]) >47 and ord(gps[39])<58 and ord(gps[40]) >47 and ord(gps[40])<58 and ord(gps[17]) >47 and ord(gps[17])<58 and ord(gps[18]) >47 and ord(gps[18])<58 and ord(gps[19]) >47 and ord(gps[19])<58 and ord(gps[20]) >47 and ord(gps[20])<58 and ord(gps[22]) >47 and ord(gps[22])<58 and ord(gps[23]) >47 and ord(gps[23])<58 and ord(gps[24]) >47 and ord(gps[24])<58 and ord(gps[25]) >47 and ord(gps[25])<58 and ord(gps[26]) >47 and ord(gps[26])<58:
       
          print "LATITUDE DMM"
          print gps[17:19] + "." + gps[19:21] +"."  + gps[22:27] 
          print "LONGITUDE DMM"
          print gps[31:33] + "." + gps[33:35] +"."+ gps[36:41] 
          
          #DMM TO DD , FOR GOOGLE EARTH'S KML FILE
          lond=int(gps[31:33])     
          lonm=float(gps[33:35])
          lons=float(gps[36:41])/100000
          lonmm=(lonm+lons)/60
          londd=float(lond+lonmm)
          londd=format(londd,'.6f')
          print "LONGITUDE DD"
          print londd
               
          latd=int(gps[17:19])
          latm=float(gps[19:21])
          lats=float(gps[22:27])/100000
          latmm=(latm+lats)/60 
          latdd=float(latd+latmm)
          latdd=format(latdd,'.6f')
          print "LATITUDE DD"
          print londd 
          
          # LAT LONG BILGISI ZAMAN ETIKETIYLE ACILAN DOSYAYA YAZILIYOR
          file=open(names,'a')
          # file.write(time)
          file.write(str(londd))
          file.write(',')
          file.write(str(latdd))
          file.write(',0 ') #altitude bilgisi otomatik 0 yazildi gercek bilgi alinabilir
       
          #file.write("\n")
          file.close      
                 
       # if no fix
       else:
         latdd = "" # No Valid Data 
         londd = ""
         
       # print new values   EKRANDA YAZIYOR
       msgSurfaceObj = fontObj.render(str(time), False,color)   
       msgRectobj = msgSurfaceObj.get_rect()
       msgRectobj.topleft =(2,0)
       windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
       
       msgSurfaceObj = fontObj.render(str(latdd), False,color)   
       msgRectobj = msgSurfaceObj.get_rect()
       msgRectobj.topleft =(210,0)
       windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)

       msgSurfaceObj = fontObj.render(str(londd), False,color)   
       msgRectobj = msgSurfaceObj.get_rect()
       msgRectobj.topleft =(580,0)
       windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
       pygame.display.update(pygame.Rect(0,0,width,height))
       fix = 1
       color = redColor
       # Recorder.py calistiriliyor, recorder calistiktan sonra tekrar burdan devam ediliyor
       os.system('python Recorder.py')

       
     
   # check for ESC key pressed, or GPS Location window closed, to quit
   for event in pygame.event.get():
       if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
              #os.system('python yazma.py')
              pygame.quit()
              sys.exit()
              
              
             

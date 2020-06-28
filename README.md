# GomuluSistemGpsTracker
Bu proje Gömülü Sistemler Dersi için hazırlanmıştır.

Yazılım, Rasbian işletim sisteminde (default) yüklü olarak gelen Geany platformunda Python 2.7 diliyle yazılmıştır.

1. Aşağıdaki Youtube Linkinde Projemi detaylı olarak sunduğum video bulunmaktadır. (Sunum videosu)                                     
https://youtu.be/85GnNSOCazk

2. Aşağıdaki Youtube Linkinde daha sunum yüzeysel olarak, yazılım daha detaylı olarak anlatılmıştır. (Proje uygulama/anlatma videosu)
https://www.youtube.com/watch?v=lTHlNa3zy18&feature=youtu.be


Kullanılan Malzemeler

1 adet Raspberry Pi 3 B+ (Raspbian işletim sistemi yüklü)

1 adet GY-NEO6MV2 Modülü Bulunan GPS Alıcı Sistemi

1 adet 10000mAh Powerbank

1 adet 16gb MicroSd kart



PROJEYİ UYGULAMASI
Videoda açıkladığım projemin tüm dokümanları GitHub'a yüklemiş bulunmaktayım ve projenin nasıl uygulamaya döküleceğini videolarda anlatmış bulunmaktayım ama yinede videoları uzun uzun izlemek istemeyenler için kısaca bu projeyi nasıl gerçekleyebileceğinizden bahsetmek istiyorum.
Yukarıda bahsettiğim malzemeleri temin etmeniz gerekmekte. Raspberry pi3b+ yerine sizde bulunan seri haberleşme yapabilen bir donanımda olabilir.



DONANIMLARIN BAĞLANTISI







1-) Raspbian İşletim sistemini Sd karta yükle.
2-) Güncelemeleri gerçekleştir.
3-) Donanım Bağlantılarını gerçekleştir.
4-) Raspberry Pi için Python GPIO kütüphanesini kur.
    Kurulum için :
        -wget https://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.11.tar.gz
        - tar -xvf RPi.GPIO-0.5.11.tar.gz
        - cd RPi.GPIO-0.5.11
        - sudo python setup.py install
5-)Standart USB webcam kütüphanesini kur.
    Kurulum için :
        - sudo apt-get install fswebcam
6-) SSMTP kütüphanesini kur.
    Kurulum için:
        - sudo apt-get install ssmtp
        - sudo apt-get install mailutils
        - sudo nano /etc/ssmtp/ssmtp.conf




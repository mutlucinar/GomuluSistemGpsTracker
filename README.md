# GomuluSistemGpsTracker
Bu proje Gömülü Sistemler Dersi için hazırlanmıştır.
GITHUB sayfasının hazırlanmasındaki amaç   : Projeyi uygulamak isteyen bir kişinin kolay yoldan uygulayabilmesi için gerekli herşeyin (kodlar, dokümanlar vs.) tek bir kaynak üzerinden sunulmasıdır. Bu kapsamda kullanılan tüm kodlar, sunum dosyaları, dokümanlar ve uygulama/anlatım videoları vs. bu sayfada paylaşılmıştır.

## Projeyi Uygulamak/Gerçekleştirmek
Projeyi uygulamak istiyorsanız, EK'teki tüm dokümanları indirip, aşağıda linklerini verdiğim videolar izlemeniz ve uygulamanız yeterlidir. Ancak ikinci bir seçenek olarak videoları izlemeden yalnızca github sayfasını okuyarak gerçekleştirmek isteyenler için aşağıda bir bölüm daha oluşturdum.

## Videoları İzleyerek Projeyi Gerçekleştirmek

1. Aşağıdaki Youtube Linkinde Projemi detaylı olarak sunduğum video bulunmaktadır. (Sunum videosu)                                     
https://youtu.be/85GnNSOCazk

2. Aşağıdaki Youtube Linkinde daha sunum yüzeysel olarak, yazılım daha detaylı olarak anlatılmıştır. (Proje uygulama/anlatma videosu)
https://www.youtube.com/watch?v=lTHlNa3zy18&feature=youtu.be

3. Yukarıdaki linkini paylaştığım videolarda kullandığım sunum GITHUB sayfasına eklenmiştir.

4. Projede kullanılan tüm kodlar yine GİTHUB sayfasına eklenmiştir.



## Videoları Uzun Uzun İzlemeden  GITHUB Sayfasını Okuyarak Projeyi Gerçekleştirmek :)
Öncelikle aşağıda yazan malzemeleri temin etmeniz gerekmekte. Raspberry pi3b+ yerine sizde bulunan seri haberleşme yapabilen bir  olabilir. Ben bu projede mobiliteyi sağlayabilmek için harici güç sağlayabilen bir powerbank tercih ettim. Geliştirme aşamasında powerbank'a ihtiyacınız olmayabilir.

### Kullanılan Malzemeler

1 adet Raspberry Pi 3 B+ (Raspbian işletim sistemi yüklü)

1 adet GY-NEO6MV2 Modülü Bulunan GPS Alıcı Sistemi

1 adet 10000mAh Powerbank

1 adet 16gb MicroSd kart

### Kodları Yazmak İçin Gerekli Yazılım
Yazılım, Rasbian işletim sisteminde (default) yüklü olarak gelen Geany platformunda Python 2.7 diliyle yazılmıştır.

### İşletim Sistemi
Raspbian İşletim Sistemi. Siz aşina olduğunuz/istediğiniz işletim sistmini kullanabilirsiniz.

## Proje Uygulama Adımları
1. Raspbian İşletim sistemini Sd karta yükle ve Raspberry Pi'ye tak. Raspbian işletim sistemini (https://www.raspberrypi.org/downloads/) adresinde bulabilirsiniz. 

2. Güncelemeleri gerçekleştir. Aslında güncelleme yapmak için bir iki komut (sudo apt-get update) yazmak yeterli. Ama detaylı bilgiye ihtiyacınız varsa (https://www.raspi-tr.com/2012/08/04/raspberry-pi-firmware-guncelleme/) ve (https://siberoloji.github.io/apt-get-update-upgrade-dist-upgrade-farki-nedir/) adreslerini inceleyebilirsiniz.

3. Donanımsal bağlantıları yap. Bunun için GY-NEO6MV2' modülünün Vcc ve GND bağlantılarını Pi'nin ilgili pinlerine bağladıktan sonra yine TX ve RX pinlerini  Pi'nin seri haberleşme yapabildiği pinlerine (GPIO 8 ve 10 )takmanız yeterli.
Sizler için GY-NEO6MV2 modülü ve Pi 3b+'ın Pinout resimlerini aşağıda paylaşıyorum.
![gy-neo6mv2-gps-modulu-ucus-kontrol-sistem-gpsi-2103-82-B](https://user-images.githubusercontent.com/64988971/85951275-cd48e580-b96a-11ea-992e-9a7066cb3bd2.jpg)
![GPIO-Pinout-Diagram-2](https://user-images.githubusercontent.com/64988971/85951278-cf12a900-b96a-11ea-859f-c6f9ac24b8cf.png)
İşte bu da benim gerçekleştirdiğim bağlantının resmi ;
![WhatsApp Image 2020-06-28 at 17 41 19](https://user-images.githubusercontent.com/64988971/85951459-00d83f80-b96c-11ea-8444-eb3bd8583101.jpeg)

![11111](https://user-images.githubusercontent.com/64988971/85951622-f1a5c180-b96c-11ea-979a-6a166f816bc0.PNG)

4. GITHUB sayfasına yüklediğim tüm dosyaları indir (hepsi bir klasörde olsun).

5. Terminal ekranından 4.maddede indirmiş olduğun klasöre git (cd komutuyla). Bu arada Linux işletim sistemine yabancıysanız (https://wiki.ubuntu-tr.net/index.php?title=Temel_Linux_komutlar%C4%B1) adresindeki temel komutları inceleyebilirsiniz.

6. 



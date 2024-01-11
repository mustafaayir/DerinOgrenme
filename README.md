# DerinOgrenme
 Derin Öğrenme Final Proje Ödevi

ℹ Dersin Adı: DERİN ÖĞRENME



## Grup Bilgileri

| Öğrenci No | Adı Soyadı           | Bölüm          		   | Proje Grup No | Grup Üyelerinin Github Profilleri                 |
|------------|----------------------|--------------------------|---------------|---------------------------------------------------|
| 5200505024  | Sezen Mutlu		     | Yazılım Mühendisliği     | PROJE_1       | [Github](https://github.com/kadirova59)      |
| 1180505044  | Mustafa Ayır      | Yazılım Mühendisliği     | PROJE_1       | [GitHub](https://github.com/mustafaayir)     |
| 1190505029  | Musa Güney        | Yazılım Mühendisliği     | PROJE_1       | [Github](https://github.com/musaguney)       |
| 1190505623  | Berkant Yurtsever | Yazılım Mühendisliği     | PROJE_1       | [GitHub](https://github.com/Eneston)         |


---

## Proje Açıklaması
Bu projede ANN,CNN, Transfer Learning, Test-Train-Val kullanılmıştır. Projenin amacı, verilen veri setindeki XRAY görüntülerini işleyerek hastanın viral sebeplerden mi yoksa bakteriyel sebeplerden mi hastalandığını anlamak ve XRAY görüntüsünün hangi hastalığa işaret ettiğini belirlemektir. Projeyi başlatmak için Google Drive içerisine incelenecek veri setini yüklemek gereklidir. Daha sonra Colab üzerinden Drive'a bağlanıp veri seti üzerinde işlemler gerçekleştirilir.


---

## Proje Dosya Yapısı

Projenizin dosya yapısını açıklayan bir bölüm ekleyebilirsiniz. Örneğin:
- */src*
  - */components*
    - ANN.ipynb
    - CNNModelClassificationReport.ipynb
    - CNNModelininDogrulukOranı.ipynb
    - TestModel75.ipynb
    - TestModel80.ipynb
    - TransferLearning.ipynb
- */public*
  - ANN.py
  - CNNModelClassificationReport.py
  - CNNModelininDogrulukOranı.py
  - testmodel75.py
  - testmodel80.py
  - TransferLearning.py
- */images*
  - ANN_ModelDegerlendirme.png
  - ANN_Sonuçlar.png
  - CNNDogrulukOranı.png
  - CNNModelClassificationReport.png
  - TestModel75.jpg
  - testmodel80.jpg
  - TransferLearning.jpeg
  - TransferLearningModel.jpeg
  - TransferLearningTestDogrulukOranı.jpeg
- README.md


---

## Kurulum

Projeyi GitHub aracılığıyla bilgisayarınıza klonlayın ve içerisindeki ".ipynb" dosya uzantılı dosyaları Colab ortamında çalıştırın. Kodların çalışabilmesi için Phunemunia/XRAY dosyalarının drive'a yüklenmesi gerekmektedir.

Kullanılan Kütüphaneler:

os kütüphanesi
numpy kütüphanesi
keras.preprocessing kütüphanesinden image
keras.preprocessing.image kütüphanesinden ImageDataGenerator
keras.models kütüphanesinden Sequential
keras.layers kütüphanesinden Conv2D, MaxPooling2D, Flatten, Dense, Dropout
keras.applications kütüphanesinden VGG16
keras.optimizers kütüphanesinden Adam
torch
torch.nn
torch.optim
torchvision kütüphanesinden datasets, transforms
torch.utils.data kütüphanesinden DataLoader
sklearn.metrics kütüphanesinden accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

---

## Kullanım

Veri seti Drive'a yüklenir.
Colab ortamında ilgili kod açılır. (ANN, CNN, TransferLearning...)
Veri setinin kod içerisinde okunabilmesi için veri setinin olduğu dosyanın yolu kopyalanır.("...content/MyDrive/Phenomuia/XRAY" gibi)
Veri setinin yolu kod içerisindeki path kısmına yapıştırılır.
Değiştirilmek istenirse örnek olarak train, test, validation gibi parametreler belirlenir ve kod çalıştırılır.
Modelin derlenmesi, eğitilmesi, test edilmesi gibi işlemler kod akışına göre ilerler. Eğitilen sonuç ve test doğruluk oranları gibi değerler ekrana yazdırılır.

---

## Katkılar

Proje yapımında stackoverflow, chatgpt, blackboxai ve ilgili kütüphanelerin dökümantasyonları kullanılmıştır.

---

## İletişim

<br/>
5200505024@ogr.klu.edu.tr  | Sezen Mutlu
<br/>
1180505044@ogr.klu.edu.tr  | Mustafa Ayır
<br/>
1190505029@ogr.klu.edu.tr  | Musa Güney
<br/>
1190505623@ogr.klu.edu.tr  | Berkant Yurtsever

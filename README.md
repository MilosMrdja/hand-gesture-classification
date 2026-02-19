# hand-gesture-recognition

# Tim
**Milos Mrdja SV34/2022**

# Asistent
**Dragan Vidaković**

## Definicija problema
Klasifikacija slike u jednu od unapred definisanih kategorija, gde svaka kategorija predstavlja jedinstveni gest ruke. Ovo je ključni korak ka budućoj implementaciji sistema koji bi mogao raditi u realnom vremenu, npr. za interakciju sa uređajima ili aplikacijama bez dodira.

## Motivacija problema
Motivacija za rešavanje ovog problema je razvoj modela koji može da izvrši preciznu i brzu klasifikaciju gestova ruke, što je korisno za aplikacije u realnom vremenu kao što su kontrola uređaja ili softverskih interfejsa gestovima ruke, sistemi za pomoć osobama sa invaliditetom.  
Iako trenutna implementacija radi sa statičnim slikama, cilj projekta je da postavi temelje za buduće real-time prepoznavanje, pri čemu model treba da zadrži visoku tačnost i pouzdanost.

## Skup podataka
Skup podataka čini 24,000 slika podeljenih u 20 kategorija. Svaka kategorija sadrži 900 slika za trening i 300 slika za testiranje.  
Skup je preuzet sa Kaggle-e sajta:  
[Hand Gesture Recognition Dataset](https://www.kaggle.com/datasets/aryarishabh/hand-gesture-recognition-dataset/data)

## Metodologija
Za razvoj modela koristi se **Transfer Learning**, što znači da će se iskoristiti već unapred obučeni konvolucioni neuronski model kao osnova koristeći određenu biblioteku (PyTorch / TensorFlow / Keras), a samo će se dodatno prilagoditi specifičnim gestovima ruke.

## Evaluacija
Za evaluaciju modela koristiće se sledeće metrike:  
- **F1 Score**  
- **Recall**  
- **Accuracy**  
- **Precision**

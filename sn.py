import requests
from bs4 import BeautifulSoup
from bs4 import Comment

url = input("url'i girin : ")

#htp(s) Kontrolü
if not url.startswith("https://") and not url.startswith("http://") :
  url=u."http://"+url
response = requests.get(url)
soup=BeautifulSoup(response.text , 'html.parser')

print("""
                        ne istersin ?
     1.tüm '<a>' etiketleri     2.Yorum satırlarını bulma
     3.tüm başlıklar (h1,h2...) 4.tüm javascript kodları
     5.hassas dosyalar (.php,.sql,.asp,...)

""")
secim=int(input("seçimin : "))

#Linkleri Bulma
if secim == 1 :
  for link in soup.find_all('a'):  
    print(link.get('href'))

#Yorum Satırlarını Bulma
elif secim == 2 :
  yorumlar = soup.find_all(string=lambda text: isinstance(text, Comment))

  if not yorumlar:
    print("[-] Bu sayfada hiç HTML yorum satırı bulunamadı.")
  else:
    for yorum in yorumlar:
      print(f"Bulunan Yorum: {yorum}")



#Başlıkları Bulma
elif secim == 3 :
  for baslik in soup.find_all(['h1','h2','h3','h4','h5','h6']) :
    print(baslik.text.strip())
#JS Kodları Traması
elif secim == 4 :
  scriptler = soup.find_all('script')
  for script in scriptler:
    if script.get('src'):
      # Dışarıdan bağlanan .js dosyaları
      print(f"Dış JS Dosyası: {script.get('src')}")
    else:
      # Doğrudan HTML içindeki JS kodları
      print("--- Dahili JS Kodu ---")
      print(script.string)
      print("----------------------")

#Hassas Dosya Taraması
elif secim == 5 :
  hassas_uzantilar = (".php", ".asp", ".aspx", ".jsp", ".env", ".sql", ".zip", ".bak")
  for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.endswith(hassas_uzantilar):
      print(f"[!] Hassas olabilecek bir dosya bulundu: {href}")

  
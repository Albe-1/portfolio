import requests
import json
import xml.etree.ElementTree as ET

class Dog:
    def __init__(self, breed, subbreeds, image_url):
        self.breed = breed
        self.subbreeds = subbreeds
        self.image_url = image_url

    def to_dict(self):
        return {
            "breed": self.breed,
            "subbreeds": self.subbreeds,
            "image_url": self.image_url
        }

dog_lists = []

r = requests.get(f"https://dog.ceo/api/breeds/list/all")   

if r.status_code == 200:
    data = r.json()
    dizionario_razze = data["message"]
    lista_razze = list(dizionario_razze.keys())

    for i in range(0,10,1):
        razza = lista_razze[i]
        sottorazze = dizionario_razze[razza]
        print(f"{i+1}. {razza}: {sottorazze}")

        image_requests = requests.get(f"https://dog.ceo/api/breed/{razza}/images/random")

        if image_requests.status_code == 200:
            image_data = image_requests.json()
            image_url = image_data["message"]
            print(f"{image_url}")
        else:
            print("Errore nel recupero dell'immagine")

        dog = Dog(breed = razza, subbreeds = sottorazze, image_url = image_url)
        dog_lists.append(dog)            
    
else:
    print("Errore nella richiesta API")

numero_razze = len(dog_lists)
media_sottorazze = sum(len(d.subbreeds) for d in dog_lists) / numero_razze
lista_alfabetica_razze = sorted([d.breed for d in dog_lists])

dogs_data = {
    "numero razze": numero_razze,
    "media sottorazze": media_sottorazze,
    "lista_alfabetica_razze": lista_alfabetica_razze,
    "dogs": [d.to_dict() for d in dog_lists]
}

with open("dogs_data.json", "w") as file:
    json.dump(dogs_data, file, indent=4)

for d in dog_lists:
    print(f"{d.breed}, {d.subbreeds}, {d.image_url}")


root = ET.Element("cane")
ET.SubElement(root, "numero razze").text = str(numero_razze)
ET.SubElement(root, "media delle sottorazze").text = str(media_sottorazze)
lista_razze_elem = ET.SubElement(root, "lista_alfabetica_razze")
for razza in lista_alfabetica_razze:
    ET.SubElement(lista_razze_elem, "razza").text = razza

dogs_elem = ET.SubElement(root, "dogs")
for dog in dog_lists:
    dog_elem = ET.SubElement(dogs_elem, "dog")
    ET.SubElement(dog_elem, "breed").text = dog.breed

    sub_elem = ET.SubElement(dog_elem, "subbreeds")
    for s in dog.subbreeds:
        ET.SubElement(sub_elem, "subbreed").text = s

    ET.SubElement(dog_elem, "image_url").text = dog.image_url if dog.image_url else ""

tree = ET.ElementTree(root)

tree.write("dogs_data.xml", encoding="utf-8", xml_declaration=True)

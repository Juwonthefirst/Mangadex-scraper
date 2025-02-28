import requests, sys, os
from pyinputplus import inputYesNo


class Mangadex:
    def __init__(self, name, lang="en"): 
        self.name = name
        self.lang = lang
        self.manga_title = None
        self.manga_description = None
        self.length = 0
        
    def search(self):
        name = self.name.split()
        name_url="%20".join(name)
        url=f"https://api.mangadex.org/manga?limit=100&title={name}&includedTagsMode=AND&excludedTagsMode=OR&contentRating%5B%5D=safe&contentRating%5B%5D=suggestive&contentRating%5B%5D=erotica&order%5BlatestUploadedChapter%5D=desc"
        manga_json=requests.get(url)
        manga_json.raise_for_status
        manga_data=(manga_json.json())["data"]
        if manga_data==[]:
        	print("This manga doesn't exist")
       		sys.exit()
    	self.manga_title=manga_data[0]["attributes"]["title"][lang]
    	self.manga_description=manga_data[0]["attributes"]["description"][lang]
        manga_id=manga_data[0]["id"]
        self.length = 1
    	return manga_id

    def __str__ (self): 
        return f"{self.manga_title}\n {self.manga_description}"
  
    def get_chapters(self, manga_id): 
        url=f"https://api.mangadex.org/manga/{manga_id}/aggregate?translatedLanguage%5B%5D={self.lang}"
        chapters_json = requests.get(url)
        chapters_json.raise_for_status
        chapters=(chapter_json.json())["volumes"]["none"]["chapters"]
    	chapter_ids={float(num) : chapter["id"] for num,chapter in chapters.items()}
    	self.length = len()
    	return chapter_ids
    	
    def __len__ (self): 
        return self.length
import requests, sys, os
from pyinputplus import inputYesNo


class Mangadex:
    def __init__(self, name, lang="en"): 
        self.name = name
        self.lang = lang
        
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
	    manga_title=manga_data[0]["attributes"]["title"][lang]p
    	manga_description=manga_data[0]["attributes"]["description"][lang]
	    manga_id=manga_data[0]["id"]
    	return (manga_title,manga_description,manga_id)
    
    
    def get_chapter_id(self,manga_id):
    
    
  

        
import requests,sys
from pyinputplus import inputYesNo
# function to get manga details
def search_for_manga(manga): 
	name=manga.split()
	name="%20".join(name)
	url=f"https://api.mangadex.org/manga?limit=100&title={name}&includedTagsMode=AND&excludedTagsMode=OR&contentRating%5B%5D=safe&contentRating%5B%5D=suggestive&contentRating%5B%5D=erotica&order%5BlatestUploadedChapter%5D=desc"
	manga_json=requests.get(url)
	manga_json.raise_for_status
	manga_data=(manga_json.json())["data"][0]
	manga_title=manga_data["attributes"]["title"]["en"]
	manga_description=manga_data["attributes"]["description"]["en"]
	manga_id=manga_data["id"]
	return manga_title,manga_description,manga_id


#function to get chapter id
def get_chapters(manga_id):
	url=f"https://api.mangadex.org/manga/{manga_id}/aggregate?translatedLanguage%5B%5D=en"
	chapter_json=requests.get(url)
	chapter_json.raise_for_status
	chapters=(chapter_json.json())["volumes"]["none"]["chapters"]
	chapter_ids={float(num) : chapter["id"] for num,chapter in chapters.items()}
	return chapter_ids

#function to download pages per chapter
def download_pages(chapter_ids):
	for num,chapter in sorted(chapter_ids.items()):
		choice=inputYesNo("We are creating a new folder for your are you sure you want to continue (yes/no): ").lower()
		if choice == "no":
			print("Quiting program........")
			sys.exit()
		print("we still in")

		
title, description, id=search_for_manga("Nan Hao and Shang Feng")
chapter_ids=get_chapters(id)
download_pages(chapter_ids)
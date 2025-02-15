import requests,sys,os
from pyinputplus import inputYesNo


# function to get manga details
def search_for_manga(manga,lang="en"):
	name=manga.split()
	name="%20".join(name)
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
			


#function to get chapter id
def get_chapters(manga_id,lang="en"):
	url=f"https://api.mangadex.org/manga/{manga_id}/aggregate?translatedLanguage%5B%5D={lang}"
	chapter_json=requests.get(url)
	chapter_json.raise_for_status
	chapters=(chapter_json.json())["volumes"]["none"]["chapters"]
	chapter_ids={float(num) : chapter["id"] for num,chapter in chapters.items()}
	return chapter_ids
	

#function to download pages per chapter
def download_pages(chapter_ids):
	for num,chapter_id in sorted(chapter_ids.items()):
		choice=inputYesNo("We are creating a new folder for your are you sure you want to continue (yes/no): ").lower()
		if choice == "no":
			print("Quiting program........")
			sys.exit()
		os.makedirs(f"comics/Nan Hao and Shang Feng/ Chapter {num}",exist_ok=True)		
		request=requests.get(f"https://api.mangadex.org/at-home/server/{chapter_id}?forcePort443=false")
		request.raise_for_status
		page_data=request.json()
		base_url=page_data["baseUrl"]
		hash=page_data["chapter"]["hash"]
		pages=page_data["chapter"]["data"]
		n=1
		for page in pages:
			url=base_url + "/data/" + hash + "/"+ page
			print(f"Downloading Chapter {num} page {n}..........")
			image=requests.get(url)
			image.raise_for_status				
			with open(f"comics/Nan Hao and Shang Feng/ Chapter {num}/page {n}.jpg","wb") as file:
				for chunk in image.iter_content(100000):
					file.write(chunk)
			print(f"Chapter {num} page {n} download successful")
			n+=1
		print(f"Chapter {num} completely downloaded")	
	
	
def main():
	print("Mangadex scraper")
	manga=input("What manga are you looking to get: ").capitalize().strip()
	manga_id=search_for_manga(manga)
		
	
	os.chdir("/storage/emulated/0")
main()
	
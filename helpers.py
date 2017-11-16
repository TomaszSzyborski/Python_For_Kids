# for downloading images
import requests
from PIL import Image
import os

def set_background_image_from_image_url(window,image_url="https://upload.wikimedia.org/wikipedia/commons/e/e8/Rasen.jpg"):
	"""
	Helper function to set up background image for turtle

	keyword arguments:
		window - takes turtle.Screen() instance
		image_url - takes url of an image, defaults to grass

	"""
	file_name_gif = "background.gif"
	file_name_jpg = "background.jpg"

	#check if the file has already been downloaded and converted
	try:
		with open(file_name_gif, "rb") as handler:
			background = handler.read()
	except Exception as e:
		print(e)
		print("Downloading image...")

		# downloading the file from internet
		img_data = requests.get(image_url).content
		with open(file_name_jpg, "wb") as handler:
			handler.write(img_data)
		
		# PIL manipulation on image
		# converting from jpg to gif
		img = Image.open(file_name_jpg)
		img.save("background.gif","gif")
		
		# cleanup after download
		os.remove(file_name_jpg)
	
	window.bgpic("background.gif")

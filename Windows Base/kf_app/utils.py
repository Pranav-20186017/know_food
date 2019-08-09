import boto3
import os
from PIL import Image
import math
def classify(filename):
	Classes = ['Banana', 'Bell Pepper', 'Cabbage', 'Carrot', 'Cauliflower', 'Cucumber', 'Green Bean', 'Okra', 'Onion', 'Pea', 'Pepper', 'Potato', 'Pumpkin', 'Radish', 'Squash', 'Sweet Potato', 'Tomato', 'Yam']
	imageFile = 'static\\media\\' + filename
	statinfo = os.stat(imageFile)
	print('****************File Data******************')
	print(statinfo.st_size)
	print(type(statinfo.st_size))
	filesize = statinfo.st_size / (1024 ** 2)
	if filesize > 5.0:
		reduced_image = Image.open(imageFile)
		reduced_image.save(imageFile, quality= (int(500 // filesize)), optimized=True)
	client=boto3.client('rekognition')
	found = False
	veggie_label = ''
	with open(imageFile, 'rb') as image:
	        response = client.detect_labels(Image={'Bytes': image.read()})
	for label in response['Labels']:
		if label['Name'] in Classes:
			return label['Name'], str(round(label['Confidence'],2))
	return 'None', '0'
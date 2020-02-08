#created by Chandra Da Silva
from selenium import webdriver
import time,datetime,string
from selenium.webdriver.common.keys import Keys

from io import BytesIO
import win32clipboard
from PIL import Image

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def copy_file(filepath):
	#filepath = 'capture\\image.png'
	image = Image.open(filepath)
	output = BytesIO()
	image.convert("RGB").save(output, "BMP")
	data = output.getvalue()[14:]
	output.close()
	send_to_clipboard(win32clipboard.CF_DIB, data)

driver=webdriver.Chrome("chromedriver.exe")
driver.get('https://web.whatsapp.com')
input('Enter anything after scanning QR code')

file_name = "attach\\caption.txt"
pesan = []


def kirim(pesan):
	kontak_name = "....Your Whatsapp Contact Name...."
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(kontak_name))
	user.click()
	if len(pesan)>0: # kalo pesan kosong ya ga kirim
		copy_file('capture\\capture.png')
		msg_box = driver.find_element_by_class_name('_3u328')
		msg_box.send_keys("{}".format(Keys.CONTROL + "v"))
		time.sleep(3)
		msg_box = driver.find_element_by_class_name('_3FeAD')
		for i in range(0,len(pesan)): #looping sesuai jumlah pesan
			if i < len(pesan)-1:
				print(pesan[i] + " shift enter")
				msg_box.send_keys("{}".format(pesan[i]) + Keys.SHIFT + Keys.ENTER)
			else:
				print(pesan[i] + " Send")
				msg_box.send_keys("{}".format(pesan[i]))
				msg_box.send_keys("{}".format(Keys.ENTER)) #kirim chat dengan gambar
				# driver.find_element_by_class_name('_2lkdt').click() #kirim chat

def read_file(file_name):
	with open(file_name) as file_in:
		lines = (line.rstrip() for line in file_in) 
		content = list(line for line in lines if line) # Non-blank lines in a list
	return content


while True:
	a=time.localtime()
	hr=a.tm_hour
	mn=a.tm_min
	sc=a.tm_sec
	waktu_kirim_real_time=str(mn)+str(sc)
	check_genap=(int(hr)%2)
	waktu_kirim="5"+"0" #tiap menit
	# waktu_kirim="0"
	# if check_genap == 0 and waktu_kirim_real_time == waktu_kirim:
	if check_genap == 0 and waktu_kirim_real_time == waktu_kirim:
		time.sleep(2)
		content=read_file(file_name)
		print(content)
		if len(content) > 0:
			for j in range(0,len(content)):
				pesan.append(content[j])
			kirim(pesan)
			pesan = []


	


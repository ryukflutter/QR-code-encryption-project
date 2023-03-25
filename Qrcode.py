#import pyqrcode
import qrcode
import re


while True:
	mobNum = input("Enter Your Number (+91): ")
#	print(len(mobNum))
	email = input("Enter your Email: ")
	patternm= r"[6-9]+[0-9]"
	patterne = r"[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
	if len(mobNum)==10:
		if re.match(patternm, mobNum):
			print("next data to be encrypted")
		else:
			print("Not a Valid Number!")
			continue
	else:
		print("Wrong number! ")
		continue
	if re.match(patterne,email):
		print("Your data will be encrypted.")
		img=qrcode.make(f"""Private Data:-> 
Phone number: {mobNum}
email: {email}""")
		break
	else:
		print("Wrong Email!")
		continue

for i in range(1):
	img.save(f"MyQr{i}.png")
	print("Encrypted Qr image saved successfully!")
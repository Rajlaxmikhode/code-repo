import qrcode

data=input("Enter the url: ").strip()
filename=input("Enter the file name: ").strip()

qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image=qr.make_image(fill_color="Black",back_color="white")
image.save(filename)
print(f"QR code saved as {filename}")

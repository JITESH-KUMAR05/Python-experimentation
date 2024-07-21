from PIL import Image , ImageFilter

filename = 'image-processing/glory.jpg'

print("original image")
img = Image.open(filename)
img.show()
print(img.size)
print(img.format)
print(img.mode)

print("cropped image")
croped_img = img.crop((10, 150, 600, 600))
print(croped_img.size)
croped_img.show()
croped_img.save('image-processing/croped_glory.png','png')

print("resized image")
resized_img = img.resize((300, 300))
print(resized_img.size)
resized_img.show()
resized_img.save('image-processing/resized_glory.png','png')

print("rotated image")
rotated_img = img.rotate(10)
print(rotated_img.size)
rotated_img.show()
rotated_img.save('image-processing/rotated_glory.png','png')

print("fliped image")
flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
flipped_img.show()
flipped_img.save('image-processing/flipped_glory.png','png')

print("transversed image")
transversed_img = img.transpose(Image.TRANSVERSE)
transversed_img.show()
transversed_img.save('image-processing/transversed_glory.png','png')

print("converted image")
cmyk_img = img.convert("CMYK")
cmyk_img.show()
rgb_img = cmyk_img.convert("RGB")
rgb_img.save('image-processing/cmyk_glory.png','png')

print("GRAYSCALE image")
gray_img = img.convert("L")
gray_img.show()
gray_img.save('image-processing/gray_glory.png','png')

print("BLACK AND WHITE image")
bw_img = img.convert("1")
bw_img.show()
bw_img.save('image-processing/bw_glory.png','png')

print("bands")
print(img.getbands(),img.getextrema(),img.getpixel((0, 0)))

print("blurred image")
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.show()
blurred_img.save('image-processing/blurred_glory.png','png')
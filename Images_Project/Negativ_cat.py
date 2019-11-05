from  PIL import Image
img = Image.open("Cute-Cat.jpg")
img2=Image.open("Github.png")
img = img.convert('L')
img2 = img.convert('L')
mat = img.load()
w,h=img2.size
print(h,w)
for x in range(w):
    for y in range(h):
        mat[x,y]=255-mat[x,y]
img.show()
img2.show()
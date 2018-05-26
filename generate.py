from PIL import Image, ImageDraw, ImageFont

def find_font_size(max_height):
    for size in range(10,1000):
        fnt = ImageFont.truetype('fonts/FE-FONT.TTF', size)
        width,height=fnt.getsize("X")
        if height > max_height:
            return size-1
    return -1

def draw_text(img,offset,size, text):
    fnt = ImageFont.truetype('fonts/FE-FONT.TTF', font_size)
    d = ImageDraw.Draw(img)
    d.text(offset, text,font=fnt, fill=(0,0,0))
    return fnt.getsize(text)

def draw_image(img, offset,size, image_filename, angle):
    d_img = Image.open(image_filename)
    rotated_img = d_img.rotate(angle)
    rotated_img.thumbnail(size, Image.ANTIALIAS)
    #print (rotated_img.mode) # RGBA
    if (rotated_img.mode == "RGBA"):
        img.paste(rotated_img,offset,mask=rotated_img)
    else:
        img.paste(rotated_img,offset)
    return rotated_img.size
    


img = Image.new('RGB', (1918,427), color=(255,255,255))

draw_image(img,(0,0),(1918,427),"plates/german_plate.png",0)

font_size = find_font_size(372-45)

width,height=draw_text(img,(230,45),font_size,"MLX");

decal_size = (int(((302-45) / 2) + 45),int(((372-45) / 2) + 45))

draw_image(img,(230 + width,45),decal_size,"decals/registration_seal/baden.png",0)
draw_image(img,(230 + width,int(((372-45) / 2) + 45)),decal_size,"decals/safety_test_sticker/2013_date_seal.png",45)

draw_text(img, (1100,45),font_size,"ABC")

img.save("test.png")

#draw 




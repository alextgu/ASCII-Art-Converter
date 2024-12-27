from PIL import Image

im = Image.open("image-path")


width, height = im.size

width, height = im.size
aspect_ratio = width / height

max_width = 200

if width > max_width:
    new_width = max_width
    new_height = int(new_width / aspect_ratio) 
else:
    new_width = width
    new_height = height

resized_image = im.resize((new_width, new_height))


print("Your image loaded successfully!")
print("Image size: " + str(new_width) + " X " + str(height))

pixels_matrix = list(im.getdata())
pixels_matrix = [pixels_matrix[i * width:(i + 1) * width] for i in range(height)]

for row in range(len(pixels_matrix)):
    for i in range(len(pixels_matrix)):
        pixels_matrix[row][i]  = round(max(pixels_matrix[row][i][0],pixels_matrix[row][i][1],pixels_matrix[row][i][2]) + 
        min(pixels_matrix[row][i][0],pixels_matrix[row][i][1],pixels_matrix[row][i][2])/2)


"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_map = {
    range(0, 4): '```',
    range(4, 8): '^^^',
    range(8, 12): "'''",
    range(12, 16): ',,,',
    range(16, 20): ':::',
    range(20, 24): ';;;',
    range(24, 28): 'III',
    range(28, 32): 'lll',
    range(32, 36): '!!!',
    range(36, 40): 'iii',
    range(40, 44): '~~~',
    range(44, 48): '+++',
    range(48, 52): '___',
    range(52, 56): '---',
    range(56, 60): '???',
    range(60, 64): ']]]',
    range(64, 68): '[[[',
    range(68, 72): '}}}',
    range(72, 76): '{{{',
    range(76, 80): '111',
    range(80, 84): ')))',
    range(84, 88): ')))',
    range(88, 92): '|||',
    range(92, 96): '\\\\\\',
    range(96, 100): '///',
    range(100, 104): 'ttt',
    range(104, 108): 'fff',
    range(108, 112): 'jjj',
    range(112, 116): 'rrr',
    range(116, 120): 'xxx',
    range(120, 124): 'nnn',
    range(124, 128): 'uuu',
    range(128, 132): 'vvv',
    range(132, 136): 'ccc',
    range(136, 140): 'zzz',
    range(140, 144): 'XXX',
    range(144, 148): 'YYY',
    range(148, 152): 'UUU',
    range(152, 156): 'JJJ',
    range(156, 160): 'CCC',
    range(160, 164): 'LLL',
    range(164, 168): 'QQQ',
    range(168, 172): '000',
    range(172, 176): 'OOO',
    range(176, 180): 'ZZZ',
    range(180, 184): 'mmm',
    range(184, 188): 'www',
    range(188, 192): 'qqq',
    range(192, 196): 'ppp',
    range(196, 200): 'ddd',
    range(200, 204): 'bbb',
    range(204, 208): 'kkk',
    range(208, 212): 'hhh',
    range(212, 216): 'aaa',
    range(216, 220): 'ooo',
    range(220, 224): '***',
    range(224, 228): '###',
    range(228, 232): 'MMM',
    range(232, 236): 'WWW',
    range(236, 240): '&&&',
    range(240, 244): '888',
    range(244, 248): '%%%',
    range(248, 999): '$$$'
}

for row in range(len(pixels_matrix)):
    for i in range(len(pixels_matrix)):
        for r in ascii_map.keys():
            if pixels_matrix[row][i] in r:
                pixels_matrix[row][i] = ascii_map[r]
                break

with open("canvas.txt", 'w') as canvas:
    
    for i in range(len(pixels_matrix)):
        row = ""
        for x in range(len(pixels_matrix)):
            row += pixels_matrix[i][x]
        print(row + "\n")
        


        


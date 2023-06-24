import io
import os
from datetime import datetime as dt
from PIL import Image
import os

UPLOADED_FILES_PATH = 'app/uploaded_files/'

# Save file to uploads folder
async def save_file_to_uploads(file, filename):
    # with open(f'{UPLOADED_FILES_PATH}{filename}', "wb") as uploaded_file:
    for line in file:
        file_content = await line.read()

        try:
            img = Image.open(io.BytesIO(file_content))

            size = len(img.fp.read())

            if size > 1000000:
                raise print(f'Размер не должен привышать 1мб. Текущий размер {size / 1000000}мб')
                

            size_1 = (1920, 1080)
            size_2 = (1280, 720)
            # size_3 = (680, 480)

            out_1920 = img.resize(size_1, resample=4, box=None)
            out_1280 = img.resize(size_2, resample=2, box=None)

            # print(out_1920.size)

            # Сохранить
            out_1920.save('img1.png', 'JPEG')
            out_1280.save('img2.png', 'JPEG')
            # out_680.save("img3.png", "PNG")
        except:
            print('При сохранении изображения произошла ошибка')

        # uploaded_file.close()


# Format filename
def format_filename(file, name=None):
    # Split filename and extention
    filename, ext = os.path.splitext(file.filename)

    # Rename file
    if name is None:
        filename = filename + dt.now().strftime('%d_%m_%Y')
    else:
        filename = name + dt.now().strftime('%d_%m_%Y')

    return filename + ext

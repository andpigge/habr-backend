import os


UPLOADED_FILES_PATH = 'app/uploaded_files/'

# Save file to uploads folder
async def save_file_to_uploads(file, filename):
    with open(f'{UPLOADED_FILES_PATH}{filename}', "wb") as uploaded_file:
        file_content = await file.read()
        uploaded_file.write(file_content)
        uploaded_file.close()


# Format filename
def format_filename(file, file_id=None, name=None):
    # Split filename and extention
    filename, ext = os.path.splitext(file.filename)

    # Rename file
    if name is None:
        filename = str(file_id)
    else:
        filename = name

    return filename + ext


# Get file size
def get_file_size(filename, path : str = None):
    file_path = f'{UPLOADED_FILES_PATH}{filename}'

    if path:
        file_path = f'{path}{filename}'

    return os.path.getsize(file_path)

#join a folder and filename with pathlib.path

from pathlib import Path

folder_name = Path('data science/')
file_name = Path('computer vision')

join_path = folder_name.joinpath(file_name)
print(join_path)

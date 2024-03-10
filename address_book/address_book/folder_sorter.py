import os
import shutil
import typing
from pathlib import Path
from collections import defaultdict


CATEGORIES = {
    'images': ['.png', '.jpeg', '.svg', '.gif', '.jpg'],
    'python': ['.py', '.pyi'],
    'javascript': ['.js'],
    'video': ['.mov', '.mp4', '.mkv', '.avi'],
    'documents': ['.docx', '.doc', '.txt', '.pdf', '.xls', '.xlsx', '.csv', '.pptx'],
    'audio': ['.mp3', '.ogg', '.wav', '.amr'],
    'archives': ['.gz', '.zip', '.tar', '.rar', '.tgz'],
    'code': ['.java', '.cpp', '.c', '.html', '.css', '.php', '.rb', '.swift', '.go'],
    'executable': ['.exe', '.bat', '.dmg'],
    'presentations': ['.key', '.odp'],
    'fonts': ['.ttf', '.otf', '.woff'],
    'spreadsheets': ['.ods'],
    'data': ['.json', '.xml', '.sql'],
    'backups': ['.bak', '.old'],
    'databases': ['.db', '.sqlite', '.mdb', '.sqlite3'],
    'ebooks': ['.epub', '.mobi'],
    'scripts': ['.ps1', '.bashrc', '.sh', '.zshrc'],
    'configurations': ['.ini', '.cfg', '.conf'],
    'cad': ['.dwg', '.dxf'],
    'torrents': ['.torrent'],
    'logs': ['.log']
}
UNKNOWN_CATEGORY = 'unknown'
CATEGORY_FOLDERS = [*CATEGORIES.keys(), UNKNOWN_CATEGORY]
SUPPORTED_EXTENSIONS = set(sum([ext for ext in CATEGORIES.values()], []))


def _get_category_by_extension(ext: str) -> str:
    for category_name, ext_list in CATEGORIES.items():
        if ext in ext_list:
            return category_name

    return UNKNOWN_CATEGORY


def _move_file(file_path: str, category_folder: str) -> typing.Tuple[str, bool]:
    try:
        shutil.move(file_path, category_folder)
    except shutil.Error:
        return file_path, True

    filename = os.path.basename(file_path)
    new_file_path = os.path.join(category_folder, filename)

    return new_file_path, False


def _check_if_path_is_part_of_category_folder(folder: str, path: str):
    path = Path(path)

    for category in CATEGORY_FOLDERS:
        category_path = Path(os.path.join(folder, category))

        if category_path == path or category_path in path.parents:
            return True

    return False


def _display_analytics(known, unknown, files, folders):
    print()

    for category, filenames in files.items():
        dirnames = folders.get(category, [])
        filenames = list(map(os.path.basename, filenames))
        dirnames = list(map(os.path.basename, dirnames))

        if filenames:
            print(f'Files added to {category:15}', ', '.join(filenames))
        if dirnames:
            print(f'Folders added to {category:15}', ', '.join(dirnames))
        if filenames or dirnames:
            print()

    if known:
        print('Seen file extensions: ', ', '.join(known))

    if unknown:
        print('Unknown file extensions: ', ', '.join(unknown))

    print('All Done')


def sort_folder(target_folder_path: str, display_analytics: bool = False) -> None:
    known = set()
    unknown = set()
    folders = defaultdict(list)
    files = defaultdict(list)

    for dirpath, dirnames, filenames in os.walk(target_folder_path):
        if not dirnames and not filenames:
            os.rmdir(dirpath)

        for filename in filenames:
            _, ext = os.path.splitext(filename)
            filename = os.path.join(dirpath, filename)

            category = _get_category_by_extension(ext)
            category_folder = os.path.join(target_folder_path, category)

            os.makedirs(category_folder, exist_ok=True)

            new_file_path, is_same_file = _move_file(filename, category_folder)

            if is_same_file:
                continue

            store = folders if os.path.isdir(new_file_path) else files
            store[category].append(new_file_path)

            if not ext:
                ext = 'W/o extension'

            if ext not in SUPPORTED_EXTENSIONS:
                unknown.add(ext)
            else:
                known.add(ext)

    for dirpath, dirnames, filenames in os.walk(target_folder_path):
        if dirpath != target_folder_path and not _check_if_path_is_part_of_category_folder(target_folder_path, dirpath):
            shutil.rmtree(dirpath)
            
    if display_analytics:
        _display_analytics(known, unknown, files, folders)
    
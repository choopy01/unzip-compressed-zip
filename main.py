import zipfile
import os
import shutil


def extract_file(file_path, extract_dir):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            extracted_path = zip_ref.extract(file_info, extract_dir)
            extracted_filename = os.path.basename(extracted_path)
            target_path = os.path.join(extract_dir, extracted_filename)

            # Проверяем наличие файла с таким же именем в целевой директории
            while os.path.exists(target_path):
                # Генерируем новое имя для извлеченного файла
                base_name, extension = os.path.splitext(extracted_filename)
                new_filename = f"{base_name}_extracted{extension}"
                target_path = os.path.join(extract_dir, new_filename)

            # Перемещаем или переименовываем извлеченный файл
            shutil.move(extracted_path, target_path)

            # Если извлеченный файл является архивом, повторяем процесс разархивирования
            if zipfile.is_zipfile(target_path):
                extract_file(target_path, extract_dir)


# Пример использования:
zip_file_path = 'C:/Users/mynam/Desktop/акшутвы/347.zip'  # Путь к zip-архиву
extract_dir = 'C:/Users/mynam/Desktop/акшутвы'  # Путь к директории для извлечения файлов

# Разархивировать файл и архивы с таким же именем по очереди
extract_file(zip_file_path, extract_dir)
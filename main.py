import zipfile
import os
import shutil


def extract_file(file_path, extract_dir):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            extracted_path = zip_ref.extract(file_info, extract_dir)
            extracted_filename = os.path.basename(extracted_path)
            target_path = os.path.join(extract_dir, extracted_filename)

           
            while os.path.exists(target_path):
                
                base_name, extension = os.path.splitext(extracted_filename)
                new_filename = f"{base_name}_extracted{extension}"
                target_path = os.path.join(extract_dir, new_filename)

            
            shutil.move(extracted_path, target_path)

            
            if zipfile.is_zipfile(target_path):
                extract_file(target_path, extract_dir)



zip_file_path = 'C:/Users/User/Desktop/anyfile/???.zip'  
extract_dir = 'C:/Users/User/Desktop/anyfile'  


extract_file(zip_file_path, extract_dir)

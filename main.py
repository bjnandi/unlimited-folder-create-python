import os
import zipfile
import random


def generate_random_numbers(start, end):
    return random.randint(start, end)

def create_zip_folders(num_folders, folder_prefix=1, file_content='Hello World'):

    for i in range(1, num_folders + 1):

        random_numbers = generate_random_numbers(1000, 10000)
        folder_prefix = random_numbers
        # folder_name = f'{folder_prefix}_{i}'
        zip_file_name = f'{folder_prefix}.zip'
        
        # Create a ZIP file
        with zipfile.ZipFile(zip_file_name, 'w') as zipf:
            # Add a text file to the ZIP file
            zipf.writestr('file.txt', file_content)
            
        print(f'{zip_file_name} created.')

# Change the number of ZIP folders to create
create_zip_folders(50)

import zipfile
import shutil

start = int(input(
    "Hello! This is a ZIP archiver and extractor.\n"
    "Choose an option:\n"
    "1. Create a ZIP archive\n"
    "2. Extract a ZIP archive\n"
    "Your choice: "
))

if start == 1:
    a = input("What should the archive be named (without .zip)?: ")
    a2 = int(input("Where should the archive be saved?\n1. Specify a custom path\n2. Save it here\nYour choice: "))
    if a2 == 1:
        paths = input("Enter the full path to save the archive (without filename): ")
        full_path = paths.rstrip("/") + "/" + a + ".zip"
    else:
        full_path = a + ".zip"
    
    with zipfile.ZipFile(full_path, "w") as archive:
        archive.writestr("hello.txt", "Hi! This is some text inside your archive.")

    print(f"Archive created successfully at: {full_path}")

elif start == 2:
    a = input("Enter the full path to your ZIP archive:\n")
    a2 = input("Enter the folder path where you want to extract the archive:\n")
    
    try:
        shutil.unpack_archive(filename=a, extract_dir=a2, format="zip")
        print("Archive extracted successfully!")
    except shutil.ReadError:
        print("Error: The file is not a valid ZIP archive.")
    except FileNotFoundError:
        print("Error: The archive file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

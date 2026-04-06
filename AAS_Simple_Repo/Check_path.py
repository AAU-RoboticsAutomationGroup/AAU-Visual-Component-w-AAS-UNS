import os

file_uri = "C:\\Users\\Thor9\\OneDrive - Aalborg Universitet\\Dokumenter\\Visual Components\\4.10\\My Models\\AAU-Visual-Components\\Components\\Phone Components\\Bottom_Cover.vcmx"  # Example file URI, replace with actual URI
if file_uri.startswith("file:///"):
    file_path = file_uri[8:]
else:
    file_path = file_uri
file_path = os.path.abspath(file_path)

if os.path.exists(file_path):
    print("Valid path:", file_path)
else:
    print("Invalid path or not found:", file_path)

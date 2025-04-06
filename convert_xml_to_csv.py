import xmltodict

xml_file = "dataset/breast_cancer.xml"

with open(xml_file, "r", encoding="utf-8") as file:
    xml_data = file.read()

# Print first few lines to check if the file is valid
print("XML Content Preview:")
print(xml_data[:500])  # Print the first 500 characters

# Proceed with parsing only if content is valid
if xml_data.strip():
    data_dict = xmltodict.parse(xml_data)
    print("XML Parsed Successfully ✅")
else:
    print("Error: XML file is empty ❌")

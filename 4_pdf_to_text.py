"""
Ce script permet d'extraire le contenu textuel d'un fichier PDF
Il est possible de l'utiliser en ligne de commande

python 4_pdf_to_text.py path_to_file.pdf
"""
from pypdf import PdfReader
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python 4_pdf_to_text.py path_to_file.pdf")

filename = sys.argv[1]

try:

    reader = PdfReader(filename)
    number_of_pages = len(reader.pages)

    text_content = []
    for page in reader.pages:
        text = page.extract_text()
        text_content.append(text)

    resultfile = filename + '.txt'
    with open(resultfile, 'w', encoding='utf-8') as file:
        file.writelines(text_content)

    print('Extraction terminée !')
    print(f'Résultat dans le fichier "{resultfile}"')

except FileNotFoundError:
    sys.exit("Error: fichier introuvable !")
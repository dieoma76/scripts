# Kleines Python Script um eine CSV einzulesen, Felder umzubenennen, neu zusammenzusetzen und
# als JSON File neu zu schreiben
# copyright: Markus Smieja
# 07.02.2023, v0.2

import csv 
import json 

csvFilePath = r'VMware Kochbuch Library.csv'
jsonFilePath = r'VMware Kochbuch Library.json'

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
            row['@context'] = 'https://schema.org'
            row['@type'] = 'Recipe'
            del row['E-Mail']
            row['author'] = row['Vorname'] + " " + row['Name']
            del row['Vorname']
            del row['Name']
            row['cookTime'] = row.pop('Zubereitungsdauer')
            row['description'] = row.pop('Geschichte des Rezepts')
            row['image'] = row.pop('Rezeptbilderpfad')
            row['name'] = row.pop('Name des Rezepts')
            del row ['Kategorie']
            row['recipeIngredient'] = row['Zutatenliste'].split(',')
            del row['Zutatenliste']
            del row['Autorbilderpfad']
            row['recipeInstructions'] = row.pop('Zubereitung')

    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

csv_to_json(csvFilePath, jsonFilePath)
# Kleines Python Script um eine CSV einzulesen, Felder umzubenennen, neu zusammenzusetzen und
# als JSON File neu zu schreiben
# copyright: Markus Smieja
# 02.02.2023, v0.1

import csv 
import json 

csvFilePath = r'Cookbook.csv'
jsonFilePath = r'Cookbook.json'

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
            del row['Bild des Autors']
            row['@context'] = 'https://schema.org'
            row['@type'] = 'Recipe'
            del row['E-Mail']
            del row['Copyright Bestätigung']
            row['author'] = row['Vorname'] + " " + row['Name']
            del row['Vorname']
            del row['Name']
            row['description fuer Jochen'] = row.pop('Geschichte des Rezepts')
            row['image'] = row.pop('Bilder des Gerichts')
            row['name'] = row.pop('Name des Rezepts')
            row['recipeIngredient'] = row['Zutatenliste'].split(',')
            del row['Zutatenliste']
            row['recipeInstructions'] = row.pop('Zubereitung')

    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

csv_to_json(csvFilePath, jsonFilePath)
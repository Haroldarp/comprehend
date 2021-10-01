import boto3
import csv
import json

with open('credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

client = boto3.client('comprehend', 
        region_name='us-east-1', 
        aws_access_key_id=access_key_id, 
        aws_secret_access_key=secret_access_key)

with open('Caperucita roja.txt', errors="ignore") as f:
    text = f.read()

response = client.detect_dominant_language(Text=text)
with open('dominant_language.json', 'w') as f:
            json.dump(response, f, indent=4 )

response = client.detect_entities(Text=text, LanguageCode = 'en')
with open('entities.json', 'w') as f:
            json.dump(response, f, indent=4 )

response = client.detect_key_phrases(Text=text, LanguageCode = 'en')
with open('key_phrases.json', 'w') as f:
            json.dump(response, f, indent=4 )

response = client.detect_sentiment(Text=text, LanguageCode = 'en')
with open('sentiment.json', 'w') as f:
            json.dump(response, f, indent=4 )   
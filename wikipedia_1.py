"""
    name: Yonatan getachew 
    Author: Yonatan Getachew 
    Created: 3/24/2024
""" 

# pip install wikipedia
import wikipedia

search_terms = input("Search Wikipedia: ")

summary = wikipedia.summary(search_terms, sentences=3)

print(summary)
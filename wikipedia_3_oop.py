# pip install wikipedia
import wikipedia

class WikipediaApp:
    def __init__(self):
        pass
    
    def get_wikipedia(self):
        """Search Wikipedia"""
        try:
            # Type in your search term
            result = input("Search Wikipedia: ")
            # Return a summary result of 3 sentences
            self._summary = wikipedia.summary(result, sentences=3)
        except:
            # Use raise for troubleshooting exceptions
            # raise 
            # If there is an exception, allow the user to try again
            print("Try a different search term.")
    
    def display_wikipedia(self):
        """Display wikipedia search results"""
        print(self._summary)

# Create a program object
wikipedia_app = WikipediaApp()

while True:
    wikipedia_app.get_wikipedia()
    wikipedia_app.display_wikipedia()

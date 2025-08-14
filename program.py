from pypdf import PdfReader,PdfWriter
import os 

# Function to add tags to different pdfs within the directory
def tagging_function():
    #iterating over the function as many times as the user would like
    while True: 
        # listing all pdfs within the directory
        for each in os.listdir():
            if each.endswith(".pdf"):
                print(each)

        targetpdf = input("Please type in the name of the pdf that you would like to add tags to: ")
        reader = PdfReader(targetpdf)
        writer = PdfWriter()
        
        #creating a new page without old metadata
        for page in reader.pages:
            writer.add_page(page)

        while True:
            print("The available tag types are age, difficulty, and category.")
            
            decision1 = input("Which tag type would you like to add to the file? (age, difficulty, category)   ")
            tag_type = "/"+decision1
            tag_contents = input("What would you like the tag to be?   ")

            # add the above metadata to the target pdf
            writer.add_metadata(
                {
                    tag_type:tag_contents,
                }
            
            # add those changes to the file
            )
            with open(targetpdf,"wb") as f:
                writer.write(f)
            
            # allows the user to add multiple tags to the same file
            decision3 = input("Would you like to add more tags to the same file? (y/n)")
            if decision3 == "y":
                continue
            if decision3 == "n":
                break
        
        # allows the user to select a different file to add tags to
        decision2 = input("Would you like to add tags to another file? (y/n)")
        if decision2 == "y":
            continue
        if decision2 == "n":
            break

search_query = []

query = input("Please enter tags you would like to search for. Please separate search terms with a comma: ")

# add some parsing that breaks up the string based on commas, adds that to the search query, and then uses that to search through metadata values

search_query.append(query)

for each in os.listdir():
    if each.endswith(".pdf"):
        pdf = PdfReader(each)
        if search_query in pdf.metadata.values():
            print(each)
        else:
            pass


'''
print("Welcome to the Piano Studio Program.")
print()
beginning = input("Would you like to tag, search, or exit?")
if beginning == "tag":
    tagging_function()
if beginning == "exit":
    exit()
'''
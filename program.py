from pypdf import PdfReader,PdfWriter
import os 

def tagging_function():
    while True: 
        for each in os.listdir():
            if each.endswith(".pdf"):
                print(each)

        targetpdf = input("Please type in the name of the pdf that you would like to add tags to: ")
        reader = PdfReader(targetpdf)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        print("The available tag types are age, difficulty, and category.")
        
        decision1 = input("Which tag type would you like to add to the file? (age, difficulty, category)")
        tag_type = "/"+decision1
        tag_contents = input("What would you like the tag to be?")


        writer.add_metadata(
            {
                tag_type:tag_contents,
            }
        )

        with open("test.pdf","wb") as f:
            writer.write(f)
        
        decision2 = input("Would you like to add tags to another file? (y/n)")
        if decision2 == "y":
            continue
        if decision2 == "n":
            break

print("Welcome to the Piano Studio Program.")
print()
beginning = input("Would you like to tag or search?")
if beginning == "tag":
    tagging_function()

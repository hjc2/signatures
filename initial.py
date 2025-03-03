

from PyPDF2 import PdfReader, PdfWriter

# Hardcoded file paths
INPUT_PDF = "test20.pdf"  # Change this to your input file name
OUTPUT_PDF = "reordered_for_printing.pdf"  # Change this to your desired output file name
SHEETS_PER_SIGNATURE = 6 # 5 sheets = 20 pages when folded

"""
Reorder pages in a PDF for printing as a single signature.
All file paths and settings are hardcoded.
"""
print(f"Reading {INPUT_PDF}...")

reader = PdfReader(INPUT_PDF)
writer = PdfWriter()
fakeWriter = PdfWriter()

total_pages = len(reader.pages)
pages_per_signature = SHEETS_PER_SIGNATURE * 4  # 4 pages per sheet (front and back, folded)

print(f"Input PDF has {total_pages} pages")
print(f"a total of {pages_per_signature} count")

# Fix the page count to exactly our signature size

first_page = reader.pages[0]
width = first_page.mediabox.width
height = first_page.mediabox.height

# Create a list with available pages
all_pages = []

# Add actual pages, limited to our signature size
for i in range(total_pages):
    all_pages.append(reader.pages[i])
print(f"a total of {len(all_pages)} all pages")

needed_pages = pages_per_signature - len(all_pages)

print(f"a total of {needed_pages} needed pages")

for _ in range(needed_pages):
    all_pages.append(fakeWriter.add_blank_page(width, height))
print(f"a total of {len(all_pages)} all after stuff")


print(f"Reordering pages")

# Reorder the pages in the correct imposition order
reordered = []
for sheet in range(SHEETS_PER_SIGNATURE):
    # Calculate page positions for this sheet
    front_left = needed_pages - 1 - (sheet * 2)  # Last page, working inward
    front_right = sheet * 2                      # First page, working inward
    back_left = (sheet * 2) + 1                  # Second page, working inward
    back_right = needed_pages - 2 - (sheet * 2)  # Second-to-last page, working inward
    # Front of sheet (when printing duplex)
    reordered.append(all_pages[front_left])
    reordered.append(all_pages[front_right])
    
    # Back of sheet (when printing duplex)
    reordered.append(all_pages[back_left])
    reordered.append(all_pages[back_right])

# Add the reordered pages to the output PDF
for page in reordered:
    writer.add_page(page)

# Save the reordered PDF
print(f"Writing PDF to {OUTPUT_PDF}...")
with open(OUTPUT_PDF, "wb") as output_file:
    writer.write(output_file)

print(f"complete")



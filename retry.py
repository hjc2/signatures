
from PyPDF2 import PdfReader, PdfWriter

# Hardcoded file paths
INPUT_PDF = "test4.pdf"  # Change this to your input file name
OUTPUT_PDF = "reordered_for_printing.pdf"  # Change this to your desired output file name
SHEETS_PER_SIGNATURE = 2 # 5 sheets = 20 pages when folded

reader = PdfReader(INPUT_PDF)
writer = PdfWriter()
fakeWriter = PdfWriter()

otherWriter = PdfWriter()

total_pages = len(reader.pages)
pages_per_signature = SHEETS_PER_SIGNATURE * 4  # 4 pages per sheet (front and back, folded)


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

needed_pages = pages_per_signature - total_pages

print(f" how many? {needed_pages}")
for _ in range(needed_pages):
    all_pages.append(fakeWriter.add_blank_page(width, height))

print(all_pages)
reordered = []
for sheet in range(SHEETS_PER_SIGNATURE):
    # Calculate page positions for this sheet
    front_left = needed_pages - 1 - (sheet * 2)  # Last page, working inward
    front_right = sheet * 2                      # First page, working inward
    back_left = (sheet * 2) + 1                  # Second page, working inward
    back_right = needed_pages - 2 - (sheet * 2)  # Second-to-last page, working inward
    # Front of sheet (when printing duplex)

    writer.add_page(all_pages[front_left])
    writer.add_page(all_pages[front_right])
    
    # Back of sheet (when printing duplex)from PyPDF2 import PdfReader, PdfWriter

# Hardcoded file paths
INPUT_PDF = "test4.pdf"  # Change this to your input file name
OUTPUT_PDF = "reordered_for_printing.pdf"  # Change this to your desired output file name
SHEETS_PER_SIGNATURE = 2  # 2 sheets = 8 pages when folded

reader = PdfReader(INPUT_PDF)
writer = PdfWriter()

total_pages = len(reader.pages)
pages_per_signature = SHEETS_PER_SIGNATURE * 4  # 4 pages per sheet (front and back, folded)

# Get dimensions from first page
first_page = reader.pages[0]
width = first_page.mediabox.width
height = first_page.mediabox.height

# Create a list with available pages
all_pages = []

# Add actual pages
for i in range(total_pages):
    all_pages.append(reader.pages[i])

# Calculate how many blank pages needed
# If we need exactly 8 pages, make sure we have 8
remainder = total_pages % pages_per_signature
if remainder != 0:
    needed_blank_pages = pages_per_signature - remainder
    print(f"Adding {needed_blank_pages} blank pages")
    for _ in range(needed_blank_pages):
        blank_page = writer.add_blank_page(width, height)
        all_pages.append(blank_page)

# Now we have total_padded_pages = len(all_pages)
total_padded_pages = len(all_pages)
print(f"Total pages after padding: {total_padded_pages}")

# Number of complete signatures
num_signatures = total_padded_pages // pages_per_signature

# Process each signature
for sig in range(num_signatures):
    start_idx = sig * pages_per_signature
    
    # Process each sheet in the signature
    for sheet in range(SHEETS_PER_SIGNATURE):
        # Calculate indexes for this sheet in the current signature
        # For a signature: pages are ordered like: last, first, second, second-to-last, etc.
        front_left_idx = start_idx + pages_per_signature - 1 - sheet
        front_right_idx = start_idx + sheet
        back_left_idx = start_idx + sheet + 1
        back_right_idx = start_idx + pages_per_signature - 2 - sheet
        
        # Add pages to the writer in correct order
        # Front of sheet
        writer.add_page(all_pages[front_right_idx])
        writer.add_page(all_pages[front_left_idx])
        
        # Back of sheet (when printing duplex)
        writer.add_page(all_pages[back_left_idx])
        writer.add_page(all_pages[back_right_idx])

# Save the reordered PDF
print(f"Writing PDF to {OUTPUT_PDF}...")
with open(OUTPUT_PDF, "wb") as output_file:
    writer.write(output_file)

print("Complete")
    writer.add_page(all_pages[back_left])
    writer.add_page(all_pages[back_right])


# Save the reordered PDF
print(f"Writing PDF to {OUTPUT_PDF}...")
with open(OUTPUT_PDF, "wb") as output_file:
    writer.write(output_file)

print(f"complete")



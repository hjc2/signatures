import fitz  # PyMuPDF

# Load the original PDF
input_path = "the_sample.pdf"
output_path = "output_single_page.pdf"
doc = fitz.open(input_path)

# Create a new PDF to hold the single page layout
new_doc = fitz.open()

# Create a new horizontal letter-sized page (11 x 8.5 inches)
letter_width, letter_height = fitz.paper_size("letter")
new_width = letter_height  # Switch width and height for landscape
new_height = letter_width

# Add a new blank page (horizontal landscape)
new_page = new_doc.new_page(width=new_width, height=new_height)

# Dimensions for each page in the 2x4 grid (2 columns, 4 rows)
cols = 4
rows = 2
spacing = 0  # space between pages in points

# Dimensions of each page in the layout
page_width = new_width / cols
page_height = new_height / rows

custom_order = [4,3,2,1,5,6,7,0]

# Loop through each page and place it in the grid
#for i in range(8):
for i, page_index in enumerate(custom_order):
    page = doc.load_page(page_index)

    # Rotate the page if it's in portrait mode (rotate 90 degrees)
   # if page.rect.width < page.rect.height:
    #    page.set_rotation(90)
    if i < 4:
        page.set_rotation(180)
    # Render the page to a pixmap (image)
    pix = page.get_pixmap()

    # Calculate position to place this page in the grid
    row = i // cols
    col = i % cols
    x_offset = col * (page_width + spacing)
    y_offset = row * (page_height + spacing)

    # Create a rectangle where the page will be placed
    rect = fitz.Rect(x_offset, y_offset, x_offset + page_width, y_offset + page_height)

    # Place the pixmap onto the new page
    new_page.insert_image(rect, pixmap=pix)

# Save the result to a new PDF
new_doc.save(output_path)
new_doc.close()
doc.close()

print("PDF has been processed and saved as:", output_path)

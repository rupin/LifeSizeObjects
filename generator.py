import os
from PIL import Image

# Set the input folder path
input_folder_path = "letters"

# Set the output folder path
output_folder_path = "output"

# Set the paper size in pixels (300 dpi for 210mm x 297mm)
paper_width = 2480
paper_height = 3508

# Iterate over each image in the input folder
for filename in os.listdir(input_folder_path):
    # Check if the file is a PNG image
    if filename.endswith(".jpg"):
        # Open the image
        image_path = os.path.join(input_folder_path, filename)
        image = Image.open(image_path)

        # Get the image dimensions
        image_width, image_height = image.size

        # Calculate the number of pages required to print the image
        num_pages_wide = (image_width + paper_width - 1) // paper_width
        num_pages_high = (image_height + paper_height - 1) // paper_height
        num_pages = num_pages_wide * num_pages_high

        # Iterate over each page
        for page_index in range(num_pages):
            # Calculate the coordinates of the top-left corner of the page
            page_x = (page_index % num_pages_wide) * paper_width
            page_y = (page_index // num_pages_wide) * paper_height

            # Calculate the coordinates of the bottom-right corner of the page
            page_right = min(page_x + paper_width, image_width)
            page_bottom = min(page_y + paper_height, image_height)

            # Calculate the size of the page
            page_width = page_right - page_x
            page_height = page_bottom - page_y

            # Create a new image for the page
            page_image = Image.new("RGB", (paper_width, paper_height), color="white")

            # Copy the relevant portion of the original image to the page
            page_image.paste(image.crop((page_x, page_y, page_right, page_bottom)))

            # Save the page as a new PNG image
            output_filename = f"{filename}_{page_index + 1}.png"
            output_path = os.path.join(output_folder_path, output_filename)
            page_image.save(output_path, dpi=(300,300))

        # Close the original image
        image.close()

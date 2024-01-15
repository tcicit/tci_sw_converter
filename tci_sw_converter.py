from PIL import Image, ImageEnhance
import argparse
import os
import glob

def convert_to_bw_with_contrast_and_brightness(input_image_path, contrast_factor, brightness_factor):
    # Open the original image
    original_image = Image.open(input_image_path)
    
    # Convert the image to black and white
    bw_image = original_image.convert('L')

    # Adjust the contrast
    enhancer_contrast = ImageEnhance.Contrast(bw_image)
    bw_with_contrast_image = enhancer_contrast.enhance(contrast_factor)

    # Adjust the brightness
    enhancer_brightness = ImageEnhance.Brightness(bw_with_contrast_image)
    final_image = enhancer_brightness.enhance(brightness_factor)

    return final_image

def generate_output_filename(input_path, output_directory, count=0):
    # Generate an output filename based on the input path and count
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_image = os.path.join(output_directory, f"{base_name}_converted_{count}.jpg")

    # Check and increment the count if the file already exists
    while os.path.exists(output_image):
        count += 1
        output_image = os.path.join(output_directory, f"{base_name}_converted_{count}.jpg")

    return output_image

def convert_single_file(input_image, output_image, contrast_factor, brightness_factor):
    # If no output path is specified, create one based on the input path
    if output_image is None:
        output_directory = os.path.dirname(input_image)
        output_image = generate_output_filename(input_image, output_directory)
    else:
        output_directory = os.path.dirname(output_image)
        output_image = generate_output_filename(output_image, output_directory)

    try:
        # Convert the single image
        final_image = convert_to_bw_with_contrast_and_brightness(input_image, contrast_factor, brightness_factor)
        final_image.save(output_image)
        print(f"Successfully converted and saved: {output_image}")
    except Exception as e:
        print(f"Error converting '{input_image}': {e}")

def convert_all_in_directory(input_directory, output_directory, contrast_factor, brightness_factor):
    # If no output directory is specified, create one in the input directory
    if output_directory is None:
        output_directory = os.path.join(input_directory, "converted_images")
        os.makedirs(output_directory, exist_ok=True)

    # List all files in the input directory
    input_files = glob.glob(os.path.join(input_directory, "*.jpg"))
    
    for input_file in input_files:
        # Generate an output path for each image
        output_image = generate_output_filename(input_file, output_directory)
        
        try:
            # Convert each image in the directory
            final_image = convert_to_bw_with_contrast_and_brightness(input_file, contrast_factor, brightness_factor)
            final_image.save(output_image)
            print(f"Successfully converted and saved: {output_image}")
        except Exception as e:
            print(f"Error converting '{input_file}': {e}")

if __name__ == "__main__":
    # Set up the argument parser for command line arguments
    parser = argparse.ArgumentParser(description='Convert an image to black and white with adjustable contrast and brightness.')
    parser.add_argument('-i', '--input', help='Path to the input image file (JPG)')
    parser.add_argument('-o', '--output', help='Path to the output image file (JPG)')
    parser.add_argument('-c', '--contrast', type=float, default=1.0, help='Contrast factor (default: 1.0)')
    parser.add_argument('-b', '--brightness', type=float, default=1.0, help='Brightness factor (default: 1.0)')
    parser.add_argument('-d', '--directory', default=None, help='Path to the directory containing images for batch processing')
    args = parser.parse_args()

    if args.directory:
        try:
            # Perform batch processing for a directory
            convert_all_in_directory(args.directory, args.output, args.contrast, args.brightness)
        except IsADirectoryError:
            print(f"Error: The directory '{args.input}' was not found.")
    else:
        try:
            # Perform single image conversion
            convert_single_file(args.input, args.output, args.contrast, args.brightness)
            print("Successfully converted and saved.")
        except FileNotFoundError:
            print(f"Error: The file '{args.input}' was not found.")
        except Exception as e:
            print(f"Error: {e}")

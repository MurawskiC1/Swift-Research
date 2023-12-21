from PIL import Image, ImageDraw

def add_transparent_rectangle(input_image_path, output_image_path, rectangle_position, rectangle_size):
    # Open the image
    img = Image.open(input_image_path).convert("RGBA")
    
    #draw an image of rectangle
    draw = ImageDraw.Draw(img)
    draw.rectangle([rectangle_position[0], rectangle_position[1],
                    rectangle_position[0] + rectangle_size[0], rectangle_position[1] + rectangle_size[1]],
                   outline="red")

    # Save the result
    img.save(output_image_path)

# Example usage:
input_image_path = "BurstPhotos/GRB071018_294645.png"
output_image_path = "Boxes/GRB2.png"
rectangle_position = (245, 96)  # X and Y coordinates of the top-left corner of the rectangle
rectangle_size = (28.5, 236.96)  # Width and height of the rectangle

add_transparent_rectangle(input_image_path, output_image_path, rectangle_position, rectangle_size)

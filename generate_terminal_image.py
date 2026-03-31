import sys
from PIL import Image, ImageDraw, ImageFont

def generate_terminal_image(input_file, output_image):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Try to load a monospaced font, fallback to default
    try:
        font = ImageFont.truetype("consola.ttf", 16)
    except IOError:
        font = ImageFont.load_default()
        
    # Calculate image size
    # Create dummy image to get text size
    dummy_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    
    lines = text.split('\n')
    max_width = 0
    total_height = 0
    
    for line in lines:
        left, top, right, bottom = draw.textbbox((0, 0), line, font=font)
        width = right - left
        height = bottom - top
        max_width = max(max_width, width)
        total_height += (height + 4) # Add line spacing
        
    # Add padding
    padding = 20
    img_width = max(800, max_width + padding * 2)
    img_height = max(100, total_height + padding * 2)
    
    # Create image with dark background
    img = Image.new('RGB', (img_width, img_height), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)
    
    # Draw terminal header bar (optional, makes it look nicer)
    draw.rectangle([0, 0, img_width, 30], fill=(50, 50, 50))
    # Draw window buttons
    draw.ellipse([10, 10, 20, 20], fill=(255, 95, 86)) # Red
    draw.ellipse([25, 10, 35, 20], fill=(255, 189, 46)) # Yellow
    draw.ellipse([40, 10, 50, 20], fill=(39, 201, 63)) # Green
    
    # Draw text
    y = padding + 20
    for line in lines:
        draw.text((padding, y), line, font=font, fill=(230, 230, 230))
        # Get line height
        _, top, _, bottom = draw.textbbox((0, 0), line, font=font)
        y += (bottom - top + 4)
        
    # Save image
    img.save(output_image)
    print(f"Saved terminal image to {output_image}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_terminal_image.py <input.txt> <output.png>")
        sys.exit(1)
    generate_terminal_image(sys.argv[1], sys.argv[2])

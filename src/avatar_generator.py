import hashlib
from PIL import Image, ImageDraw


def hash_input(input_text:str) -> str:
    """
    Hash the input text using SHA-256 and return a hex string.
    """
    return hashlib.sha256(input_text.encode('utf-8')).hexdigest()


def generate_color_from_hash(hash_str:str) -> tuple[int, int, int]:
    """
    Generate a color based on the first few characters of the hash.
    """
    return (int(hash_str[:2], 16), int(hash_str[2:4], 16), int(hash_str[4:6], 16))


def draw_avatar(input_text:str, size:int=256, grid_size:int=5) -> Image:
    """
    Create a GitHub-like avatar based on the hashed input text.
    """
    # Create a blank image with white background
    image = Image.new('RGB', (size, size), "white")
    draw = ImageDraw.Draw(image)
    
    # Generate a hash for the input
    hash_str = hash_input(input_text)
    
    # Get a color from the hash
    color = generate_color_from_hash(hash_str)
    
    # Define cell size
    cell_size = size // grid_size
    
    # Generate a mirrored pattern
    for i in range(grid_size):
        for j in range((grid_size + 1) // 2):
            # Determine if cell should be filled based on hash
            fill = int(hash_str[(i * grid_size + j) % len(hash_str)], 16) % 2 == 0
            
            if fill:
                # Draw the cell on both sides to create symmetry
                draw.rectangle(
                    [j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size],
                    fill=color
                )
                draw.rectangle(
                    [(grid_size - j - 1) * cell_size, i * cell_size, (grid_size - j) * cell_size, (i + 1) * cell_size],
                    fill=color
                )
    
    return image


def main():
    # Example usage
    input_text = "example_user"
    avatar = draw_avatar(input_text)
    avatar.show()


if __name__ == "__main__":
    main()

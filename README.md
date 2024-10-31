# GitHub-Like Avatar Generator

This project generates unique, GitHub-style avatar images based on a user's input, like a username or email. Each avatar is created by hashing the input and mapping it to a symmetrical grid pattern and color, ensuring that each avatar is visually distinct.

## Features

- **Unique Identicons**: Each avatar is generated based on a hash of the input text, ensuring that each identifier creates a distinct pattern.
- **Color Customization**: The color of each avatar is derived from the hashed input, creating a unique color scheme for each user.
- **Symmetrical Grid Pattern**: Avatars are generated on a symmetrical 5x5 grid, similar to GitHub identicons.
- **Highly Scalable**: Over 549 billion unique avatars can be generated with this approach.

## Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate and display an avatar, run the following command:

```bash
python avatar_generator.py
```

### Sample Code Usage

Here is a quick example of how to use the avatar generator within your own code:

```python
from avatar_generator import draw_avatar

# Generate an avatar for "example_user"
avatar_image = draw_avatar("example_user")
avatar_image.show()  # Display the generated avatar
avatar_image.save("example_user_avatar.png")  # Save the avatar as a PNG file
```

## License

This project is licensed under the MIT License.

--- 

This version removes the repository-cloning instruction while keeping the setup and usage details clear.
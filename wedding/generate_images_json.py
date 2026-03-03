#!/usr/bin/env python3
"""
Generate images.json for the wedding photo gallery.
This script scans the pictures/ folder and creates a JSON file
listing all image files for the gallery to load dynamically.

Usage: python generate_images_json.py
"""

import os
import json
from pathlib import Path

def generate_images_json():
    """Scan pictures folder and generate images.json"""
    
    # Get the script directory
    script_dir = Path(__file__).parent
    pictures_dir = script_dir / 'pictures'
    
    # Image extensions to look for
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.svg'}
    
    # Collect all image files
    images = []
    
    if pictures_dir.exists():
        for file in sorted(pictures_dir.iterdir()):
            if file.is_file() and file.suffix.lower() in image_extensions:
                images.append(file.name)
    
    # Create the JSON structure
    output = {
        "images": images,
        "count": len(images)
    }
    
    # Write to images.json
    output_file = script_dir / 'images.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"Generated {output_file}")
    print(f"Found {len(images)} images:")
    for img in images:
        print(f"  - {img}")
    
    if len(images) == 0:
        print("\nNo images found in pictures/ folder.")
        print("Add your wedding photos to the pictures/ folder and run this script again.")

if __name__ == '__main__':
    generate_images_json()

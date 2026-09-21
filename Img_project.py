import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

class IMG:
    def __init__(self, path):
        # Load image
        self.image = imread(path)
        # Extract channels
        self.R = self.image[:, :, 0]
        self.G = self.image[:, :, 1]
        self.B = self.image[:, :, 2]
        # Convert to grayscale
        self.grayscale = 0.2989*self.R + 0.587*self.G + 0.114*self.B

    def show_original(self):
        plt.imshow(self.image)
        plt.title("Original Image")
        plt.axis("off")
        plt.show()

    def show_grayscale(self):
        plt.imshow(self.grayscale, cmap='gray')
        plt.title("Grayscale")
        plt.axis("off")
        plt.show()

    def apply_filter(self, cmap_name):
        """Apply any colormap filter by name"""
        plt.imshow(self.grayscale, cmap=cmap_name)
        plt.title(f"Filter: {cmap_name}")
        plt.axis("off")
        plt.show()

    def show_all_filters(self, batch_size=12):
        """Show all colormaps in batches"""
        colormaps = plt.colormaps()
        for start in range(0, len(colormaps), batch_size):
            plt.figure(figsize=(15,10))
            for i, cmap in enumerate(colormaps[start:start+batch_size]):
                plt.subplot(3, batch_size//3, i+1)
                plt.imshow(self.grayscale, cmap=cmap)
                plt.title(cmap, fontsize=8)
                plt.axis("off")
            plt.tight_layout()
            plt.show()


# ------------------- MAIN MENU -------------------
def main():
    INP = input("Enter image path: ")
    img = IMG(INP)

    while True:
        print("\n----- Image Filter Menu -----")
        print("1. Show Original Image")
        print("2. Show Grayscale Image")
        print("3. Apply Specific Filter")
        print("4. Show All Filters (Batch)")
        print("0. Exit")

        choice = int(input("Enter your choice :- "))

        if choice == 1:
            img.show_original()
        elif choice == 2:
            img.show_grayscale()
        elif choice == 3:
            cmap = input("Enter filter name (e.g., jet, hot, cool, viridis, plasma, gray): ")
            img.apply_filter(cmap)
        elif choice == 4:
            batch = int(input("Enter batch size (default 12): ") or 12)
            img.show_all_filters(batch_size=batch)
        elif choice == 0:
            print("Thank you for using Image Filter Project!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()

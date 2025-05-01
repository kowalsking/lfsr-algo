
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# === Параметри ===
BLOCK_ROWS = 15
BLOCK_COLS = 15
LFSR_SEED = 0b10101110101
LFSR_TAPS = [10, 7, 0]

# === Функція LFSR ===
def lfsr_complete(seed, taps, length):
    sr = seed
    mask = (1 << sr.bit_length()) - 1
    sequence = []
    seen = set()
    while len(sequence) < length:
        xor = 0
        for t in taps:
            xor ^= (sr >> t) & 1
        sr = ((sr << 1) & mask) | xor
        val = sr % length
        if val not in seen:
            sequence.append(val)
            seen.add(val)
    return sequence

# === Завантаження або створення тестового зображення ===
image_path = 'sample_image.jpg'
try:
    img = Image.open(image_path).convert('RGB')
except FileNotFoundError:
    img = Image.new('RGB', (240, 180), color='white')
    for i in range(12):
        x = (i % 4) * 60
        y = (i // 4) * 60
        Image.Image.paste(img, Image.new('RGB', (60, 60), color=(i * 20, 100, 150)), (x, y))
    img.save(image_path)

img_np = np.array(img)
h, w, _ = img_np.shape
block_h = h // BLOCK_ROWS
block_w = w // BLOCK_COLS

# === Розбиття зображення на блоки ===
def divide_blocks(image, rows, cols):
    blocks = []
    for r in range(rows):
        for c in range(cols):
            block = image[r*block_h:(r+1)*block_h, c*block_w:(c+1)*block_w]
            blocks.append(block)
    return blocks

# === Збирання зображення з блоків ===
def assemble_blocks(blocks, rows, cols):
    img = np.zeros((rows*block_h, cols*block_w, 3), dtype=np.uint8)
    for idx, block in enumerate(blocks):
        r = idx // cols
        c = idx % cols
        img[r*block_h:(r+1)*block_h, c*block_w:(c+1)*block_w] = block
    return img

# === Шифрування ===
def encrypt_image(image, seed, taps, rows, cols):
    blocks = divide_blocks(image, rows, cols)
    perm = lfsr_complete(seed, taps, len(blocks))
    scrambled = [blocks[i] for i in perm]
    return assemble_blocks(scrambled, rows, cols), perm

# === Дешифрування ===
def decrypt_image(scrambled_img, perm, rows, cols):
    scrambled_blocks = divide_blocks(scrambled_img, rows, cols)
    descrambled_blocks = [None] * len(perm)
    for i, p in enumerate(perm):
        descrambled_blocks[p] = scrambled_blocks[i]
    return assemble_blocks(descrambled_blocks, rows, cols)

# === Повна демонстрація ===
scrambled_img, perm = encrypt_image(img_np, LFSR_SEED, LFSR_TAPS, BLOCK_ROWS, BLOCK_COLS)
descrambled_img = decrypt_image(scrambled_img, perm, BLOCK_ROWS, BLOCK_COLS)

# === Виведення результатів ===
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(img_np)
axs[0].set_title("Оригінал")
axs[1].imshow(scrambled_img)
axs[1].set_title("Зашифроване (LFSR)")
axs[2].imshow(descrambled_img)
axs[2].set_title("Розшифроване (LFSR)")
for ax in axs:
    ax.axis('off')
plt.tight_layout()
plt.show()

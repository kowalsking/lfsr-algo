
# 🔐 LFSR Image Encryption Demo

Цей проєкт демонструє простий спосіб **шифрування та розшифрування зображення** за допомогою алгоритму **LFSR (Linear Feedback Shift Register)**.

## 🧩 Що він робить:
- Ділить зображення на блоки (за замовчуванням 15×15)
- Генерує псевдовипадкову перестановку блоків за допомогою LFSR
- Переставляє блоки — створює зашифроване зображення
- Повертає блоки у правильний порядок — розшифровує зображення

---

## ⚙️ Як запустити проєкт

### 1. Клонувати репозиторій (або завантажити `.py` файл)
```bash
git clone https://github.com/your-username/lfsr-image-encryption.git
cd lfsr-image-encryption
```

### 2. Створити віртуальне середовище (рекомендовано)
```bash
python -m venv venv
```

### 3. Активувати середовище
- **Windows:**
```bash
venv\Scripts\activate
```
- **macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Встановити залежності
```bash
pip install -r requirements.txt
```

або вручну:
```bash
pip install pillow numpy matplotlib
```

### 5. Запустити скрипт
```bash
python lfsr_image_encryption.py
```

## 🛠 Залежності:
- Python ≥ 3.7
- Pillow
- NumPy
- Matplotlib

---

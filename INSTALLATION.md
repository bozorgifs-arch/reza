# 📦 راهنمای نصب Nobitex AI Scalper Pro

## Windows

### گام 1: نصب Python
1. دانلود از: https://www.python.org/downloads/
2. **اهم:** تیک "Add Python to PATH" را بزن
3. Next → Install

### گام 2: نصب پروژه

```bash
# کلون کردن repository
git clone https://github.com/bozorgifs-arch/reza.git
cd reza

# ایجاد محیط مجازی (اختیاری اما توصیه‌شده)
python -m venv venv
venv\Scripts\activate

# نصب نیاز‌مندی‌ها
pip install -r requirements.txt
```

### گام 3: تنظیم Telegram (اختیاری)

```bash
# کپی فایل
copy .env.example .env

# ویرایش .env با Notepad
# اضافه کن:
# TELEGRAM_BOT_TOKEN=your_token
# TELEGRAM_CHAT_ID=your_id
```

### گام 4: اجرا

```bash
python run_strategy_Version1.py
```

---

## Mac

```bash
# نصب Homebrew (اگر ندارید)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# نصب Python
brew install python@3.11

# بقیه مراحل مثل Linux
```

---

## Linux (Ubuntu/Debian)

```bash
# نصب Python و pip
sudo apt update
sudo apt install python3 python3-pip python3-tk

# کلون و نصب
git clone https://github.com/bozorgifs-arch/reza.git
cd reza

# محیط مجازی
python3 -m venv venv
source venv/bin/activate

# نیاز‌مندی‌ها
pip install -r requirements.txt

# اجرا
python3 run_strategy_Version1.py
```

---

## Docker (اختیاری)

```bash
# ساخت image
docker build -t nobitex-scalper .

# اجرا
docker run -it nobitex-scalper
```

---

## مشکلات عام

### ❌ "Python not found"
- Python را بازنصب کن (ADD TO PATH را انتخاب کن)

### ❌ "No module named tkinter"
**Linux:**
```bash
sudo apt install python3-tk
```

### ❌ "pyttsx3 error"
```bash
pip install pyttsx3 --upgrade
```

### ❌ Permission Denied
```bash
chmod +x run_strategy_Version1.py
```

---

## ساخت EXE (Windows)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed run_strategy_Version1.py
```

فایل exe در `dist/` قرار می‌گیرد.

---

**آماده‌ای؟** شروع کن! 🚀

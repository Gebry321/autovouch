# 📜 How To Set Up and Run `auto vouch` Script

## 1. Install Python 3.10 or Higher
- Download **Python 3.10 or above** from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Important**: During install, **check** the box that says **"Add Python to PATH"**.

---

## 2. Prepare the Script Files
You must have these files ready **in the same folder**:
- `main.py` (your script)
- `proxies.txt` (can be **empty** or filled with proxies)
- `token.txt` (must be filled with tokens)
- `word.txt` (must be filled with text lines/messages)

---

## 3. Edit the Script (Channel ID)
- Open `main.py` with any text editor (like Notepad or VSCode).
- Go to **line 16** and **replace** the current number with **your own Discord channel ID**:

```python
ref = YOUR_CHANNEL_ID_HERE
```

- If you don't update this, the script won't know where to send the messages!

---

## 4. Open CMD in the Script Folder
- Open the folder where the files are located.
- **Shift + Right Click** inside the folder → select **"Open PowerShell window here"** or **"Open Terminal here"**.
- Or:
  - **Click** on the folder address bar (at the top).
  - **Type** `cmd` and **press Enter**.

---

## 5. Run the Script
In the command line, type:

```bash
auto vouch main.py
```

If that doesn't work, simply type:

```bash
auto
```
then press **TAB** to autocomplete the filename, and hit **Enter**.

---

## 6. Install Missing Libraries
If you get an error like `ModuleNotFoundError: No module named 'requests'`, you need to install the missing libraries manually:

```bash
pip install requests
pip install tls-client
```

- Install any other missing libraries if it asks for them.
- **Tip**: If you're unsure how to fix an error, **Google it** or **ask ChatGPT**.

---

## 7. Important Notes
- **proxies.txt**
  - If empty, the script **won't use proxies**.
  - If filled, it will randomly choose proxies for sending messages.
- **token.txt**
  - Must have one **Discord token per line**.
- **word.txt**
  - Must have one **message per line**.
- Make sure everything is saved correctly and located in the right folder.

---

# ✅ After setting everything up once, you can easily rerun it anytime!

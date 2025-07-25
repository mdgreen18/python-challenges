# 📦 Python Challenge 1: Email Parser

## 🧠 Problem Statement
You’ve been given a file full of email addresses (one per line). Your task is to **read the file**, **validate each email**, and write the results to two new files.

---

## 📥 Input
Plain text file (`emails.txt`) with lines like:
```
john.doe@example.com
invalid_email@com
jane123@domain.net
noatsymbol.com
```

---

## 🎯 Requirements
1. Prompt for the input file path
2. Validate using regex or logic
3. Save:
   - Valid emails → `valid_emails.txt`
   - Invalid emails → `invalid_emails.txt`
4. Print how many were valid/invalid

---

## 🔧 Extras
- Use `re` module
- Add exception handling for missing files

---

# 🛠 Python Challenge 2: Config File Checker

## 🧠 Problem Statement
You’re building a script that validates a JSON-based config file. If the config file is missing required keys, insert defaults and save.

---

## 🎯 Requirements
1. Load a `config.json` file
2. Required keys:
   - `"api_key"` (default = `"DEFAULT_KEY"`)
   - `"timeout"` (default = `60`)
   - `"debug"` (default = `false`)
3. Add missing keys
4. Save updated config and print results

---

## 🔧 Bonus
- Backup original file
- Validate types (e.g. timeout = int)
- Use `try/except` for errors

---

# ⚠️ Python Challenge 3: Exception Logging Decorator

## 🧠 Problem Statement
Create a **function decorator** called `@safe_execute` that wraps any function and logs exceptions to a file.

---

## 🎯 Requirements
1. Define `@safe_execute`
2. On exception:
   - Log to `errors.log`:
     - Function name
     - Error message
     - Timestamp
   - Return None

---

## ✅ Example
```python
@safe_execute
def divide(x, y):
    return x / y

divide(10, 2)  # 5.0
divide(10, 0)  # Logs ZeroDivisionError
```

---

## 📄 Log File Example
```
[2025-07-21 10:45:12] Error in function divide: ZeroDivisionError - division by zero
```

---

## 🔧 Bonus
- Allow `@safe_execute(log_file="log.txt")`
- Use `functools.wraps` and `datetime`

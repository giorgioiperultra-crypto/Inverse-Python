# Inverse Python

Inverse Python is a small “inverse” language based on Python.  
All commands **must be written backwards**, while the rest of the code is normal Python.

---

## Supported Commands

Some examples:

| Inverse | Python |
|---------|--------|
| tnirp   | print  |
| fi      | if     |

For the full list of supported commands, read the file `supported commands.txt`.

---

## How to Use

1. Make sure that `inv.py` and your `.inv` file are **in the same folder**.  
2. Open your terminal.  
3. Navigate to the folder and run your `.inv` file (example below):

```

cd C:\Users\Username\Desktop\yourdirectory  
python inv.py run yourprogram.inv

# example.inv
x = 0

elihw True:
    x = x+1
    fi x < 5:
        tnirp(x)


# Expected output:
4  
3  
2  
1

```

---

## Notes

- Remember: **only the main commands must be reversed** (like `print` → `tnirp`, `if` → `fi`); the rest of the code is standard Python.  
- Always check `supported commands.txt` to see which commands are supported in the `.inv` language.  
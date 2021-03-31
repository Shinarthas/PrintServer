import win32api
import  win32print

GHOSTSCRIPT_PATH = "C:\\ghostscript\\bin\\gswin32.exe"
GSPRINT_PATH = "C:\\gsprint\\gsprint.exe"

# YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
currentprinter = win32print.GetDefaultPrinter()

win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "document.pdf"', '.', 0)
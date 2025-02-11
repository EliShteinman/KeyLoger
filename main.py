import sys
import subprocess

def ensure_packages_installed(requirements_file="requirements.txt"):
    try:
        with open(requirements_file, "r") as f:
            packages = [line.strip() for line in f.readlines() if line.strip() and not line.startswith("#")]
        
        for package in packages:
            try:
                __import__(package.split("==")[0])  # מנסה לייבא את החבילה
            except ImportError:
                print(f"📦 {package} לא נמצא, מתקין...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        
        print("✅ כל הספריות מותקנות!")
    
    except FileNotFoundError:
        print(f"⚠️ הקובץ {requirements_file} לא נמצא!")

# קרא לפונקציה בתחילת הקוד
ensure_packages_installed()
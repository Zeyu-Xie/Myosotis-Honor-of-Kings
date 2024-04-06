import sys
import subprocess
import time

if __name__ == "__main__":
    
    start_time = time.time()

    print("Running versions/main.py")
    subprocess.run([sys.executable, "./versions/main.py"])
    print("Running heros/main.py")
    subprocess.run([sys.executable, "./heros/main.py"])

    end_time = time.time()

    print(f"Time taken: {end_time - start_time} seconds")
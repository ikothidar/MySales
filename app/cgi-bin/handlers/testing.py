import sys
import os

print(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

print(sys.path)

print(sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

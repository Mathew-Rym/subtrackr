import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).parent))

try:
    from models.subscription import Subscription
    print("SUCCESS! Subscription class imported")
    print("Class definition:", Subscription.__doc__)
except ImportError as e:
    print("FAILED! Error details:")
    print(f"Python path: {sys.path}")
    print(f"Error: {e}")

# SHA-256 Implementation

Implementation of SHA-256 algorithm from scratch based on the Wikipedia pseudocode.

## Files

- `sha256.py` - SHA-256 implementation
- `main.py` - Script to hash the Book of Mark
- `book_of_mark.txt` - Text from https://quod.lib.umich.edu/cgi/r/rsv/rsv-idx?type=DIV1&byte=4697892

## Usage

```bash
python main.py
```

This will compute the SHA-256 hash of the Book of Mark and verify it against Python's hashlib.

## How it works

The SHA-256 algorithm:
1. Pads the message to be a multiple of 512 bits
2. Processes the message in 512-bit chunks
3. Uses bitwise operations (rotate, XOR, AND, OR) with round constants
4. Produces a 256-bit (64 hex character) hash

Reference: https://en.wikipedia.org/wiki/SHA-2

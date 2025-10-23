The Wikipedia pseudocode has been used to implement SHA-256 algorithm in plain-text code.

Files
sha256.py - SHA-256 implementation
main.py - Bookof Mark hash script.
book of mark.text - Content of https://quod.lib.umich.edu/cgi/r/rsv/rsv-idx?type=DIV1&byte=4697892.
Usage
python main.py
It will compute a SHA-256 of the Book of Mark and compare it to the library of hash functions of Python.

How it works
The SHA-256 algorithm:

padding of the message to 512 bits.
Breaks down the message into 512 bit blocks.
Round constants were used to perform bitwise operations (rotate, XOR, AND, OR).
Computes 256-bit (64 character in hex) hash.
Reference: https://en.wikipedia.org/wiki/SHA-2

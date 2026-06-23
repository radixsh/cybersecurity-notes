Completed 2026-03-25

logs.txt --> solution.py --> output.png --> solution.py

The log file looks like one long base64 string. Decode it to bytes and save the
bytes to a file using `log_to_base64()`.

The output file's file signature says it's a PNG, so set the file extension to
PNG.

The PNG shows a long string of numbers. Copy this painstakingly by hand into a
string:
7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F62653836303237397D.

If we try to interpret it as a string, the first character will be "7", or 0x37,
and it won't get interpreted as bytes. So make it a Python bytes object by
sandwiching b"" around it.

Decode the bytes object using `decode_hexstring()`. This yields the flag.

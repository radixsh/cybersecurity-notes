$ file img.jpg
img.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9", baseline, precision 8, 640x640, components 3

base64 to ascii
c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9 --> steghide:cEF6endvcmQ=
cEF6endvcmQ= --> pAzzword

$ steghide --extract -sf img.jpg -p pAzzword
wrote extracted data to "flag.txt".
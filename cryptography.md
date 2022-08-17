# Cryptography
## Tools
* John the Ripper
    * [Beginner's Guide](https://www.hackingarticles.in/beginner-guide-john-the-ripper-part-1)
    * [JTR Cheatsheet](https://countuponsecurity.files.wordpress.com/2016/09/jtr-cheat-sheet.pdf)
* hashcat
* [CyberChef](https://gchq.github.io/CyberChef)

## Notes
### Basic decoding
* Hexadecimal: 2 digits per unit of meaning; often starts with 0x; consists of
  letters from alphabet `0123456789abcdef`
* Base64: length is divisible by 4; often padded with `==`
* [ascii codes to ascii characters](https://convert.town/ascii-to-text)
* Octal: base 8; just use CyberChef
* Substitution cipher: letters are replaced by other letters;
  [quipqiup](quipqiup.com) is good at automatically decoding substitution
  ciphers
    * Caesar cipher (aka rot13): shift the alphabet by some number; e.g., with a
      shift of 3, A becomes D, B becomes E
    * atbash: A becomes Z, B becomes Y, etc.
    * vigenere: you have to have a key
    * [Statistical analysis for substitution ciphers](https://www.guballa.de/substitution-solver)
    * [QWERTY fingers on dvorak keyboard](http://wbic16.xedoloh.com/dvorak.html)
* Morse code: try a lot of different online decoders, and make sure to check for
  caps, etc.
    * Looks like `----. ----. ----. / -.... -.... -.... / ---.. ---.. / ..---
      ..--- ..--- / ..---/ -.... -.... / --... --... --... / ...-- ...-- / ..---
      / ...-- / -.... / ----.----. ----. / --... --... --... --... / -.... /
      --... --... --... --...`
    * There will be dots, dashes, probably spaces (between characters), and
      probably slashes (between words). [Morse Decoder](https://morsedecoder.com)
      can decode that without trouble.
* [Decimal to ascii without a clear delimiter](https://onlineasciitools.com/convert-decimal-to-ascii)
    * Example ctf challenge: [SECRET CONVE.RSA.TIONS](https://github.com/Tartifletteuhh/UnlockTheCityCTF2022-WriteUps-SKBO/tree/master/District2/Secret_ConveRSAtions)
* SMS
    * Looks like `999 666 88 222 2 66 777 33 2 3 6 999 7777 6 7777`
    * Example ctf challenge: [Tring Tring](https://github.com/S-H-E-L-L/S.H.E.L.L-CTF-2022/blob/main/crypto/Tring%20Tring/solution.md)

### Weird ones
* Pigpen
* [Birds on a wire](https://www.dcode.fr/birds-on-a-wire-cipher)
    * Example ctf challenge: [Tweeeeet](https://github.com/S-H-E-L-L/S.H.E.L.L-CTF-2022/blob/main/crypto/Tweeeeet/solution.md)
    * It looks like the birds have to be precise matches; it isn't just a bird
      in general looking left/up/whatever. So the dcode link would be helpful.
    * Also, don't do this by hand. I'm never getting back the ten minutes I just
      spent walking through that chal.
* Railfence: rearrange text in a wave pattern (up and down) and read from left
  to right
* [Esoteric programming languages](https://esolangs.org/wiki/Language_list)
    * [Brainfuck](https://esolangs.org/wiki/Brainfuck) looks like
      `++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>
      >.<-.<.+++.------.--------.>>+.>++.`
    * [Malbolge](https://malbolge.doleczek.pl) looks like
      ```('&%:9]!~}|z2Vxwv-,POqponl$Hjig%eB@@>}=<M:9wv6WsU2T|nm-,jcL(I&%$#"
      `CB]V?Tx<uVtT`Rpo3NlF.Jh++FdbCBA@?]!~|4XzyTT43Qsqq(Lnmkj"Fhg${z@>
      ```



### Actual decryption
* XOR: in py, ord() converts character to number; chr() converts number to
  character 
    * Example ctf challenge: [OX9OR2](https://github.com/S-H-E-L-L/S.H.E.L.L-CTF-2022/tree/main/crypto/OX9OR2)
    ```
    key = 'ctf{flag}'
    output = ''
    for i in range(len(input)):
        output += chr(ord(input[i]) ^ ord(key[i % len(key)]))
    ```
* MD5: 128-bit output (32 ascii chars); easily hackable using dictionary attacks
  like John the Ripper with `rockyou.txt`
    * [passwordrecovery.io](https://passwordrecovery.io/md5): MD5 hash cracker;
      it'll compare your hash against hashes from `rockyou.txt` very quickly
* [Getting Started with John the Ripper](https://www.tunnelsup.com/getting-started-cracking-password-hashes/)
* [hashcat](https://github.com/hashcat/hashcat)
    * If you know part of the plaintext of a hash, then use [mask attack](https://hashcat.net/wiki/doku.php?id=mask_attack)
    * Download and unzip and make as necessary
    * Make a mask file. In this case, we know the plaintext is
      `FLAG-HQNT-?d?d?d?d` where `?d` indicates some numerical digit, so create
      a `file.hcmask` with that string in it. Then run `./hashcat -a 3 -m 0
      --show ../All\ Ctfs/NCLFall2019/md5masked-file.hcmask`
* [hash toolkit for md5, sha1, sha256, sha512](https://hashtoolkit.com)
* [NTLM aka ntHash](https://medium.com/@petergombos/lm-ntlm-net-ntlmv2-oh-my-a9b235c58ed4):
  Windows hash system
    * `./john --format=netntlmv2 NAME.txt`
* RSA
    * [My explanation of RSA](rsa.md)
    * [RSA step by step explanation](https://www.cryptool.org/en/cto/rsa-step-by-step)
    * [RSA calculator](https://www.cs.drexel.edu/~jpopyack/Courses/CSP/Fa17/notes/10.1_Cryptography/RSA_Express_EncryptDecrypt_v2.html)
    * [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool): can do lots of
      attacks
* [encrypted pdfs](https://ctftime.org/writeup/8707): `pdfcrack --wordlist=rockyou.txt NAME.pdf`
* shadow and passwd file dehashing
    * [shadow format](https://www.linuxquestions.org/questions/linux-security-4/etc-shadow-file-663816): `$1$IwCH$c5VgaFQG9VZdL1UnWDUmj0`
        * The part between the first two “$”s is the type of algorithm used (1
          indicates MD5)
        * The second part is the salt
        * The third part is the hash itself
        * `touch` a text file and fill it with the salt and the hash as given in
          the shadow document
        * Use john the ripper: `./john/run/john --format=md5crypt-opencl
          --wordlist=../../rockyou.txt dumps.txt`
    * `./john/run/unshadow passwd.txt shadow.txt > passwords.txt`
    * `./john/run/john --format=md5crypt-opencl --wordlist=../../rockyou.txt
      passwords.txt`

### Steganography: hiding messages in files
* [0xRick's list of tools/resources](https://0xrick.github.io/lists/stego): some
  person's
* [First steps cheatsheet](https://pequalsnp-team.github.io/cheatsheet/steganography-101)
* `binwalk flag.png`
    * If you see something interesting, extract it with `unzip flag.png`
* `foremost`
* Check plaintext sections with `cat`, `strings`, and/or `hexdump -C` or `xxd` (shows both binary and hexdump)
* Image metadata
	* `exiftool`
    * `mdls`
* stegsolve
* steghide
* Check file's [magic numbers](https://en.wikipedia.org/wiki/List_of_file_signatures)
  to make sure it is what its file extension says it is
* [StegOnline](https://stegonline.georgeom.net/upload)

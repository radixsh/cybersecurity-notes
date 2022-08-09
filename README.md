# CTF notes
## RSA
[Source](https://github.com/Tartifletteuhh/UnlockTheCityCTF2022-WriteUps-SKBO/tree/master/District2/Secret_ConveRSAtions)

Factorization attack: if we know `N`, `p`, and `q`, then we can find the private
key `d` and the totient function `phi(n)` which will give us access to the
message.

`c = m^e, mod n`

(ciphertext = plaintext to the power of public exponent, mod product of two
large primes)

`m = c^d, mod n`

(plaintext = ciphertext to the power of private exponent, mod the same product
as before)

How to turn ciphertext into plaintext given product `n` and public exponent `e`: 
1. Given product `n`, use factorDB.py to find prime factors `p` and `q`:
   `python3 factorDB.py YOUR_N_HERE`
2. Find totient function, which counts the positive ints up to `n` that are
   relatively prime to `n`: `phi = (p - 1) * (q - 1)`
3. Given exponent `e`, find private key `d`: `d = inverse(e, phi)`
4. The decrypted message is **c to the power of d, modulus n**: `m = pow(c, d,
   n)`

(Sometimes decimal to ascii is difficult; CyberChef won't be able to do it, but
[onlineasciitools](https://onlineasciitools.com/convert-decimal-to-ascii) can
decode decimal to ascii without a clear delimiter. This was also identifiable as
requiring hex to ascii decoding because 123 is `{` and 125 is `}`.)

## Threat intelligence tools 
* [Urlscan.io](https://urlscan.io): website analysis, automated crawling
* [ThreatFox](https://threatfox.abuse.ch): indicators of compromise (IOCs)
* [URLhaus](https://urlhaus.abuse.ch): malware URLs
* [MALWAREbazaar](https://bazaar.abuse.ch): malware samples
* [PhishTool Community](https://app.phishtool.com/submit): emails
* [VirusTotal](https://www.virustotal.com/gui/home/upload): files / domains /
  IPs / URLs

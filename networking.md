# Networking
## Tools
* nmap
    * To view open ports/services: `nmap -Pn ports.cityinthe.cloud`
    * To view UDP ports in addition to TCP ports: `sudo nmap -sU -sT -p0-65535 ports.cityinthe.cloud`
    * While things are being scanned, you can press `e` to get a report on the
      progress
* Burp Suite
* FoxyProxy
    * [Selective proxy routing with FoxyProxy patterns](https://rynehanson.com/infosec/foxyproxy-patterns/)
* Wireshark
    * [Chappell University](https://chappell-university.com/lauras-lab)
    * To see credentials a user tried: Click on one of the pcaps > Follow > TCP
      Stream
    * To see MD5 checksum of an uploaded file: apply the filter ftp-data and
      save the data from the packet containing the first stream of data by
      following its TCP Stream and selecting “Show Data As > Raw” and saving
      that file to your disk. Find the checksum by running md5sum filename in
      Terminal.
    * In HTTP traffic logs, you see the md5sum of a file downloaded online
      (using wget) with File > Export Objects > HTTP and then using md5sum in
      terminal
    * To see pings: filter for icmp
    * To extract (or see details of) files from pcaps: File > Export Objects > HTTP
        * [extracting files from pcaps](https://crucialsecurity.wordpress.com/2011/02/24/extracting-files-from-packet-captures/)
        * Make sure there are no filters for the packets
        * Identify the packet in which data is actually being transferred (i.e.,
          the one *right after* the request)
        * Follow the TCP conversation of that packet
        * Change view to hex data and identify magic number; note what the
          transferred file’s extension should be
        * Change view to raw and Save As something without a file extension
          (filename)
        * In Terminal, run `file filename`; it should line up with the magic
          number.  Rename it with the appropriate extension, and then you can do
          what you need to do with the file — unzip it, extract it from tar
          archive, cat it, etc.
    * To filter by strings in the Info column: Edit > Find Packet > check String
      > search whatever string you need

## Notes
* [subnets](http://steves-internet-guide.com/subnetting-subnet-masks-explained)
    * A valid IP of the 10.128.0.0 network is 10.128.0.1
    * [How to calculate prefix, network, subnet, and host numbers](https://networkengineering.stackexchange.com/questions/7106/how-do-you-calculate-the-prefix-network-subnet-and-host-numbers)
    * Use [subnet calculator](https://wintelguy.com/subnetcalc.pl) to find
      subnet masks
    * maximum netmask = minimum hostmask
    * [The slash number after an IP](https://networkengineering.stackexchange.com/questions/3697/the-slash-after-an-ip-address-cidr-notation) (Classless Inter-Domain Routing (CIDR) notation) represents the number of consecutive ones in the subnet mask
        * 192.168.10.0/24 is equal to the network 192.168.10.0 with a subnet
          mask 255.255.255.0 because if you make 24 consecutive ones, then you
          get 11111111.11111111.11111111.00000000, which is 255.255.255.0
    * Given an IP, say, 10.10.15.10/16:
        * Convert each of the four octets in that IP to binary:
          00001010:00001010:00001111.00001010
        * [Find the subnet mask](https://aelius.com/njh/subnet_sheet.html)
          and convert it into binary
        * Perform a bitwise AND operation with those two numbers:
          00001010.00001010:00000000.00000000
        * Convert back to decimal: 10.10.0.0
        * And now you know that any IP address from 10.10.0.0 to 10.0.255.255 is
          part of that network :)
    * How many hosts are possible in a network? Compare the /## number to the
      cheat sheet for subnetting masks, and use your brain if necessary
        * For example, /14 isn't on the chart, but you know you can multiple the number
          of addresses for a 16 by 2 and then by 2 again and then subtract 2 to
          get the number of hosts [citation needed]
* To find wireless password (in hex): `aircrack-ng "foobar.cap" -w rockyou.txt`

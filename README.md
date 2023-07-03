## WD-Decryption
The Western Digital Decryption tools for LINUX

## The Files : 
* [wd-decrypt.py]() : generate's the .BIN file ( 40bytes ) contains the decryption password 
* [adapter.sh]() : Automation script for the drive encryption

<br>
<br>

## The commands : 

<br>

1. ```dmesg | grep -i scsi ```
<br> Detect **sdd** the WD Adapter Drive

2. ```./wd-decrypt.py PASSWORD >password.bin```
<br> Initialize your password into the script and Generate the Password file

3. Install 'sg3_utils' 
<br> This is the [SG_UTILS](https://www.linuxfromscratch.org/blfs/view/svn/general/sg3_utils.html) package you need to install depending on the Linux Distro you use. 

4. sudo sg_raw -s 40 -i password.bin /dev/sdd c1 e1 00 00 00 00 00 00 28 00

<br>
<br>

## The adapter.sh : 

<br>

1. `python ./home/username/Desktop/cookpw.py SIFO123 >password.bin`:  
   This command runs a Python script called "wd-decrypt.py" located at "/home/username/Desktop" directory. It takes an argument "PASSWORD" and redirects the output to a file named "password.bin". 


2. `sudo sg_raw -s 40 -i password.bin /dev/SDD c1 e1 00 00 00 00 00 00 28 00`:  
   This command is executed with superuser privileges ("sudo") and performs a low-level SCSI operation using the "sg_raw" command. It sends a SCSI command sequence to a device located at "/dev/SDD" (which could be a storage device like a hard drive).

   The specific command sequence being sent is represented by the hexadecimal values "c1 e1 00 00 00 00 00 00 28 00".


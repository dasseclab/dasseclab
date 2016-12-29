#!/usr/bin/python3.4.5
#DKEY - An Anti-Forensic Tool
#Written by Drew Sutton (@dasseclab; https://twitter.com/dasseclab)
#Distributed on GitHub at https://github.com/dasseclab/dkey

import os
import sys
import crypt

def ApplyCrypto():
    """Method to apply cryptography to selected drives. Crypto method works in three phases, each phase using a new algorithm: AES (DH), Serpent, & Threefish."""

def DriveList():
    """Gather UNIX-like connected device information"""
hd="ls /dev/hd*"
if hd >= 0
    return hd
    else print("No IDE or SCSI Devices")
sd="ls /dev/sd*"
if sd >= 0
    return sd
    else print("No SATA or SAS Devices")

def SSDList():
    """Build an array of any Solid State Drives present in system."""
    for drive in session:
        do
        'sudo hdparm -I $drive | grep -i 'Solid State Device''
        if drive #is SSD create array SSD.
        #else, create array HDD.

def SecureSSDErase():
    """Perform SSD Secure erase on each SSD in the session."""
        print("Performing secure erase on SSDs")
        for drive in SSD:
            do
            'sudo hdparm -I $drive | grep -i frozen'
            if return == ' frozen'
            do
            'sudo hdparm -Y $drive'
            print("Disconnect power to" $i)
            if return == 'not frozen'
            continue
        do
        'sudo hdparm --user-master u --security-set-pass QWERTYdrowssap!' $i
        do
        'sudo hdparm --user-master u --security-erase QWERTYdrowssap!' $i
def DiskWipe():
    """Module for doing a repeat of overwriting data."""

def main():
DriveList():
print("Select a device to DKEY")
device = raw_input()
if device is '/dev/sda'
    print("WARNING! dkey on this device will not complete unless dkey runs from another source!")
    print("Confirm or Deny?")
    decision = raw_input()
    if decision == "Confirm":
        continue
    elif decision == "Deny"
        exit()
    else print("Try again")
elif device != (/dev/sda):
SSDList():
ApplyCrypto():
    for drive in device
    print("Applying AES Cryptography To Device")
    #apply crypto phase1
    #generate key via /dev/urandom with method1 (AES-512)

    for drive in device
    print("Applying Serpent Cryptography To Device")
    #apply crypto phase2
    #generate key via /dev/urandom with method 2 (Serpent)

    for drive in device
    print("Applying Threefish Cryptography To Device")
    #apply crypto phase3
    #generate key via /dev/urandom with method 3 (Threefish)
SecureSSDErase():
    print("SSDs have completed secure erase")
    print("HDDs continuing with dkey")
DiskWipe():



#Wipe data from sectors
for i in HDDs
    do "dd if=/dev/urandom of=$i bs=512"
        print("Starting pass 1 of 3 of data wipe")
        if #errors, print to log & stop
        elif continue
    do "dd if=/dev/urandom of=$i bs=512"
        print("Starting pass 2 of 3 of data wipe")
        if  # errors, print to log & stop
        elif continue
    do "dd if=/dev/urandom of=$i bs=512"
        print("Starting pass 3 of 3 of data wipe")
        if  # errors, print to log & stop
        elif continue
for i in HDDs:
    if #errors == 0
        #complete script
        print("Data successfully destroyed")
    elif #errors > 0
        print("There are errors present and data destruction cannot be validated.")


if __name__=="main()":
        main()
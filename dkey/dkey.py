#!/usr/bin/python3.4.5
"""DKEY - An Anti-Forensic Tool
Written by Drew Sutton (@dasseclab; https://twitter.com/dasseclab)
Distributed on GitHub at https://github.com/dasseclab/dkey"""

import os
import sys
import subprocess
import crypt

def apply_crypto():
    """Method to apply cryptography to selected drives. Crypto method works in three phases, each phase using a new algorithm: AES (DH), Serpent, & Threefish."""

def drive_list():
    """Gather UNIX-like connected device information"""
    hd = subprocess.check_output(['ls', '/dev/hd*'])
    if hd >= 0
        return hd.split()
        else print("No IDE or SCSI Devices")
    sd = subprocess.check_output(['ls', '/dev/sd*'])
    if sd >= 0
        return sd.split()
        else print("No SATA or SAS Devices")

def ssd_list():
    """Build an array of any Solid State Drives present in system."""
    for drive in session:
        ssd = subprocess.check_output(['sudo', 'hdparm', '-I' drive '|', 'grep', '-i' 'Solid State Device'])
        return ssd.split()
        return hdd.split()

def secure_ssd_erase():
    """Perform SSD Secure erase on each SSD in the session."""
        print("Performing secure erase on SSDs")
        for drive in ssd:
            subprocess.call(['sudo', 'hdparm', '-I' drive '|', 'grep', '-i', 'frozen'])
            if return == 'frozen':
                subprocess.call(['sudo', 'hdparm', '-Y', drive])
                return("Disconnect power to" drive)
                sys.exit(1)
            if return == 'not frozen':
                continue
            subprocess.call(['sudo hdparm --user-master u --security-set-pass QWERTYdrowssap!' drive])
            subprocess.call(['sudo hdparm --user-master u --security-erase QWERTYdrowssap!' drive])
def disk_wipe():
    """Module for doing a repeat of overwriting data."""
    for drive in hdd
        do "dd if=/dev/urandom of=$drive bs=512"
            print("Starting pass 1 of 3 of data wipe")
            if #errors, print to log & stop
            elif continue
        do "dd if=/dev/urandom of=$drive bs=512"
            print("Starting pass 2 of 3 of data wipe")
            if  # errors, print to log & stop
            elif continue
        do "dd if=/dev/urandom of=$drive bs=512"
            print("Starting pass 3 of 3 of data wipe")
            if  # errors, print to log & stop
            elif continue
def main():
    drive_list():
        print("Select a device to DKEY")
        device = raw_input()
    if device is '/dev/sda'
        print("WARNING! dkey on this device will not complete unless dkey runs from another source!")
        print("Confirm or Deny?")
        decision = raw_input()
        if decision == "Confirm":
            continue
        elif decision == "Deny"
            sys.exit(1)
        else print("Try again")
    elif device != (/dev/sda):
    ssd_list():
    apply_cryto():
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
    secure_ssd_erase():
        print("SSDs have completed secure erase")
    print("HDDs continuing with dkey")
    disk_wipe():
    #Wipe data from sectors
    for i in HDDs:
        if #errors == 0
        #complete script
            print("Data successfully destroyed")
        elif #errors > 0
            print("There are errors present and data destruction cannot be validated.")


if __name__=='__main__':
    main()
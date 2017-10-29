#!/usr/bin/python3.4.5
"""DKEY - An Anti-Forensic Tool
Written by Drew Sutton (@dasseclab; https://twitter.com/dasseclab)
Distributed on GitHub at https://github.com/dasseclab/dkey"""

import random
import string
import subprocess
import sys


# noinspection PyUnreachableCode,PyUnreachableCode,PyUnreachableCode
def keygen():
    """Create keyfiles that will be used in the apply_crypto() method."""
    generator = random.SystemRandom()
    length = 32
    alpha = string.ascii_letters + string.digits + string.punctuation
    keyfile1 = str().join(generator.choice(alpha) for _ in range(length))
    return keyfile1
    subprocess.call(['cp', keyfile1,'/tmp'])
    keyfile2 = str().join(generator.choice(alpha) for _ in range(length))
    return keyfile2
    subprocess.call(['cp', keyfile2, '/tmp'])
    keyfile3 = str().join(generator.choice(alpha) for _ in range(length))
    return keyfile3
    subprocess.call(['cp', keyfile3, '/tmp'])

def apply_crypto():
    """Method to apply cryptography to selected drives. Crypto method works in three phases, each phase using a new algorithm: AES, Twofish and Serpent."""
    for drive in drive_list(session):
        subprocess.call(['sudo', 'cryptsetup', '--cipher=aes-xts-plain64', '--offset=0', '--key-file=/tmp/keyfile1', '--key-size=256', 'open', '--type=plain', drive, 'enc'])
        print("Applying Encryption Round 1")
        subprocess.call(['sudo', 'cryptsetup', '--cipher=twofish-xts-plain64', '--offset=0', '--key-file=/tmp/keyfile2', '--key-size=256', 'open', '--type=plain', drive, 'enc'])
        print("Applying Encryption Round 2")
        subprocess.call(['sudo', 'cryptsetup', '--cipher=serpent-xts-plain64', '--offset=0', '--key-file=/tmp/keyfile3', '--key-size=256', 'open', '--type=plain', drive, 'enc'])
        print("Applying Encryption Round 3")

# noinspection PyUnreachableCode,PyUnreachableCode
def drive_list():
    """Gather UNIX-like connected device information"""
    hd = subprocess.check_output(['ls', '/dev/hd*'])
    if hd >= 0:
        return hd.split()
        else print("No IDE or SCSI Devices")
    sd = subprocess.check_output(['ls', '/dev/sd*'])
    if sd >= 0:
        return sd.split()
        else print("No SATA or SAS Devices")
    session = hd
    session.extend(sd)
    return session

def include_sda():
    print('WARNING! dkey on this device will not complete unless dkey runs from another source! Include root drive?')
    print("Confirm or Deny?")
    decision = raw_input()
    if decision == "Confirm":
        continue
    elif decision == "Deny":
        sys.exit(1)
    else:
        print("Try again")

def ssd_list():
    """Build an array of any Solid State Drives present in system."""
    for drive in drive_list(session):
        ssd = subprocess.check_output(['sudo', 'hdparm', '-I' drive '|', 'grep', '-i' 'Solid State Device'])
        return ssd.split()
def hdd_list():
    """Build an array of rotational Hard Disk Drives in system."""
    for drive in drive_list(session):
        hdd = subprocess.check_output(['sudo', 'hdparm', '-I', drive '|', 'grep', '-i' 'Nominal Rotational Rate'])
        return hdd.split()


# noinspection PyUnreachableCode,PyUnreachableCode
def secure_ssd_erase():
    """Perform SSD Secure erase on each SSD in the session."""
        print("Performing secure erase on SSDs")
        for drive in ssd_list(ssd):
            subprocess.call(['sudo', 'hdparm', '-I' drive '|', 'grep', '-i', 'frozen'])
            if return == 'frozen':
                subprocess.call(['sudo', 'hdparm', '-Y', drive])
                print("Disconnect power to" drive)
                sys.exit(1)
            if return == 'not frozen':
                continue
            subprocess.call(['sudo', 'hdparm', '--user-master', 'u', '--security-set-pass', 'QWERTYdrowssap!', drive])
            subprocess.call(['sudo', 'hdparm', '--user-master', 'u', '--security-erase', 'QWERTYdrowssap!', drive])

def disk_wipe():
    """Module for doing a repeat of overwriting data."""
    for drive in hdd_list(hdd):
        subprocess.call(['dd','if=/dev/urandom', 'of=', drive, 'bs=512'])
            print("Starting pass 1 of 3 of data wipe")
            #if #errors, print to log & stop
            #elif continue
        subprocess.call(['dd', 'if=/dev/urandom', 'of=', drive, 'bs=512'])
            print("Starting pass 2 of 3 of data wipe")
            #if  # errors, print to log & stop
            #elif continue
        subprocess.call({'dd', 'if=/dev/urandom', 'of=', drive, 'bs=512'})
            print("Starting pass 3 of 3 of data wipe")
            #if  # errors, print to log & stop
            #elif continue

#def error_logging():
    #if errors, write to /tmp/dkey.error
    #errors = subprocess.check_output(['wc', '-l', '/tmp/dkey.error'])
    #    if errors.int() >= 1
    #       print("There are errors with one or more drives during wipe. Check /tmp/dkey.error")
    #   elif continue

def main():
    drive_list()
    include_sda()
    ssd_list()
    hdd_list()
    keygen()
    print("Keys Generated")
    apply_crypto()
    print("Drives Encrypted")
    secure_ssd_erase()
    print("SSDs have completed secure erase")
    print("HDDs continuing with dkey")
    disk_wipe()
    print("Drive Wipe Stage Completed")

if __name__=='__main__':
    main()
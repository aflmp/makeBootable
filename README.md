# makeBootable
script to create bootable usb in macOS when there's no time

```sh
$ python makeBootable.py -h
usage: makeBootable.py [-h] [-if INPUTFILE] [-of OUTPUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -if INPUTFILE, --inputfile INPUTFILE
                        specify the input file
  -of OUTPUTFILE, --outputfile OUTPUTFILE
                        specify the output file
```
## Example:
```sh
$ python makeBootable.py -if /Users/test/Downloads/iso/exploit.iso -of /dev/disk2
or
$ python makeBootable.py
/dev/disk0 (internal):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                         251.0 GB   disk0
   1:                        EFI EFI                     314.6 MB   disk0s1
   2:          Apple_CoreStorage Macintosh HD            250.0 GB   disk0s2
   3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3

/dev/disk1 (internal, virtual):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                  Apple_HFS Macintosh HD           +249.7 GB   disk1
                                 Logical Volume on disk0s2
                                 25DA8201-0275-43C9-B0ED-4261296E990F
                                 Unencrypted

/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                            Custom Live CD         *4.0 GB     disk2

destination disk path:   /dev/disk2
source iso path:   /Users/test/Downloads/iso/exploit.iso
Unmount of all volumes on disk2 was successful
Writing to disk...
Password: //enter password
Disk /dev/disk2 ejected
Bootable USB created!
```
## Note
 Press `Ctrl + t` to get the status during disk writing process.
```sh
2664+1 records in
2664+1 records out
2794307584 bytes transferred in 139.179738 secs (20076971 bytes/sec)
```

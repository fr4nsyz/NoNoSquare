# NoNoSquare

The last thing I want is for my host system to be compromised because I downloaded a fishy pip package that promised me free robux, so that's why I decided to create this QEMU + KVM powered virtual machine workflow for the ultra paranoid developer.

## Usage



### NOTE:

Editing the `user-data` requires that you rebuild the whole VM to propagate your changes.

To do this, you must delete `jammy-server-cloudimg-amd64.img` and `cloudinit.iso`

Then, you can rerun `cloud-localds cloudinit.iso user-data meta-data`

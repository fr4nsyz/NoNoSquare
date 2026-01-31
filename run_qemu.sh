#!/bin/env bash

# $1 is num RAM (GB)
# $2 is num virtual CPUs

qemu-system-x86_64 \
  -enable-kvm \
  -cpu host \
  -m ${1} \
  -smp 4 \
  -drive file=jammy-server-cloudimg-amd64.img,format=qcow2 \
  -drive file=cloudinit.iso,format=raw \
  -netdev user,id=net0,hostfwd=tcp::2222-:22 \
  -device virtio-net-pci,netdev=net0 \
  -nographic

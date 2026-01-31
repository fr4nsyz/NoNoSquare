#!/bin/env bash

qemu-system-x86_64 \
  -enable-kvm \
  -cpu host \
  -m 8G \
  -smp 4 \
  -drive file=jammy-server-cloudimg-amd64.img,format=qcow2 \
  -drive file=cloudinit.iso,format=raw \
  -netdev user,id=net0,hostfwd=tcp::2222-:22 \
  -device virtio-net-pci,netdev=net0 \
  -nographic

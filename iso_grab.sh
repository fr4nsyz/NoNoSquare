#!/bin/env bash

wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img
qemu-img create -f qcow2 -o backing_file=jammy-server-cloudimg-amd64.img,backing_fmt=qcow2 bean.qcow2 10G

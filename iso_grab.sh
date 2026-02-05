#!/bin/env bash

wget https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img
qemu-img create -f qcow2 -o backing_file=noble-server-cloudimg-amd64.img,backing_fmt=qcow2 bean.qcow2 96G

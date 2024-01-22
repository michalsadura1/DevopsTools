###################################################################################################
Packer commands
###################################################################################################
init
packer init .

fmt
packer fmt 

Build
packer build -force oraclevb-ubuntu.pkr.hcl

Convert json to hcl2
@x-Victus-by-HP-Laptop-16-e0xxx:~/packer$ packer hcl2_upgrade -with-annotations ./ubuntu.json
Successfully created ./ubuntu.json.pkr.hcl. Exit 0

###################################################################################################
cloudinit
###################################################################################################
password hash for cloudinit
mkpasswd --method=sha-512

docs exmaples
https://cloudinit.readthedocs.io/en/latest/development/index.html

examples
https://github.com/justin-p/packer-proxmox-ubuntu2004/blob/main/ubuntu2004.pkr.hcl

useful docs
https://github.com/rlaun/packer-ubuntu-22.04/blob/master/README.md



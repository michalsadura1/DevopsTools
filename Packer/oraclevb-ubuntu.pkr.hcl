packer {
  required_plugins {
    virtualbox = {
      version = "~> 1"
      source  = "github.com/hashicorp/virtualbox"
    }
  }
}


source "virtualbox-iso" "basic-example" {

  guest_os_type    = "Ubuntu_64"
  iso_url          = "https://releases.ubuntu.com/22.04/ubuntu-22.04.3-live-server-amd64.iso"
  iso_checksum     = "a4acfda10b18da50e2ec50ccaf860d7f20b389df8765611142305c0e911d16fd"
  iso_target_path   = "./packer/"
  output_directory  = "./packer/Ubuntu-22.04-Build"
  headless = "false"
  disk_size = "12000"
  memory = "2048"
  nic_type = "82540EM"
  http_directory = "./http"
  boot_wait = "3s"
  boot_command  = [
    "e<wait>",
    "<down><down><down>",
    "<end><bs><bs><bs><bs><wait>",
    "autoinstall ds=nocloud-net\\;s=http://{{ .HTTPIP }}:{{ .HTTPPort }}/ ---<wait>", "<f10><wait>"
    ]
  ssh_username  = "sadura"
  ssh_password  = "sadura"
  ssh_wait_timeout = "14m"
  ssh_port = 22
  ssh_pty = true
  ssh_timeout = "14m"
  ssh_handshake_attempts = "420"
  shutdown_command = "echo sadura | sudo  -S /sbin/shutdown -P now 2>&1 /dev/null"
  //shutdown_commnand = "echo 'ppppp' | sudo -S /sbin/shutdown -P now"  
  vm_name  = "ubuntu-22.04-packer"

}


build {
  sources = ["source.virtualbox-iso.basic-example"]

   provisioner "shell" {
    inline = [
      
      "echo 'Complete...'",
      //"while [ ! -f /var/lib/cloud/instance/boot-finished ]; do sleep 1; done",
      //"echo  sadura | sudo -t -S /sbin/shutdown -P now",
    ]
  }

}

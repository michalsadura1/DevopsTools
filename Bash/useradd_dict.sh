#!/bin/bash
#create user from dict
#create autorized_key file in home
#add to sudosers
#checked on ubuntu20 ->24 

set -x

declare -A users=(
    [michal.sadura1]="ssh-rsa PUBLIC-KEY michal.sadura1"
    [michal.sadura2]="ssh-rsa PUBLIC-KEY michal.sadura2"
 )

# Wypisywanie zawartości słownika
#echo "${users[@]}"

# Wypisywanie wartości dla konkretnego klucza
#echo "${users[michal.sadura2]}"

# Dodawanie nowego klucza i wartości
#slownik[klucz4]="wartość4"

# Wypisywanie wszystkich kluczy
#echo "${!users[@]}"

#echo "#####################"

#for klucz in "${!users[@]}"; do
#  wartosc=$(echo "${users[$klucz]}") # Alternatywny sposób odzyskiwania wartości
#  echo "Klucz: $klucz, Wartosc: $wartosc"
#done

dodaj_usera() {

for klucz in "${!users[@]}"; do
wartosc=$(echo "${users[$klucz]}") # Alternatywny sposób odzyskiwania wartości
# create user add ssh keys and sudo
useradd -m -d /home/$klucz -s /bin/bash $klucz
cd /home/$klucz && mkdir .ssh && chown  $klucz:$klucz .ssh && chmod 700 .ssh
cd /home/$klucz/.ssh && touch authorized_keys
cat << EOF | sudo tee /home/$klucz/.ssh/authorized_keys
$wartosc
EOF
cd /home/$klucz/.ssh  && chown $klucz:$klucz authorized_keys && chmod 600 authorized_keys
sudo usermod -aG sudo $klucz

cat << EOF | sudo tee -a /etc/sudoers.d/90-cloud-init-users
$klucz ALL=(ALL) NOPASSWD:ALL
EOF
done
}

dodaj_usera

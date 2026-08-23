#!/bin/bash

# Last Update: 3-Feb-2021
# Usar este script en servera como root
# Dar permiso de ejecución a este file.

hosto=$(hostname | cut -d '.' -f1)
if [ $hosto != 'servera' ];then
    echo -en "\n\tERROR: El script debe ejecutarse en servera\n\n"
    exit 1
fi

if [ -d /documentos ];then
    echo en "\n\tERROR: El script ya se habia ejecutado\n\n"
    exit 2
fi

echo -en "\n\tPreparando servera para los ejercicios de NFS...\n"

mkdir /documentos
mkdir -p /content/{Virtualizacion,Sistema,SELinux}

echo "Enhorabuena, has conseguido acceder al servidor de NFS en servera" > /documentos/info.txt

touch /content/Virtualizacion/RHV.pdf
touch /content/Sistema/{RHEL8-boot,RHEL8-Users}.pdf
touch /content/SELinux/SELinux-Basics.pdf

echo "/documentos  	172.25.250.0/24(rw,sync)" >> /etc/exports

echo "/content 172.25.250.0/24(rw,sync)" >> /etc/exports

systemctl start nfs-server && systemctl enable nfs-server
systemctl restart nfs-server
exportfs
firewall-cmd --permanent --add-service nfs && firewall-cmd --reload

echo -en "\tPreparacion terminada\n"
exit

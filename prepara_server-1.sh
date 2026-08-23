#!/bin/bash

# Last Update: 30-Dic-2020
# Usar este script en servera como root
# Dar permiso de ejecución a este file.

hosto=$(hostname | cut -d '.' -f1)
if [ $hosto != 'servera' ];then
    echo -en "\n\tERROR: El script debe ejecutarse en servera\n\n"
    exit 1
fi

if [ -d /marketing ];then
    echo en "\n\tERROR: El script ya se habia ejecutado\n\n"
    exit 2
fi

echo -en "\n\tPreparando servera para los ejercicios de NFS...\n"
mkdir -p /marketing/{folletos,videos}
mkdir /docs
echo "esto es una prueba de fichero exportado por NFS" > /docs/doc1.txt
echo "/docs  	172.25.250.0/24(rw,sync)" >> /etc/exports
echo "/marketing   172.25.250.0/24(ro,sync)" >> /etc/exports
touch /marketing/videos/presentacion{1,2}.avi
touch /marketing/folletos/producto{1,2}.ppt
systemctl start nfs-server && systemctl enable nfs-server
exportfs
firewall-cmd --permanent --add-service nfs && firewall-cmd --reload

echo -en "\tPreparacion terminada\n"
exit

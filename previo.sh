#/bin/bash
# Script de configuracion de simulacro de examen 1
# Last Update: 14-Octubre-2026

# El script se debe ejecutar en server0 como root

if [[ $(hostname) != "server0" ]];then
    echo "ERROR: Este script debe ejecutarse en server0"
    exit 1
fi
if [[ $(id -u) != '0' ]]; then
   echo "ERROR: Este script debe ejecutarse como root"
   exit 2
fi 
  
# Configurar repositorio DNF
echo "Configurando repositorio DNF"
cat > /etc/yum.repos.d/control.repo << EOF
[rhel10-BaseOS]
name = RHEL 10 BaseOS
baseurl = http://control.example.com/pub/rhel10/repo/BaseOS
gpgcheck = 0
enabled = 1
[rhel10-AppStream]
name = RHEL 10 AppStream
baseurl = http://control.example.com/pub/rhel10/repo/AppStream
gpgcheck = 0
enabled = 1
EOF
dnf makecache &> /dev/null

# Desplegar un servidor NFS
echo "Desplegando servidor NFS"
dnf install nfs-utils -y &> /dev/null
mkdir -p /exports/{pepe,nfsshare}
chown 2233 /exports/pepe; chmod 700 /exports/pepe
echo '/exports/pepe *(rw,sync,no_root_squash)' >> /etc/exports
echo '/exports/nfsshare *(rw,sync,no_root_squash)' >> /etc/exports
systemctl enable --now nfs-server &> /dev/null
firewall-cmd --add-service=nfs --permanent &> /dev/null && firewall-cmd --reload &> /dev/null
	
# Desplegar un servidor Apache en puerto 8234 sin arrancarlo

echo "Desplegando Apache web server"
dnf install httpd -y &> /dev/null
sed -i.bak 's|DocumentRoot "/var/www/html"|DocumentRoot "/html"|' /etc/httpd/conf/httpd.conf
sed -i 's/Listen 80/Listen 8234/' /etc/httpd/conf/httpd.conf	
echo -e "<Directory \"/html\">\n  Require all granted\n</Directory>" >> /etc/httpd/conf/httpd.conf	
mkdir /html
echo "Bienvenido a server0" > /html/index.html

exit

  

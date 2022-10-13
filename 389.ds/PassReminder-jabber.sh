#!/bin/bash
#
###########################################################################################################
#													  #
# 	 ____               ____                _           _           				  #	
# 	|  _ \ __ _ ___ ___|  _ \ ___ _ __ ___ (_)_ __   __| | ___ _ __ 				  #
# 	| |_) / _` / __/ __| |_) / _ \ '_ ` _ \| | '_ \ / _` |/ _ \ '__|				  #
# 	|  __/ (_| \__ \__ \  _ <  __/ | | | | | | | | | (_| |  __/ |   				  #
# 	|_|   \__,_|___/___/_| \_\___|_| |_| |_|_|_| |_|\__,_|\___|_|                                     #
#                                                                                                         #
#                         _       _     _                                                                 #
#                        | | __ _| |__ | |__   ___ _ __                                                   #
#                     _  | |/ _` | '_ \| '_ \ / _ \ '__|                                                  #
#                    | |_| | (_| | |_) | |_) |  __/ |                                                     #
#                     \___/ \__,_|_.__/|_.__/ \___|_|                                                     #
#                                                                                                         #
#                                                                                                         #
#  				                                                                          #
#													  #
#													  #
# Este script permite enviar un mensaje vía jabber a los usuarios de un LDAP o un FDS		          #
# ( Fedora Directory Server ) una advertencia para que cambien su contraseña, antes de que	          #
# expire su cuenta.											  #	
#													  #	
# Desarrollado por: Edwind Richzendy Contreras Soto							  #						
#		    richzendy@gmail.com									  #
#		    http://www.Richzendy.org								  #
#													  #
#			Agradecimientos a:								  #
#													  #
#	SAIME - http://www.saime.gob.ve									  #
#													  #
# Este programa es protegido por GNU/GPl, si no sabe lo que es, obtenga una copia en castellano en:       #
#													  #	
# http://www.es.gnu.org/modules/content/print.php?id=8							  #	
#													  #
# Por favor distribuya este programa a quien sea por el medio que sea... HAGALO!			  #	
# Por favor modifique este programa y comparta las modificaciones.					  #
# Use este programa como le de la gana.									  #	
# 													  #	
###########################################################################################################


# Your host or ip for LDAP o Fedora Directory Server (FDS)
LDAP_HOST="ldap.example.com"

# What is you LDAP o FDS port?
PORT="389"

# Your base dn search in LDAP o FDS server
BASEDN="dc=example,dc=gob,dc=ve"


# xsend script path
XSEND=/home/operador/bin/xsend.py

# Haga chequeos de passwords a vecer desde hoy hasta dentro de 5 dias
for n in {0..5}; do

FECHA=`date +%F --date "$n day" | sed 's/-//g'`

# Busque en el directorio a los usuarios afectados

BUSQUEDA=`ldapsearch -H ldap://$LDAP_HOST:$PORT -x -b $BASEDN "(passwordexpirationtime=$FECHA*)" mail  | grep @ | cut -d " " -f 2`

# Reviso que la cadena de busqueda no este vacia.

VALOR_DE_COMPROBACION=`echo $BUSQUEDA | cut -f 1 -d "@"`

if [ -z  $VALOR_DE_COMPROBACION ] ; then
echo "0" > /dev/null
else

# Si hoy se te vence la password te voy a mandar un mail personalizado bien alarmante :D

if [ $n == 0 ] ; then
echo "0" > /dev/null

for i in $BUSQUEDA ; do
ADDRESS=`echo $i | cut -f 2 -d "@"`

# Compruebo que la cuenta de correo tenga el dominio, saime.gob.ve, actualmente donde esta alojado el script no me permite enviar correo a otros dominios.

if [ $ADDRESS != saime.gob.ve ] ; then
echo "0" > /dev/null
else

echo ""
echo "enviando ultimatum a: $i"
        $XSEND $i  Hasta HOY tiene oportunidad de cambiar su clave, Hagalo desde https://192.168.0.4/cgi-bin/changepass.pl 
fi
done

else

# Enviar mail aca de advertencia a los demás, con dias de vencimiento a partir de hoy.

for i in $BUSQUEDA ; do

ADDRESS=`echo $i |cut -f 2 -d "@"`

if [ $ADDRESS != saime.gob.ve ] ; then
echo "0" > /dev/null
else

echo ""
echo "enviando notificación a: $i | le quedan $n dias"
        $XSEND $i  Su password se vencerá en $n dias, Puede cambiarla desde la dirección: https://192.168.0.4/cgi-bin/changepass.pl
fi
done
fi
fi
done

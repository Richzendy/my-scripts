#!/bin/bash
#
#													  #	
# Desarrollado por: Edwind Richzendy Contreras Soto							  #
#						                                                          #
#		    richzendy@gmail.com									  #
#		    http://www.Richzendy.org								  #
#													  #
#			Agradecimientos a:								  #
#													  #
#	        SAIME - http://www.saime.gob.ve								  #
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
LDAP_HOST="ldap1.example.com"

# What is you LDAP o FDS port?
PORT="389"

# Your base dn search in LDAP o FDS server
BASEDN="dc=example,dc=com"

# Admin ldap
LDAPADMINPASSWD="yourpasswd"
DNENTRYLDAPADMIN="uid=ldapadmin,ou=especial users,dc=example,dc=com"

echo "Content-type: text/html; charset=UTF-8"
echo ""


# Función que define el formulario usado

header () {
cat <<EOE 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <meta name="description" content="Intranet" />
        <meta name="keywords" content="" />

        <title>Intranet</title>
        <link rel="stylesheet" href="http://intranet.example.com/style.css" media="screen" />
</head>
<body>
        <div id="container">
                <div id="header">
<table width="760" height="46" border="0" cellpadding="0" cellspacing="0">

      <tr>
        <td width="30px" height="46"><img src="http://intranet.example.com/images/log.jpg" alt=""/></td>
        <td width="167px" height="46" style="color:#777;font-size:14px" valign="bottom">
        <div style="padding:5px">
        <b>Gobierno <span style="color:#000">Bolivariano</span> <br/>
        de Venezuela</b>
        <div>

        </td>
        <td width="2px" height="46" valign="bottom">
        <img src="images/spacer.jpg" alt=""/>
        </td>
        <td width="280" height="46" style="color:#777;font-size:12px" valign="bottom">
        <div style="padding:5px">
        <b>Ministerio del Poder Popular<br/>
        para <span style="color:#000">Relaciones Interiores y Justicia</span></b>

        </div>
        </td>
        <td ><div align="right"><img src="http://intranet.example.com/images/detodos.gif" alt="" width="75" height="45" /></div></td>
        </tr>
    </table>

                </div>
                <div id="content">
                        <h2>Página de Intranet</h2>
<br>
<H3 align="center">Cambio de clave para el usuario: <b>$USER</b></H3>
<hr> 
<br>
<br>
EOE
}

formulario () {
cat <<EOF

<p>
 Coloque su contraseña actual, la nueva contraseña y haga clic en el botón &#8220;Cambiar Contraseña&#8221;.
 </p>
<form method="post" action="https://intranet.example.com/cgi-bin/changepass.cgi?login=$USER" enctype="application/x-www-form-urlencoded">
 <input type="hidden" name="login" value=$USER  maxlength="25" />
<table border=0 cellspacing=0 cellpadding=0 margin-left:46.0pt' summary='Cambiar contraseña' >
 <tr style='mso-yfti-irow:0'>
 <tr >
 <td style='padding:.75pt .75pt .75pt .75pt'>Contraseña Actual:</td>
 <td style='padding:.75pt .75pt .75pt .75pt'><input type="password" name="oldpass"  maxlength="25" /></td>
 </tr>
 <tr >
 <td style='padding:.75pt .75pt .75pt .75pt'>Nueva Contraseña</td>

 <td style='padding:.75pt .75pt .75pt .75pt'><input type="password" name="newpass"  maxlength="25" /></td>
 </tr>
 <tr >
 <td style='padding:.75pt .75pt .75pt .75pt'>Repetir Contraseña</td>
 <td style='padding:.75pt .75pt .75pt .75pt'><input type="password" name="newpass2"  maxlength="25" /></td>
 </tr>
 <tr >
 <td style='padding:.75pt .75pt .75pt .75pt'>

 <p></p>
 </td>
 <td style='padding:.75pt .75pt .75pt .75pt'><input type="submit" name="Cambiar contraseña" value="Cambiar contraseña" /></td>
 </tr>
 </table>
 <br>
<br>
<p>
 <b>Su contraseña debe ser segura y cumplir con ciertos requisitos:</b> 
</p> 
 - Debe cambiarla cada 60 dias.            
 <br><br>
 - Si ud. ha realizado un cambio de contraseña recientemente o le fue reseteada su password, deber&aacute; esperar 24 horas para realizar un cambio de clave.
 <br><br>
 - Si ud. está intentando ingresar a internet/correo o algún otro servicio luego de cambiar la contraseña, debe esperar aproximadamente 2 minutos para que se actualice.
 <br><br>
 - Una contraseña segura contiene: 
 <ol start=1 type=1>
 <li>
  Una longitud mínima de 7 caracteres.
 </li>
 <li>
   Palabras NO comunes y/o sistem&aacute;ticas.
 </li>

 <li>
   Una combinación de letras, números o uno de los siguientes caracteres: 
 </li>
 </ol>

 <div id=pre><span>!@#^&amp;*()_+=|~{[}].</span></div>
<br>
<p>
 <b>Obtenga ayuda a través de:</b>
</p>
 Soporte
 <br>
 Tlf: (0212)243245365
 <br>

 email: <a href='mailto:soporte@example.com'>soporte@example.com</a>
 <br>

EOF
}

# Capturar Variables usadas del formulario


read -n $CONTENT_LENGTH QUERY_STRING_POST
USER=`echo "$QUERY_STRING" | grep -oE "(^|[?&])login=[a-z]+" | cut -f 2 -d "=" | head -n1`
CLAVE_ACTUAL=`echo "$QUERY_STRING_POST" | grep -oE "(^|[?&])oldpass=[A-Za-z0-9%*_.]+" | cut -f 2 -d "=" | head -n1 | sed -e 's/%21/!/g' -e 's/%40/@/g' -e  's/%23/#/g' -e 's/%5E/^/g' -e  's/%26/\&/g' -e  's/%28/(/g' -e  's/%29/)/g' -e  's/%2B/+/g' -e  's/%3D/=/g' -e  's/%7C/|/g' -e  's/%7E/~/g' -e 's/%7B/{/g' -e 's/%7D/}/g' -e 's/%5B/[/g' -e 's/%5D/]/g'`
CLAVE_NUEVA=`echo "$QUERY_STRING_POST" | grep -oE "(^|[?&])newpass=[A-Za-z0-9%*_.]+" | cut -f 2 -d "=" | head -n1 | sed -e 's/%21/!/g' -e 's/%40/@/g' -e  's/%23/#/g' -e 's/%5E/^/g' -e  's/%26/\&/g' -e  's/%28/(/g' -e  's/%29/)/g' -e  's/%2B/+/g' -e  's/%3D/=/g' -e  's/%7C/|/g' -e  's/%7E/~/g' -e 's/%7B/{/g' -e 's/%7D/}/g' -e 's/%5B/[/g' -e 's/%5D/]/g'`
CLAVE_NUEVA_REP=`echo "$QUERY_STRING_POST" | grep -oE "(^|[?&])newpass2=[A-Za-z0-9%*_.]+" | cut -f 2 -d "=" | head -n1 | sed -e 's/%21/!/g' -e 's/%40/@/g' -e  's/%23/#/g' -e 's/%5E/^/g' -e  's/%26/\&/g' -e  's/%28/(/g' -e  's/%29/)/g' -e  's/%2B/+/g' -e  's/%3D/=/g' -e  's/%7C/|/g' -e  's/%7E/~/g' -e 's/%7B/{/g' -e 's/%7D/}/g' -e 's/%5B/[/g' -e 's/%5D/]/g'`

# Tabla de reemplazos
#%21=!
#%40=@
#%23=#
#%5E=^
#%26=&
#%28=(
#%29=)
#%2B=+
#%3D==
#%7C=|
#%7E=~
#%7B={
#%7D=}
#%5B=[
#%5D=]


if [ -z $USER ] && [ -z $CLAVE_ACTUAL ] && [ -z $CLAVE_NUEVA ] && [ -z $CLAVE_NUEVA_REP ] ; then

header

echo "<div id=error>Este script no puede ser accedido directamente, Ud. debe verificar el estado de su cuenta <a href="http://intranet.example.com/cgi-bin/fechaexp.cgi">primero</a>.</div>"

else

if [ -n $USER ] && [ -z $CLAVE_ACTUAL ] && [ -z $CLAVE_NUEVA ] && [ -z $CLAVE_NUEVA_REP ] ; then

header
formulario

else

HEIGHT=`echo $CLAVE_ACTUAL |wc -c`
if [ $HEIGHT -eq 0 ] || [ $HEIGHT -le 7 ] ; then

header

echo "<div id=error><b>ERROR: la 'Contraseña Actual' no puede ser menor de 7 caracteres.</b></div>"

formulario

else

HEIGHT1=`echo $CLAVE_NUEVA |wc -c`

if [ $HEIGHT1 -eq 0 ] || [ $HEIGHT1 -le 7 ] ; then

header
 
echo "<div id=error><b>ERROR: la 'Nueva Contraseña' no debe ser menor a 7 caracteres.</b></div>"

formulario

else

if [ $CLAVE_NUEVA != "$CLAVE_NUEVA_REP" ] ; then

header

echo "<div id=error><b> ERROR: la 'Nueva Contraseña' y su comprobación no son iguales, por favor verifique.</b> </div>"

formulario

else

CADENA=`ldapsearch -H ldap://$LDAP_HOST:$PORT -x -b $BASEDN "(uid=$USER)" passwordexpirationtime | grep passwordexpirationtime: | sed 's/passwordexpirationtime://;s/\ //' | cut -c 1-8`

YEAR=`echo $CADENA | cut -c 1-4`
MES=`echo $CADENA | cut -c 5-6`
DIA=`echo $CADENA | cut -c 7-8`

FECHA_ACTUAL=`date +'%Y-%m-%d'`
FECHA_ACTUAL_UNIX=`date --date="$FECHA_ACTUAL" +%s`
FECHA_EXP_UNIX=`date --date="$YEAR-$MES-$DIA" +%s`
DIFERENCIA_FECHAS=`echo $[$FECHA_ACTUAL_UNIX - $FECHA_EXP_UNIX ]`
DIAS_DIFERENCIA=`date -d @$DIFERENCIA_FECHAS +"%d"`

if [ "$FECHA_EXP_UNIX" -lt $FECHA_ACTUAL_UNIX ]  ; then

DATE=`date +%F --date "1 day" | sed 's/-//g'`

echo "dn: uid=$USER,ou=People,dc=example,dc=com
changetype: modify
replace: passwordexpirationtime
passwordexpirationtime: $DATE" > /tmp/exp.$$

ldapmodify -xD "$DNENTRYLDAPADMIN" -w $LDAPADMINPASSWD -H ldap://$LDAP_HOST -f /tmp/exp.$$ 2> /tmp/exp.log

rm /tmp/exp.$$


header
echo "dn: uid=$USER,ou=People,dc=example,dc=com
changetype: modify
replace: UserPassword
UserPassword: $CLAVE_NUEVA" > /tmp/ldif.$$

ldapmodify -xD "uid=$USER,ou=People,dc=example,dc=com" -w "$CLAVE_ACTUAL" -H ldap://$LDAP_HOST -f /tmp/ldif.$$ 2> /tmp/changepass.log
rm /tmp/ldif.$$

if [ -z `cat /tmp/changepass.log` ] ; then

echo "<div id=pre>Su Clave fue cambiada adecuadamente,<b> por seguridad trate de memorizarla, nunca anote ni comparta su clave.</b></div>"

echo "" > /tmp/changepass.log
else

# Acomodar mensajes de respuesta
INV="ldap_bind: Invalid credentials"
INV_ES="ERROR: Credenciales Inválidas, su Clave Actual no concuerda con la que realmente debería ser."
EDAD="within password minimum age"
EDAD_ES="ERROR: Ud. ha cambiado su password recientemente, debe esperar al menos 24 horas luego del cambio para poder volver a cambiarla."
HISTORIAL="password in history"
HISTORIAL_ES="ERROR: Ud. está usando como Nueva Clave una clave muy parecida o igual a alguna usada las últimas 5 veces que ha cambiado la password, debe colocar una Nueva Clave que no tenga relación con las 5 últimas usadas. (19)"
RETRY="Exceed password retry limit. Please try later"
RETRY_ES="Ud. se ha equivocado numerosas veces al intentar hacer login y su cuenta se ha bloqueado aproximadamente 10 minutos, por favor intente más tarde"
SINTAX="invalid password syntax"
SINTAX_ES="ERROR: Su clave es demasiado simple, debe contener letras mayúsculas o minúsculas y además números."

RESPUESTA=`echo $(cat /tmp/changepass.log) | sed -e "s/$INV/$INV_ES/g" -e "s/$EDAD/$EDAD_ES/g" -e "s/$HISTORIAL/$HISTORIAL_ES/g" -e "s/$RETRY/$RETRY_ES/g" -e "s/$SINTAX/$SINTAX_ES/g"`

echo "<div id=error>$RESPUESTA</div>"

echo "" > /tmp/changepass.log

formulario

fi



else



header
echo "dn: uid=$USER,ou=People,dc=example,dc=com
changetype: modify
replace: UserPassword
UserPassword: $CLAVE_NUEVA" > /tmp/ldif.$$

ldapmodify -xD "uid=$USER,ou=People,dc=example,dc=com" -w "$CLAVE_ACTUAL" -H ldap://$LDAP_HOST -f /tmp/ldif.$$ 2> /tmp/changepass.log
rm /tmp/ldif.$$

if [ -z `cat /tmp/changepass.log` ] ; then 

echo "<div id=pre>Su Clave fue cambiada adecuadamente,<b> por seguridad trate de memorizarla, nunca anote ni comparta su clave.</b></div>"

echo "" > /tmp/changepass.log
else

# Acomodar mensajes de respuesta
INV="ldap_bind: Invalid credentials"
INV_ES="ERROR: Credenciales Inválidas, su Clave Actual no concuerda con la que realmente debería ser."
EDAD="within password minimum age"
EDAD_ES="ERROR: Ud. ha cambiado su password recientemente, debe esperar al menos 24 horas luego del cambio para poder volver a cambiarla."
HISTORIAL="password in history"
HISTORIAL_ES="ERROR: Ud. está usando como Nueva Clave una clave muy parecida o igual a alguna usada las últimas 5 veces que ha cambiado la password, debe colocar una Nueva Clave que no tenga relación con las 5 últimas usadas."
RETRY="Exceed password retry limit. Please try later"
RETRY_ES="Ud. se ha equivocado numerosas veces al intentar hacer login y su cuenta se ha bloqueado aproximadamente 10 minutos, por favor intente más tarde"
SINTAX="invalid password syntax"
SINTAX_ES="ERROR: Su clave es demasiado simple, debe contener letras mayúsculas o minúsculas y además números."

RESPUESTA=`echo $(cat /tmp/changepass.log) | sed -e "s/$INV/$INV_ES/g" -e "s/$EDAD/$EDAD_ES/g" -e "s/$HISTORIAL/$HISTORIAL_ES/g" -e "s/$RETRY/$RETRY_ES/g" -e "s/$SINTAX/$SINTAX_ES/g"`

echo "<div id=error>$RESPUESTA</div>"

echo "" > /tmp/changepass.log

formulario

fi
fi
fi
fi
fi
fi
fi

cat <<EOE
 </div>
                <div id="sidebar">
                        <ul>
                                <li><a href="http://intranet.example.com">Inicio</a></li>
                                <li><a target="_blank" href="http://correo.example.com">Correo</a></li>
                                <li><a target="_blank" href="https://ns2.example.com:26266/clients/dsgw/bin/lang?context=pb">Directorio</a></li>
                        </ul>

                        <div class="widget">
<img src=http://intranet.example.com/images/logo.png>
                        </div>

                </div>
                <div id="footer">Copyleft @ Derechos cedidos| Sitio web desarrollado por <a target="_blank" href="http://www.Richzendy.org">Richzendy</a> </div>
        </div>
</body>
</html>
EOE


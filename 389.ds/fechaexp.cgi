#!/bin/bash
echo "Content-type: text/html; charset=UTF-8"
echo ""

formulario () {

echo "<HTML>"
echo "<HEAD><TITLE>SAIME - LDAP Tools - Fecha de Expiración de Cuentas</TITLE></HEAD>"
echo "<BODY bgcolor="#cccccc" text="#000000">"
echo "<H2>Herramienta de búsqueda de fechas de expiración de cuentas en el LDAP</H2>"
echo "<hr>"
echo "<form enctype="text/plain" method="get" action="fechaexp.cgi"  name="Busquedas de cuentas expiradas">"
echo "Introduce Nombre de usuario o login: &nbsp; &nbsp; "
echo "<input maxlength="15" size="15"  name="login">"
echo "<input name="enviar" type="submit" value"enviar"></input><br>"
echo "</form>"
echo "<hr>"
"</BODY>"
"</HTML>"
}

# Variables usadas 


USER=`echo "$QUERY_STRING" | grep -oE "(^|[?&])login=[a-z]+" | cut -f 2 -d "=" | head -n1`

if [ -z $QUERY_STRING ]; then

formulario

else 

CADENA=`ldapsearch -H ldap://ns1.saime.gob.ve:389 -x -b "dc=saime,dc=gob,dc=ve" "(uid=$USER)" passwordexpirationtime | grep passwordexpirationtime: | sed 's/passwordexpirationtime://;s/\ //' | cut -c 1-8`

if [ -z $CADENA ] ; then

formulario
echo "Nombre de usuario no existe en el Directorio, por favor verifique."

else

formulario


# Variables para el tratamiento de las fechas

YEAR=`echo $CADENA | cut -c 1-4`
MES=`echo $CADENA | cut -c 5-6`
DIA=`echo $CADENA | cut -c 7-8`
FECHA_ACTUAL=`date +'%Y-%m-%d'`
FECHA_ACTUAL_UNIX=`date --date="$FECHA_ACTUAL" +%s`
FECHA_EXP_UNIX=`date --date="$YEAR-$MES-$DIA" +%s`
DIFERENCIA_FECHAS=`echo $[$FECHA_ACTUAL_UNIX - $FECHA_EXP_UNIX ]`
DIAS_DIFERENCIA=`date -d @$DIFERENCIA_FECHAS +"%d"`

echo "La Fecha de Expiración es: $DIA-$MES-$YEAR / (dia-mes-año)"
echo "<br><br>"

if [ "$FECHA_EXP_UNIX" -lt $FECHA_ACTUAL_UNIX ] ; then

echo "Su cuenta se vencio hace $DIAS_DIFERENCIA dia(s), debe abrir un ticket de soporte, desde la aplicación Service Desk<br>"
echo "como usuario invitado, solicitando la aplicación del tiempo de expiración, desde la siguiente dirección:<br><br>"
echo "<a href="https://soporte.saime.gob.ve">https://soporte.saime.gob.ve</a>"
echo "<br>"
echo "<br>"
echo "O si lo prefiere puede llamar directamente por los teléfonos 0-800-STSAIME ( 08002782463 ), en donde<br>"
echo "uno de nuestros operadores lo atenderan.<br><br>"

echo "Una vez que el problema sea resuelto, tendrá 2 dias para cambiar su password, con lo cual gozará de 60 días<br>"
echo "de vigencia en su cuenta. Se le recuerda que debe revisar su cuenta de correo eléctronico con frecuencia, ya <br>"
echo "que allí fue notificado de que su cuenta estaba a punto de expirar con anterioridad." 

else 

DIFERENCIA_FECHAS=`echo $[$FECHA_EXP_UNIX - $FECHA_ACTUAL_UNIX ]`
DIAS_DIFERENCIA=`date -d @$DIFERENCIA_FECHAS +"%d"`

echo "Y le quedan $DIAS_DIFERENCIA dia(s) para que expire su cuenta de usuario<br>"
echo "Si lo desea, puede cambiar su contraseña pulsando <a href="https://monitoreo.saime.gob.ve/cgi-bin/changepass.pl">aquí</a>"

fi
fi
fi


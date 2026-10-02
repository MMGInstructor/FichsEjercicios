#!/usr/bin/perl -w

# Definición del programa para enviar correo, debe dejarse sin cambios.
$progmail = '/usr/bin/mailx';

# Usuario al que se enviarán los mensajes. Deberá poner su alias de correo electrónico.
$destino = 'mmartinez@edustance.com';

# Indica que se trata de un documento HTML
print "Content-type: text/html\n\n";

# Obtiene la entrada
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

# Divide las variables entre nombre y valor.
@pairs = split(/&/, $buffer);

# Optiene todas las variables y sus valores
foreach $pair (@pairs)
{
($name, $value) = split(/=/, $pair);

$value =~ tr/+/ /;
$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$FORM{$name} = $value;
}

# Imprime el título y la cabecera
print "<html><Head><Title>Gracias</Title></Head><Body>";

# Si la respuesta es vacia, se llama a una función que la trata 
&blank_response unless $FORM{'comentar'};


print "<H1>Muchas Gracias, sus comentarios son bienvenidos</H1>";

# Imprime el texto del texto a mostar.
print "Gracias por enviar sus comentarios a <I>mmartinez\@edustance.com</I><P></BODY></HTML>";

# Ahora enviamos el mail al $destino
open (SALIDA, "|$progmail $destino") || die "No puedo abrir $progmail!\n";
print SALIDA "Reply-to: $FORM{'email'} ($FORM{'nombre'} $FORM{'apellido'})\n";
print SALIDA "Subject: Comentarios al formulario de prueba ($FORM{'nombre'} $FORM{'apellido'})\n\n";
print SALIDA "$FORM{'nombre'} $FORM{'apellido'} del curso $FORM{'curso'}envio \n";
print SALIDA "El siguiente comentario::\n\n";
print SALIDA "------------------------------------------------------------\n";
print SALIDA "$FORM{'comentar'}";
print SALIDA "\n------------------------------------------------------------\n";
close (SALIDA);

# ------------------------------------------------------------
# subrutina blank_response para comentarios en blanco
sub blank_response
{
print "Sus comentarios estan en blanco, de manera que no seran";
print " enviados a mmartinez\@edustance.com. Por favor vuelva a introducirlos.</BODY></html>";
exit;
}

# Ahora enviamos la salida al fichero: /var/www/cgi-bin/respuestas.htm
open (SALIDA, ">> /var/www/cgi-bin/respuestas.htm") || die "No puedo abrir el fichero!\n";
print SALIDA "=======================\n";
print SALIDA "$FORM{'nombre'} $FORM{'apellido'} ($FORM{'email'}) \n del curso $FORM{'curso'} puso el comentario\n";
print SALIDA "------------------------------------------------------------\n";
print SALIDA "$FORM{'comentar'}";
print SALIDA "\n------------------------------------------------------------\n\n";
close (SALIDA);
exit;


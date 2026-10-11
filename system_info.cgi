#!/bin/bash

# Generar la cabecera HTTP obligatoria para scripts CGI
echo "Content-Type: text/html; charset=utf-8"
echo ""

# Obtener datos del sistema mediante comandos de Linux
HOSTNAME=$(hostname)
IPS=$(ip -4 addr show | grep -oP '(?<=inet\s)\d+(\.\d+){3}' | grep -v '127.0.0.1')

# Generar el HTML
cat <<EOF
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Información del Servidor Apache</title>
    <style>
        body {
            font-family: system-ui, -apple-system, sans-serif;
            background-color: #f4f6f8;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            max-width: 450px;
            width: 100%;
        }
        h1 {
            color: #cc0000;
            font-size: 1.4rem;
            margin-top: 0;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
        ul { list-style: none; padding: 0; }
        li { padding: 8px 0; border-bottom: 1px solid #f0f0f0; }
        .label { font-weight: bold; }
        code {
            background-color: #eef2f7;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            color: #d63384;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Servidor Apache</h1>
        <ul>
            <li><span class="label">Hostname:</span> <code>$HOSTNAME</code></li>
            <li>
                <span class="label">Direcciones IP IPv4:</span>
                <ul>
EOF

# Iterar sobre las IPs encontradas
for ip in $IPS; do
    echo "                    <li><code>$ip</code></li>"
done

cat <<EOF
                </ul>
            </li>
        </ul>
    </div>
</body>
</html>
EOF


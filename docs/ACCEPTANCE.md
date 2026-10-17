# Pruebas pendientes en servidor
- docker compose config --quiet; no imprimir .env/hash en canales públicos.
- Arranque nuevo crea datastore vacío, pausado y silenciado; guarda API key y settings.
- Login exige contraseña; API sin x-api-key devuelve rechazo.
- Probar URLs internas/file:// rechazadas; no ampliar permisos globales.
- Ejecutar dos revisiones de página propia y comprobar diferencia/historial.
- Reiniciar conserva watches/configuración/snapshots.
- Backup/restauración a volumen nuevo con red aislada, sin envío de notificaciones.
- Revisar consumo, intervalo mínimo1h, máximo50 watches, errores y retención.
- Probar notificación solo cuando exista destinatario/canal autorizado.

Local: Python/YAML, hash PBKDF2 nativo, .env0600/no sobrescritura y ZIP. No se ejecutó app real, API ni store interno contra imagen.

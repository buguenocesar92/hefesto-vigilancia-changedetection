# Restauración y traslado
1. Destino con misma imagen0.60.9 y VOLUME_PREFIX nuevo; no iniciar app sobre volumen vacío antes de restaurar. Mantener origen intacto.
2. Recuperar .env y ops de backup confiable, verificar hashes de configuración. Conservar SALTED_PASS si mantiene contraseña, actualizar dominio según destino.
3. `python3 scripts/restore.py /ruta/respaldo`. Exige volumen vacío, app detenida, hash y rutas válidos; restaura con propietario root como imagen oficial. No sobrescribe.
4. Ensayo: `docker compose -f compose.yaml -f compose.bootstrap.yaml -f compose.rehearsal.yaml up -d`. Red interna bloquea Internet. No conectar proxy/servicios con salida a esa red. Watches restaurados pueden intentar ejecutar y fallar: entrar y pausar todos antes de retirar aislamiento. Notificaciones recuperadas también podrían reactivarse al recuperar conectividad.
5. Revisar contraseña, watches, filtros, snapshots/historial y configuración. No activar avisos en el ensayo.
6. Corte final: pausar origen, backup definitivo, restaurar limpio, configurar proxy/DNS y reactivar solo revisiones aceptadas. No dejar ambas copias activas para evitar doble consulta/notificación.

Un fallo parcial exige destino nuevo. Hash detecta corrupción, no autentica origen desconocido. No restaurar un backup de otra versión encima de un datastore existente. Plan de actualización: copia aislada, lectura de cambios upstream, verificación y rollback por backup íntegro.

Odoo/n8n: integración futura mediante API/webhooks/avisos, sin módulo instalado en este kit. Mantener API key exclusivamente en backend, no en enlaces públicos. Validar esquema y deduplicar eventos por watch/cambio antes de crear tareas o actividades. La API de esta instancia no es un sistema multitenant con scopes por cliente.

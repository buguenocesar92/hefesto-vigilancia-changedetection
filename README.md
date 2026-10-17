# Hefesto Vigilancia · changedetection.io 0.60.9

Detección de cambios en páginas web para revisar catálogos, documentación y avisos públicos. Kit Docker/Coolify con contraseña de acceso, almacenamiento persistente, respaldos y restauración. Sin instancia desplegada ni notificaciones enviadas.

## Stack y límites
Producto nativo Python + archivos en /datastore. No requiere Supabase: no usa PostgreSQL como backend intercambiable. El volumen contiene configuración, watches, historial, snapshots, API key y posibles credenciales configuradas posteriormente.

Se incluye backend HTTP requests para contenido servido en HTML. No se instala navegador remoto/Playwright: páginas que dependen de JavaScript, sesiones complejas o selectores visuales requieren ampliación y pruebas. No se incluyen evasión de bloqueos, CAPTCHA ni acceso a contenido privado.

Dos workers, máximo50 watches y mínimo1h entre revisiones, como límites iniciales de este kit. El intervalo por página puede ser mayor. No hay garantía de que todo cambio se detecte ni de disponibilidad inmediata; las páginas pueden alterar HTML, bloquear solicitudes o devolver contenido dinámico.

## Puesta en marcha
Requisitos: Docker/Compose v2, Python3.11+ para scripts y dominio/proxy HTTPS. Inicio orientativo1CPU/1GB; dimensionar historial y volumen según uso.

1. `python3 scripts/configure.py`: solicita contraseña dos veces sin mostrarla y crea .env0600 con SALTED_PASS (hash PBKDF2 nativo). No guarda contraseña plana. Editar PUBLIC_URL y VOLUME_PREFIX.
2. `docker compose -f compose.yaml -f compose.bootstrap.yaml up -d`. Abrir http://localhost:8108 o túnel `ssh -L 8108:127.0.0.1:8108 usuario@servidor`.
3. Entrar con contraseña definida; no hay usuario compartido preconfigurado. Nueva instancia arranca sin watches, globalmente pausada y silenciada. El inicializador usa el store de la versión fijada para evitar ejemplos upstream que se revisan automáticamente.
4. Revisar ajustes: API key requerida, no deshabilitar protección API; backend requests, notificaciones vacías. BASE_URL define enlaces de notificación, no obliga HTTPS ni decide exposición de red.
5. Añadir una página propia o autorizada, seleccionar texto/selector y revisar filtros con docs/PRIMERA-REVISION.md. Quitar pausa global solo cuando quiera empezar. Mantener silencio y no definir destinos de notificación hasta completar prueba.
6. `docker compose -f compose.yaml -f compose.bootstrap.yaml down` sin -v. Confirmar PUBLIC_URL HTTPS y `docker compose up -d`.
7. Coolify: importar compose.yaml con ops y variables. Asociar dominio HTTPS a app5000. No publicar override bootstrap. Proxy debe proteger conexión externa con TLS; sin puerto5000 directo.
8. Probar acceso sin sesión, API sin key, ejecución de revisión autorizada e historial después de reinicio.

La contraseña del entorno prevalece sobre configuración almacenada. Para cambiarla generar un nuevo hash con el mismo método conservando configuración; puede generar .env temporal en otra copia del kit, copiar solo SALTED_PASS y recrear app. No sobrescribir la instalación ni borrar la base para cambiar contraseña.

## Protección y datos
Se mantienen bloqueos nativos a URLs privadas/reservadas y file://. No activar ALLOW_IANA_RESTRICTED_ADDRESSES/ALLOW_FILE_URI globalmente. Si una revisión requiere intranet, diseñar despliegue/red de acceso específico. No instalar paquetes extra ni proporcionar claves IA para este kit.

Servicio de una instancia compartida: no ofrece aislamiento multicliente por usuario. Preferir una instancia por cliente. Hash de contraseña va en .env; API key, notificaciones y otras preferencias se guardan según diseño nativo en datastore. No se afirma que todos los secretos estén fuera de archivos de la app.

## Respaldos
`python3 scripts/backup.py` pausa app y workers, copia /datastore completo y configuración, genera hashes y reinicia si estaba activa. Usar compose base y finalizar ediciones antes de copiar. No copiar solo changedetection.json: los subdirectorios contienen historial y definiciones.

Cifrar respaldo y mantenerlo fuera del servidor. `python3 scripts/restore.py /ruta/respaldo` exige volumen vacío y valida hashes/rutas. Ver docs/RESTORE.md.

Estado: sintaxis/configuración y generación del hash comprobadas localmente. Falta ejecutar imagen, inicialización real del store, detección y restauración en servidor. No se ha consultado ninguna página como watch ni activado avisos.

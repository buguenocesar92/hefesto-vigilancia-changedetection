# Primera revisión controlada
1. En una página propia de ensayo publicar texto identificable, por ejemplo “Versión de prueba: A”.
2. Añadir URL HTTPS en interfaz, título “Prueba Hefesto”, backend requests y frecuencia de1h o superior. Evitar incluir cabeceras/tokens de servicios reales.
3. Desactivar pausa global cuando quiera ejecutar. Primera revisión establece referencia; revisar contenido extraído antes de asumir que es correcto.
4. Cambiar página de ensayo a “Versión de prueba: B”. Ejecutar una segunda revisión cuando el límite de frecuencia lo permita. Comprobar diferencia e historial.
5. Añadir filtro CSS/XPath adecuado a la página para evitar menús, timestamps y anuncios. Validar nuevamente después de cambiar filtros.
6. Notificaciones: permanecen vacías/silenciadas hasta elegir canal. Para probar, autorizar destinatario y configurar un solo canal; comprobar éxito y errores antes de ampliar. Nunca enviar contenido sensible de una página a un canal público.

El kit no levanta una web de prueba ni toca sitios externos. El archivo examples/pagina-demo.html es material que puede publicar en su propio entorno de ensayo; no se configura automáticamente como watch local porque las redes internas permanecen bloqueadas.

#!/usr/bin/env python3
import base64,getpass,hashlib,os,secrets
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def create_env(password,root=ROOT):
    if len(password)<14:raise ValueError('Usar al menos14 caracteres')
    salt=secrets.token_bytes(32)
    value=base64.b64encode(salt+hashlib.pbkdf2_hmac('sha256',password.encode(),salt,100000)).decode()
    s=(root/'.env.example').read_text().replace('GENERAR_CON_CONFIGURE',value)
    fd=os.open(root/'.env',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
    with os.fdopen(fd,'w') as f:f.write(s)
if __name__=='__main__':
    if (ROOT/'.env').exists():raise SystemExit('.env ya existe; no se sobrescribe')
    password=getpass.getpass('Contraseña de acceso (mínimo14 caracteres): ')
    if password!=getpass.getpass('Repetir contraseña: '):raise SystemExit('No coinciden')
    create_env(password)
    print('.env creado con hash nativo; no se guardó contraseña plana. Configurar dominio.')

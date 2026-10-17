#!/usr/bin/env python3
import base64,json,os,sys
from pathlib import Path
sys.path.insert(0, "/app")
try:
    if len(base64.b64decode(os.environ.get('SALTED_PASS',''),validate=True))!=64:raise ValueError()
except (ValueError,TypeError):raise SystemExit('Configurar SALTED_PASS válido con scripts/configure.py')
root=Path('/datastore');root.mkdir(exist_ok=True)
config=root/'changedetection.json'
if not config.exists():
    if any(root.iterdir()):raise SystemExit('Datastore con archivos pero sin changedetection.json: revisar migración, no inicializar encima')
    # Version-pinned initialization using the same store implementation as upstream.
    from changedetectionio import store, __version__
    ds=store.ChangeDetectionStore(datastore_path=str(root),version_tag=__version__,include_default_watches=False)
    ds.data['settings']['application']['all_paused']=True
    ds.data['settings']['application']['all_muted']=True
    ds._save_settings()
settings=json.loads(config.read_text())
# The main settings file contains the settings block; require explicit API protection.
if not settings.get('settings',{}).get('application',{}).get('api_access_token_enabled',False):
    raise SystemExit('Mantener api_access_token_enabled=true antes de iniciar')
os.execv(sys.executable,[sys.executable,'/app/changedetection.py','-d','/datastore'])

import hashlib
import hmac
import json
import urllib.request
from datetime import datetime, timezone

# Tus datos
payload = {
    "action_run_link": "PLACEHOLDER",
    "email": "martinbernardobonilla@gmail.com",
    "name": "Martín Bernardo Bonilla",
    "repository_link": "https://github.com/MartinBernardoBonilla/b12-application",
    "resume_link": "https://woodstack-portfolio.vercel.app",
    "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.") + 
                 f"{datetime.now(timezone.utc).microsecond // 1000:03d}Z"
}

# Convertir a JSON compacto con claves ordenadas
body = json.dumps(payload, separators=(',', ':'), sort_keys=True).encode('utf-8')

# Firmar con HMAC-SHA256
secret = b'hello-there-from-b12'
signature = hmac.new(secret, body, hashlib.sha256).hexdigest()

# Enviar el POST
req = urllib.request.Request(
    'https://b12.io/apply/submission',
    data=body,
    headers={
        'Content-Type': 'application/json',
        'X-Signature-256': f'sha256={signature}'
    },
    method='POST'
)

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read().decode('utf-8'))
    print("Receipt:", result['receipt'])

# transaction-auth
<b>Simple API service for JWT authentication, registration by login &amp; password</b>


<b>To run API:</b>
1) git clone "https://github.com/tegularis/transaction-auth.git"
2) run postgresql server 
3) create & fill <b>config/config.yml</b> according to <b>config/config_example.yml</b> fields

# methods:

---
    POST: /client/register

registers client in the API, returns JWT-token (5 minutes lifetime)

<b>body example:</b>


    "data": {
        "login": "your-login"
        "password": "unique-password"
    }

<b>response example:</b>
    
    "ok": true,
    "message": "success",
    "content": {
        "data": {
            "jwt_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnQiOnsiaWQiOjMsInV1aWQiOiI0MDIyODI4ZS1iZjc1LTRlYjMtODZkOS1mNTZiOTRjYmIwZWUiLCJsb2dpbiI6InhYeFB1c3N5MjQzRGVzdHJveWVyMTIzIiwicGFzc3dvcmQiOiIxMjMifSwiZXhwaXJhdGlvbl90aW1lIjoxNzMyNDY0NzczLjU0NjU0OH0.d7vVALaf7PLiBbV8tZ9s_S5r__xC_g-mAh8c395ULXI",
            "expiration_time": 1732464773.546548
        }
    }

---

    POST: /client/authenticate

returns fresh JWT-token for existing client (5 minutes lifetime)

<b>body example:</b>


    "data": {
        "login": "your-login"
        "password": "your-password"
    }

<b>response example:</b>
    
    "ok": true,
    "message": "success",
    "content": {
        "data": {
            "jwt_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnQiOnsiaWQiOjMsInV1aWQiOiI0MDIyODI4ZS1iZjc1LTRlYjMtODZkOS1mNTZiOTRjYmIwZWUiLCJsb2dpbiI6InhYeFB1c3N5MjQzRGVzdHJveWVyMTIzIiwicGFzc3dvcmQiOiIxMjMifSwiZXhwaXJhdGlvbl90aW1lIjoxNzMyNDY0NzczLjU0NjU0OH0.d7vVALaf7PLiBbV8tZ9s_S5r__xC_g-mAh8c395ULXI",
            "expiration_time": 1732464773.546548
        }
    }

---
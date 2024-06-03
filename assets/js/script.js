document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const usuario = document.getElementById('usuario').value;
    const senha = document.getElementById('senha').value;
    
    if (usuario === "charmander" && senha === "12345"){
        alert('Sucesso liberando seções');
        document.getElementById('dropdownContainer').style.display = 'flex'; // Display flex to align properly
    } else {
        alert('Senha e/ou usuário incorretos');
    }
});

document.getElementById('irParaSecao').addEventListener('click', function() {
    const selecao = document.getElementById('secoesDropdown').value;
    window.location.href = selecao;
});
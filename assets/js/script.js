document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const usuario = document.getElementById('usuario').value;
    const senha = document.getElementById('senha').value;
    
    if (usuario === "charmander" && senha === "12345"){
        alert('Sucesso liberando seções');
        document.getElementById('dropdownContainer').style.display = 'flex'; 
        document.querySelector('.header-login').addEventListener('submit', function(){
            this.classList.add('fade-out');
            this.addEventListener('animationend', () => {
            this.style.display = 'none';
              });
        })
    } else {
        alert('Senha e/ou usuário incorretos');
    }
});

document.getElementById('irParaSecao').addEventListener('click', function() {
    const selecao = document.getElementById('secoesDropdown').value;
    window.location.href = selecao;
});

let imagens=["./assets/img/lixo1.png", "./assets/img/lixo2.png", "./assets/img/peixeMorto1.png", "./assets/img/peixeMorto2.png", "./assets/img/acidente.png" ];
let index = 0;
let time = 3000;

function slideShow(){

    document.getElementById("imgbanner").src=imagens[index];
    index++;
    
        if(index == imagens.length){
            index=0;
        }
        setTimeout("slideShow()", time);
    }
    slideShow();
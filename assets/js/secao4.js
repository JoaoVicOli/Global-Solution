let imagens = ["./assets/img/lixo1.png", "./assets/img/lixo2.png", "./assets/img/peixeMorto1.png", "./assets/img/peixeMorto2.png", "./assets/img/acidente.png"];
let index = 0;
let time = 3000;

function slideShow() {
    document.getElementById("imgbanner").src = imagens[index];
    index++;
    
    if (index === imagens.length) {
        index = 0;
    }
    setTimeout(slideShow, time);
}

slideShow();


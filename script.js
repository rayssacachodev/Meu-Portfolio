//Seleciona todos os elementos com a classe 'fade-in':
const elementos =
document.querySelectorAll('.fade-in');

//Função que verifica se os elementos estão visíveis na tela:
function checkVisibility() {
    //Define o ponto de disparo do efeito (90% da altura da janela para cada elemento com fade-in:
    const triggerBottom = window.innerHeight * 0.9;
    elementos.forEach(el => {
        const top = el.getBoundingClientRect().top;
        if (top < triggerBottom) {
            el.classList.add('visible');
        }
    });
}

//verifica a visibilidade ao rolar a página:
window.addEventListener ('scroll', checkVisibility);

//Verifica a visibilidade ao carregar a página:
window.addEventListener ('load', checkVisibility);


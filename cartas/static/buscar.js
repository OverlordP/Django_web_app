const buscador = document.getElementById("buscador");
const cartas = document.getElementById("cartitas");
const boton = document.getElementById("botoncito");

const filtro = (e) => {
  for (let i = 0; i < cartas.children.length; i++) {
    let cartita =cartas.children[i].children[0].children[2].children[0].innerHTML;

    if(cartita.toLowerCase().includes(e.target.value.toLowerCase())){
        cartas.children[i].classList.remove("filtro")
    }
    else{
        cartas.children[i].classList.add("filtro")
    }

  }
};

buscador.addEventListener("keyup", filtro);

boton.addEventListener("click", (e)=>{
    e.preventDefault()
    console.log(cartas.children[0])
});

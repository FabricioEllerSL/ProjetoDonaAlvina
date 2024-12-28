function abrirModal(id) {
    const modal = document.getElementById(`modalVenda${id}`);
    if (modal) {
        modal.style.display = "block";
    } else {
        console.error(`Modal com ID modalVenda${id} não encontrado.`);
    }
}

function fecharModal(id) {
    const modal = document.getElementById(`modalVenda${id}`);
    if (modal) {
        modal.style.display = "none";
    } else {
        console.error(`Modal com ID modalVenda${id} não encontrado.`);
    }
}


window.onclick = function (event) {
    var modal = document.querySelectorAll(".modal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
};


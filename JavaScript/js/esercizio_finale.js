const nome_p = document.querySelectorAll("#nome_p") //Vado a prendere tutti gli id nome_p
const prezzi = document.querySelectorAll("#prezzo") //Vado a prendere tutti i prezzo
const totale = document.querySelector("#totale") //Vado a prendere il totale
const qta = document.querySelectorAll("#qta") //Prendo tutte le quantità

console.log(nome_p[0].textContent + "Prezzo: " + prezzi[0].textContent)

nome_p.forEach((nome, id) =>{
    console.log(nome.textContent + " " + id)
})


qta.forEach((q, id) =>{
    console.log(q.options[q.selectedIndex].value) //Vado a prendere il valore della select con opzione selezionata
    q.addEventListener("change", ()=>{
        totale_f() //Richiamo la funzione per il calcolo del totale
    })
})

function totale_f(){
    let totale_carrello = 0; //Serve per sommare tutti i prezzi
    prezzi.forEach((prezzo, id) =>{
        console.log(prezzo.textContent + " " + id)
        //let prezzo_int = prezzo.textContent.slice(0, prezzo.textContent.indexOf("€"))
        //let prezzo_int = prezzo.textContent.split("€")[0]; 
        //let prezzo_int = prezzo.textContent.replace("€", "") //Tolgo il simbolo dell'€ alla stringa 
        totale_carrello += Number(prezzo.textContent.replace("€", "")) * Number(qta[id].options[qta[id].selectedIndex].value)//Aggiornare la somma totale dei prezzi
    })
totale.textContent = totale_carrello + "€"
}

totale_f() //Lancio la funzione per calcolare il prezzo al caricamento della pagina
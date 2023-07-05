#Pagina principale
#Rif https://www.w3schools.com/python/python_ref_string.asp

testo = "ciao dal corso di python, python è il linguaggio del momento"

#IMPORTANTE le stringhe sono array di caratteri
print(testo[1])

#per conoscere la lunghezza di una stringa uso il metodo len(stringa da contare)
print(len(testo))

#Restituisce il numeri di volte che il termine cercato è presente nella stringa
#rif: https://www.w3schools.com/python/ref_string_count.asp
print(testo.count("python"))

#Trasformare solo la prima lettere di una stringa in maiuscolo
#rif: https://www.w3schools.com/python/ref_string_capitalize.asp
print(testo.capitalize())

#Trasformare tutte le iniziali delle parole in MAIUSCOLO
#rif: https://www.w3schools.com/python/ref_string_title.asp
print(testo.title())

#Trasformare tutta la stringa in MAIUSCOLO
#rif: https://www.w3schools.com/python/ref_string_upper.asp
print(testo.upper())

#Trasformare tutta la stringa in minuscolo
#rif: https://www.w3schools.com/python/ref_string_lower.asp
print(testo.lower())

#Per modificare il testo in una stringa
#rif: https://www.w3schools.com/python/ref_string_replace.asp
testo2 = testo.replace("python", "javascript")
print(testo2)

#Per eliminare gli spazzi prima e dopo la stringa
#Rif: https://www.w3schools.com/python/ref_string_strip.asp
testo3 = "     ciao   "
print(testo3)
print(testo3.strip())

testo4 =",,,,...banana...rrrr,,,gtknk,,,"
print(testo4)
print(testo4.strip(",.rgtk"))

#Eliminare gli spazzi o caratteri alla destra della stringa
testo5 = "      cioa       "
print(testo5)
print(testo5.rstrip())
print(testo5.lstrip())

#Per trasformare una stringa in un array
#Rif: https://www.w3schools.com/python/ref_string_split.asp

testo6 = "benvenuti nel corso di python"

ar_testo6 = testo6.split() #Senza nulla di default splicca con gli spazzi
print(ar_testo6)

testo6_a = "python#developer#corso"
ar_testo6_a = testo6_a.split("#")
print(ar_testo6_a)
ar_testo6_a = testo6_a.split("#", 1)
print(ar_testo6_a)

#Splitto con la nuova linea
#Rif: https://www.w3schools.com/python/ref_string_splitlines.asp
testo7 = "Benvenuti\nIn questo paragrafo parliamo di Python.\nPython è un linguaggio molto potente."
print(testo7)
ar_teso7 = testo7.splitlines()
print(ar_teso7)

#Trovare l'indice di inizio della parola cercate 
#Rif: https://www.w3schools.com/python/ref_string_rindex.asp
testo8 = "Mi casa, su casa"
print(testo8.index("casa")) #Primo
print(testo8.rindex("casa")) #Ultimo

#Come sapere come è fatta una stringa (conoscere se è numerica o testo)
testo9 = "12"
print(testo9.isnumeric())
# if testo9.isnumeric() == True:
#     print(f"Lo raddoppio: {int(testo9) * 2}")
# else:
#     print("Lo stampo: " + testo9)

if testo9.isnumeric():
    print(f"Lo raddoppio: {int(testo9) * 2}")
else:
    print("Lo stampo: " + testo9)

#Vedere se è alfanumerico isalnum()
#Rifhttps://www.w3schools.com/python/ref_string_isalnum.asp

#Vedere se è solo caratteri e non numeri isalpha()
#https://www.w3schools.com/python/ref_string_isalpha.asp

#Es:
#Data un testo ritornare quante volte una parola, scelta dall'utente è ripetuta nel testo
es_testo = "La campagna svizzera di Suvorov si svolse in territorio elvetico tra il settembre e l'ottobre del 1799 durante la guerra della seconda coalizione. Le truppe russo-austriache, che avevano già sconfitto ripetutamente tra aprile e agosto i francesi in Italia, attraversarono il San Gottardo al comando del feldmaresciallo Aleksandr Vasil'evič Suvorov, con l'ordine di marciare contro il generale Andrea Massena per scacciarlo dalla Repubblica Elvetica. Dopo le importanti vittorie dei mesi precedenti durante la campagna in Italia, Suvorov era rimasto padrone della situazione nella parte settentrionale della penisola e sembrava imminente una sconfitta definitiva dei francesi con il generale russo deciso a marciare addirittura verso la Francia, ma le divisioni e le rivalità delle potenze coalizzate avrebbero ben presto favorito la ripresa delle armate rivoluzionarie: per timore che l'influenza della Russia diventasse troppo grande, gli alleati, facendo anche leva sulle ambizioni dello zar Paolo I di presentarsi come liberatore della Svizzera, riuscirono a ottenere che le truppe russe interrompessero le loro operazioni in Italia e venissero rischierate nella Confederazione, lasciando l'iniziativa nella penisola agli austriaci. A Suvorov fu quindi ordinato di portarsi con il suo esercito verso nord e marciare attraverso il San Gottardo per congiungersi alle truppe russe appena condotte sulla Limmat dal generale Aleksandr Michajlovič Rimskij-Korsakov. Il maresciallo Suvorov prese dopo difficili combattimenti il San Gottardo e marciò poi faticosamente lungo la valle del fiume Reuss, costantemente contrastato dal generale Claude Lecourbe. Giunto ad Altdorf fu costretto a deviare a nord-est per le montagne, in quanto i francesi controllavano saldamente il lago dei Quattro Cantoni e i passi a ovest. Il generale Massena inviò quindi le divisioni dei generali Honoré Gazan e Édouard Mortier, coordinate dal generale Nicolas Soult, a bloccare l'avanzata dei russi tra Schwyz (o Svitto) e Glarona; Suvorov si diresse allora verso la Linth, ma anche qui, dopo qualche successo, le sue truppe furono ripetutamente respinte a Näfels dai soldati del generale Gabriel Molitor. La situazione del maresciallo Suvorov, isolato tra le montagne, con scarsi rifornimenti e contrastato su tutti i fronti dalle truppe francesi, divenne sempre più difficile; dopo aver appreso della disfatta dei generali Korsakov e von Hotze nella seconda battaglia di Zurigo, non gli rimase che tentare di ripiegare verso est allo scopo di mettere in salvo i resti del suo esercito, ormai molto provato. La ritirata dei russi fu molto difficoltosa e costò nuove pesanti perdite, mentre tutta l'artiglieria andò perduta; infine, passando per il passo di Panix, i russi raggiunsero il Reno a Jante (o Ilanz) il 7 ottobre e proseguirono quindi verso il Vorarlberg, dove si congiunsero con i superstiti del generale Korsakov. Suvorov venne richiamato a San Pietroburgo dove cadde nuovamente in disgrazia presso la corte zarista: Paolo I rifiutò di riceverlo in udienza e, ferito e malato, il vecchio generale morì dopo poche settimane nella capitale stessa il 18 maggio del 1800."

print(es_testo)

trova = input("Cosa vuoi cercare?: ")

if es_testo.lower().count(trova.lower()) > 0:
    print(f"Parola trovata e sono presenti {es_testo.lower().count(trova.lower())} occorrenze")
else:
    print("Parola non presente")


iron_man = "Tony-Stark-40-Torre Stark"
#testo_separato = iron_man.split("-")
nome, cognome, eta, residenza = iron_man.split("-") #Assegno alle variabili lo split
print(f"{nome} {cognome} {eta} {residenza}")
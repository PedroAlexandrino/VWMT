const ordenar_Part_Linha = document.getElementById('ordenar_Part_Linha');

Sortable.create(ordenar_Part_Linha, {
	animation: 150,
	ghostClass: 'blue-background-class',

	onEnd: () => {
		console.log('changed');
	},

	group: "lista_Part_Linha",
	store: {
		//Gurdar a ordem da lista:
		set: (sortable) => {
			const list_order = sortable.toArray();
			localStorage.setItem(sortable.options.group.name , list_order.join('|'));
		},

		//Obter a ordem da lista:
		get: (sortable) => {
			const list_order = localStorage.getItem(sortable.options.group.name);
			return list_order ? list_order.split('|') : [];
		}
	}
});
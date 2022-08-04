console.log('hello World')

var url = '/packing/clients-json/';
var url2 = '/packing/products-json/';
const clientsDataBox = document.getElementById('clients-data-box')
const clientInput = document.getElementById('clientes')

const clientsDataBox2 = document.getElementById('clients-data-box2')

const productsDataBox = document.getElementById('products-data-box')
const productInput = document.getElementById('produtos')

const typeDataBox = document.getElementById('type-data-box')

const productText = document.getElementById('product-text')
const typeText = document.getElementById('type-text')

const tabela = document.getElementById('example')

let selectedClient = null
let selectedProduct = null
let selectedType = null

$.ajax({
    type: 'GET',
    url: url,
    success: function (response) {
        console.log(response.data)
        const clientsData = response.data

        clientsData.map(item => {
            const option = document.createElement('div')
            option.textContent = item.oem
            option.setAttribute('class', 'item')
            option.setAttribute('value', item.name)
            clientsDataBox.appendChild(option)
        })

        clientsData.map(item => {
            var row = document.createElement("tr");
            var cell = document.createElement("td");
            cell.textContent = item.oem
            row.appendChild(cell)
            // clientsDataBox2.appendChild(row)
        })
        clientsData.map(item => {
            var row = document.createElement("tr");
            for (var i = 0; i < 5; i++) {
                var cell = document.createElement("td");
                if (i == 0) {
                    cell.textContent = item.oem
                    row.appendChild(cell)
                }
                if (i == 1) {
                    cell.textContent = item.oem
                    row.appendChild(cell)
                }
                //clientsDataBox2.appendChild(row)
            }
        })
    },
    error: function (error) {
        console.log(error)
    }
})
clientInput.addEventListener('change', e => {
    console.log(e.target.value)
    selectedClient = e.target.value

    productsDataBox.innerHTML = ""
    productText.textContent = "Choose product"
    productText.classList.add("default")
    typeDataBox.innerHTML = ""
    typeText.textContent = "Choose type"
    typeText.classList.add("default")

    $.ajax({
        type: 'GET',
        url: `/packing/products-json/${selectedClient}/`,
        success: function (response) {
            console.log(response.data)
            const productsData = response.data
            productsData.map(item => {
                const option = document.createElement('div')
                option.textContent = item.nome
                option.setAttribute('class', 'item')
                option.setAttribute('value', item.name)
                productsDataBox.appendChild(option)
            })
            productsData.map(item => {
                var row = document.createElement("tr");
                for (var i = 0; i < 5; i++) {
                    var cell = document.createElement("td");
                    if (i == 0)
                        cell.textContent = selectedClient.toUpperCase()
                    if (i == 1)
                        cell.textContent = item.nome
                    row.appendChild(cell)
                    clientsDataBox2.appendChild(row)
                }
            })
        },
        error: function (error) {
            console.log(error)
        }
    })

})

productInput.addEventListener('change', e => {
    console.log(e.target.value)
    selectedProduct = e.target.value

    typeDataBox.innerHTML = ""
    typeText.textContent = "Choose type"
    typeText.classList.add("default")

    $.ajax({
        type: 'GET',
        url: `/packing/type-json/${selectedProduct}/`,
        success: function (response) {
            console.log(response.data)
            const typeData = response.data
            typeData.map(item => {
                const option = document.createElement('div')
                option.textContent = item.nome
                option.setAttribute('class', 'item')
                option.setAttribute('value', item.name)
                typeDataBox.appendChild(option)
            })
            typeData.map(item => {
                var row = document.createElement("tr");
                for (var i = 0; i < 5; i++) {
                    var cell = document.createElement("td");
                    if (i == 0)
                        cell.textContent = selectedClient.toUpperCase()
                    if (i == 1)
                        cell.textContent = selectedProduct.toUpperCase()
                    if (i == 2)
                        cell.textContent = item.nome
                    row.appendChild(cell)
                    clientsDataBox2.appendChild(row)
                }
            })
        },
        error: function (error) {
            console.log(error)
        }
    })
})





// Función para mostrar productos según la categoría seleccionada
function showProducts(category) {
    // Puedes agregar más categorías y productos según tus necesidades
    const products = {
        beverages: ['Manzana', 'Plátano', 'Fresa'],
        vegetales: ['Zanahoria', 'Lechuga', 'Tomate'],
        carnes: ['Pollo', 'Res', 'Cerdo']
    };

    const productList = document.getElementById('products');
    const categoryProducts = products[category];

    // Limpiar la lista de productos antes de agregar nuevos
    productList.innerHTML = '';

    // Mostrar los productos de la categoría seleccionada
    categoryProducts.forEach(product => {
        const listItem = document.createElement('li');
        listItem.textContent = product;
        productList.appendChild(listItem);
    });
}

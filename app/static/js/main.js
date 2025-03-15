document.getElementById('sale-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const product = document.getElementById('product').value;
    const quantity = document.getElementById('quantity').value;

    const response = await fetch('/api/sales/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ product, quantity }),
    });

    const result = await response.json();
    console.log(result);
});

const express = require('express') 
const app = express() 
const products = [ 
    {id:1, name: "product 1", description: "description for product 1", price:10}, 
    {id:2, name: "product 2", description: "description for product 2", price:20}, 
    {id:3, name: "product 3", description: "description for product 3", price:30}
]

app.get('/products', (req, res)=> { 
    res.json(products) 
}) 
app.get('/products/:product_id', (req, res)=> { 
    const productId = parseInt(req.params.product_id) 
    //cari apakah id nya ada 
    const product = products.find(product => product.id === productId) 
    //jika id nya ada maka tampilkan datanya, jika tidak munculkan teks not found 
    if(product) { 
        res.json(product) 
    }else{ 
        res.status(404).json({error: "product not found"}) 
    } 
})

app.listen(5000, () => { 
    console.log("server berjalan") 
})
let p = fetch("http://127.0.0.1:5000/recipe?name=butter chicken")
p.then((value1)=>{
    return value1.json()
}).then((value2)=>{
    console.log(value2)
})
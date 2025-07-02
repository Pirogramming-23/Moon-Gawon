//main
function loadItems() {
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => console.items);
}

loadItems()
.then(items => {
    console.log(items);
    // displayItems(items);
    // setEvelntLIstener(items);
})
.catch(console.log)
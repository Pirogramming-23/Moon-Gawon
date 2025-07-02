//main
function loadItems() {
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => console.items);
}
//Update the list
function displayItems(items) {
    const container = document.querySelector('.items');
    const html = items.map(item => createHTMLString(item));
    console.log(html);
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

//create HTML
function createHTMLString(item) {
    return`
    <li class="item">
        <img src="${item.image} alt="${item.type}" class="item_thumbnail" />
        <span class="item_description">${item.gender},${item.size}</span>
    </li>
    `;
}
function onbuttonClick(event, items) {
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;
    if (key == null || value == null) {
        return;
    }
    displayItems(items.filter(item => item[key] === value));
}
function setEventListener(items) {
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click', () => displayItems(items));
    buttons.addEventListener('click', () => onbuttonClick(event, items));
}
loadItems()
    .then(items => {
    displayItems(items);
    //setEvelntLIstener(items);
})
.catch(console.log)
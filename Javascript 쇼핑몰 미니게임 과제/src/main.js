// main.js

function loadItems() {
  return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

function displayItems(items) {
  const container = document.querySelector('.items');
  container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

function createHTMLString(item) {
  return `
    <li class="item">
      <img src="${item.image}" alt="${item.type}" class="item__thumbnail" />
      <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
  `;
}

function onbuttonClick(event, items) {
  const target = event.target;
  const key = target.dataset.key;
  const value = target.dataset.value;
  if (key == null || value == null) {
    return;
  }
  const filtered= items.filter(item => item[key] === value);
  displayItems(filtered);
  // updateItems(items, key, value);
}

// function updateItems(items, key, value) {
//   const elements = document.querySelectorAll('.item');
//   elements.forEach((element, index) => {
//     if (items[index][key] === value) {
//       element.classList.remove('invisible');
//     } else {
//       element.classList.add('invisible');
//     }
//   });
// }

function setEventListener(items) {
  const logo = document.querySelector('.logo');
  const buttons = document.querySelector('.buttons');
  logo.addEventListener('click', () => displayItems(items));
  buttons.addEventListener('click', event => onbuttonClick(event, items));
}

loadItems()
  .then(items => {
    displayItems(items);
    setEventListener(items);
  })
  .catch(console.log);
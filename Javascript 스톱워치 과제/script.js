let startTime, intervalId;
let elapsed = 0;
let running = false;

const display = document.getElementById("display");
const startBtn = document.getElementById("start");
const stopBtn = document.getElementById("stop");
const resetBtn = document.getElementById("reset");
const recordList = document.getElementById("record-list");
const deleteCheckedBtn = document.getElementById("delete-checked");
const toggleAll = document.getElementById("toggle-all");

function format(ms) {
    const seconds = String(Math.floor(ms / 1000)).padStart(2, "0");
    const milliseconds = String(ms % 1000).padStart(3, "0").slice(0, 2);
    return `${seconds}:${milliseconds}`;
}

function updateDisplay() {
    display.textContent = format(elapsed + (Date.now() - startTime));
}

startBtn.onclick = function () {
    if (running) return;
    running = true;
    startTime = Date.now();
    intervalId = setInterval(updateDisplay, 50);
};

stopBtn.onclick = function () {
    if (!running) return;
    clearInterval(intervalId);
    elapsed += Date.now() - startTime;
    running = false;

    const li = document.createElement("li");
    li.innerHTML = `
        <input type="checkbox" class="record-checkbox" />
        <span class="record-time">${format(elapsed)}</span>
    `;
    recordList.appendChild(li);
};

resetBtn.onclick = function () {
    clearInterval(intervalId);
    running = false;
    elapsed = 0;
    display.textContent = "00:00";
};

deleteCheckedBtn.onclick = function () {
    const checkboxes = document.querySelectorAll(".record-checkbox");
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
        checkbox.closest("li").remove();
        }
    });
};

toggleAll.onchange = function () {
    const checkboxes = document.querySelectorAll(".record-checkbox");
    checkboxes.forEach(checkbox => {
        checkbox.checked = toggleAll.checked;
    });
};
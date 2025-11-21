async function loadValue() {
    const response = await fetch("/value");
    const data = await response.json();
    document.getElementById("display").innerText = data.value;
}

async function increment() {
    const response = await fetch("/update/plus", { method: "POST" });
    const data = await response.json();
    document.getElementById("display").innerText = data.value;
}

async function decrement() {
    const response = await fetch("/update/minus", { method: "POST" });
    const data = await response.json();
    document.getElementById("display").innerText = data.value;
}

loadValue();

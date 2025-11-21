async function refresh() {
    const res = await fetch("/value");
    const data = await res.json();
    document.getElementById("display").innerText = data.value;
}

async function increment() {
    await fetch("/change/up", { method: "POST" });
    refresh();
}

async function decrement() {
    await fetch("/change/down", { method: "POST" });
    refresh();
}

setInterval(refresh, 800);
refresh();

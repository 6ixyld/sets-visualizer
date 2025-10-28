function sendData() {
    const setA = document.getElementById('setA').value.split(',').map(x => x.trim());
    const setB = document.getElementById('setB').value.split(',').map(x => x.trim());
    const operation = document.getElementById('operation').value;

    fetch('/process', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ setA, setB, operation })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('result').innerText = `{ ${data.result.join(', ')} }`;
    });
}

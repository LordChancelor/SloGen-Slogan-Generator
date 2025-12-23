async function generateSlogan() {
    const product = document.getElementById('productInput').value;
    const keywords = document.getElementById('keywordInput').value;
    const resultText = document.getElementById('resultText');
    const loading = document.getElementById('loading');

    if (!product) {
        alert("Please enter a product name.");
        return;
    }

    resultText.innerText = "";
    loading.classList.remove('hidden');

    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ product: product, keywords: keywords })
        });

        const data = await response.json();
        
        loading.classList.add('hidden');
        if (data.slogan) {
            resultText.innerText = `"${data.slogan}"`;
        } else {
            resultText.innerText = "Could not generate slogan.";
        }
    } catch (error) {
        loading.classList.add('hidden');
        resultText.innerText = "Error connecting to server.";
        console.error(error);
    }
}
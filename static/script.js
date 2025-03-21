document.getElementById("url-form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const originalUrl = document.getElementById("original_url").value;
  const response = await fetch("/shorten", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ original_url: originalUrl }),
  });

  const result = await response.json();
  const resultDiv = document.getElementById("result");

  if (response.ok) {
    resultDiv.innerHTML = `
      <p>URL encurtada com sucesso:</p>
      <a href="${result.short_url}" target="_blank">${result.short_url}</a>
    `;
  } else {
    resultDiv.innerHTML = `<p style="color: red;">Erro: ${result.message}</p>`;
  }
});
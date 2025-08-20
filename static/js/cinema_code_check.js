document.addEventListener("DOMContentLoaded", function () {
    const input = document.querySelector("#id_cinema_code");
    if (!input) return;

    // Indicator qo'shamiz
    const indicator = document.createElement("div");
    indicator.classList.add("form-text", "mt-1");
    input.insertAdjacentElement("afterend", indicator);

    let timeout = null;

    input.addEventListener("input", function () {
        clearTimeout(timeout);
        indicator.innerHTML = `<div class="spinner-border spinner-border-sm text-primary" role="status"></div>🌀 Checking...`;

        timeout = setTimeout(() => {
            const code = input.value.trim();
            if (!code) {
                indicator.innerHTML = `<span class="text-muted">ℹ️ Enter a unique cinema code...</span>`;
                return;
            }

            fetch(`/check-cinema-code/?cinema_code=${encodeURIComponent(code)}`)
                .then(res => res.json())
                .then(data => {
                    if (data.is_taken) {
                        indicator.innerHTML = `<span class="badge bg-danger">❌ Taken!</span>`;
                    } else {
                        indicator.innerHTML = `<span class="badge bg-success">✅ Available!</span>`;
                    }
                })
                .catch(() => {
                    indicator.innerHTML = `<span class="badge bg-warning text-dark">⚠️ Error checking</span>`;
                });
        }, 500);
    });
});

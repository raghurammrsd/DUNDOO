document.addEventListener("DOMContentLoaded", () => {
  if (typeof Chart === "undefined") {
    console.warn("Chart.js not loaded");
    return;
  }

  
  const salesCanvas = document.getElementById("salesChart");
  if (salesCanvas && Array.isArray(salesLabels)) {
    const ctx = salesCanvas.getContext("2d");

    new Chart(ctx, {
      type: "bar",
      data: {
        labels: salesLabels,
        datasets: [
          {
            label: "Sales (₹)",
            data: salesData,
            backgroundColor: "rgba(241, 21, 25, 0.8)",
            borderRadius: 6
          },
          {
            label: "Profit (₹)",
            data: profitData,
            backgroundColor: "rgba(244, 63, 94, 0.8)",
            borderRadius: 6
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: (value) => "₹" + value.toLocaleString()
            },
            grid: {
              color: "#e5e7eb"
            }
          },
          x: {
            grid: {
              display: false
            }
          }
        },
        plugins: {
          legend: {
            position: "bottom"
          },
          tooltip: {
            callbacks: {
              label: (ctx) => {
                const val = ctx.parsed.y || 0;
                return `${ctx.dataset.label}: ₹${val.toLocaleString()}`;
              }
            }
          }
        }
      }
    });
  }

  const stockCanvas = document.getElementById("stockChart");
  if (stockCanvas && Array.isArray(stockLabels) && stockLabels.length) {
    const ctx2 = stockCanvas.getContext("2d");

    new Chart(ctx2, {
      type: "doughnut",
      data: {
        labels: stockLabels,
        datasets: [
          {
            data: stockValues,
            backgroundColor: [
              "#2563eb",
              "#f97316",
              "#22c55e",
              "#a855f7",
              "#e11d48",
              "#0ea5e9"
            ]
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: "right"
          },
          tooltip: {
            callbacks: {
              label: (ctx) => {
                const label = ctx.label || "";
                const value = ctx.parsed || 0;
                return `${label}: ₹${value.toLocaleString()}`;
              }
            }
          }
        },
        cutout: "65%"
      }
    });
  }
});

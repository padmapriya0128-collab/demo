let analysisChart = null;

function analyzeStudent() {
    const payload = {
        cgpa: document.getElementById('cgpa').value,
        skill: document.getElementById('skill').value,
        projects: document.getElementById('projects').value,
        certifications: document.getElementById('certifications').value,
        internships: document.getElementById('internships').value
    };

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => Promise.reject(err));
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('result').innerHTML =
            "<h3>Analysis Result</h3>" +
            "Score: " + data.score + "<br>" +
            "Status: " + data.readiness + "<br>" +
            "Recommendations: " + data.recommendations.join(', ');

        renderChart(data);
    })
    .catch(error => {
        console.error(error);
        document.getElementById('result').innerHTML =
            "Error connecting to backend!";
    });
}

function renderChart(data) {
    const ctx = document.getElementById('analysisChart').getContext('2d');
    const labels = [
        'Academics',
        'Skills',
        'Projects',
        'Certifications',
        'Internships'
    ];
    const values = [
        data.cgpa_score,
        data.skill_score,
        data.project_score,
        data.certification_score,
        data.internship_score
    ];

    if (analysisChart) {
        analysisChart.destroy();
    }

    analysisChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Component Scores',
                data: values,
                backgroundColor: [
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    'rgba(153, 102, 255, 0.6)',
                    'rgba(255, 99, 132, 0.6)'
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 99, 132, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 35
                }
            }
        }
    });
}
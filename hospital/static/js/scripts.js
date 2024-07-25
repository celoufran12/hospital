function refreshPatientList() {
    fetch('/patients')
        .then(response => response.text())
        .then(html => {
            document.getElementById('patient-list').innerHTML = html;
        })
        .catch(error => console.warn('Error fetching patient list:', error));
}

setInterval(refreshPatientList, 10000); // Refresh every 10 seconds

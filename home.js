document.getElementById('numberForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const numberID = document.getElementById('numberID').value;
    
    fetch(http://localhost:9876/numbers/${numberID})
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('prevState').textContent = 'Previous State: ' + JSON.stringify(data.windowPrevState);
            document.getElementById('currState').textContent = 'Current State: ' + JSON.stringify(data.windowCurrState);
            document.getElementById('numbers').textContent = 'Numbers: ' + JSON.stringify(data.numbers);
            document.getElementById('average').textContent = 'Average: ' + data.avg;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
});
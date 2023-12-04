document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('api-form');

  form.addEventListener('submit', function(event) {
    event.preventDefault();
    const userInput = document.getElementById('location').value;
    const resultContainer = document.getElementById('result-container');

    // Function to update the UI with the response or error
    const updateUI = (content) => {
      if (resultContainer) {
        resultContainer.textContent = content;
      } else {
        console.error('Result container not found');
      }
    };

    fetch('/api/process_request', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ user_input: userInput })
    })
    .then(response => response.json())
    .then(data => {
      console.log('API Response:', data); // Log the response to the console
      updateUI(typeof data === 'string' ? data : 'Invalid data format');
    })
    .catch(error => {
      console.error('Fetch Error:', error);
      updateUI('Error: ' + error.message);
    });
  });
});

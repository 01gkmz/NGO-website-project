// Add floating label functionality
document.querySelectorAll('.input-group input').forEach(input => {
  input.addEventListener('focus', function() {
    this.parentNode.classList.add('focused');
  });

  input.addEventListener('blur', function() {
    if (!this.value) {
      this.parentNode.classList.remove('focused');
    }
  });

  // Check if input has value on page load
  if (input.value) {
    input.parentNode.classList.add('focused');
  }
});

// Form submission with animation
document.getElementById('customerForm').addEventListener('submit', function(e) {
  const form = this;
  const submitBtn = form.querySelector('.submit-btn');

  // Add loading animation
  submitBtn.innerHTML = `
    <span>Saving...</span>
    <div class="spinner"></div>
  `;
});

// script.js

document.addEventListener('DOMContentLoaded', () => {

  // Highlight required fields
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      const inputs = form.querySelectorAll('input, select');
      let valid = true;

      inputs.forEach(input => {
        if (input.hasAttribute('required') && !input.value.trim()) {
          input.style.border = '2px solid red';
          valid = false;
        } else {
          input.style.border = '1px solid #ccc';
        }
      });

      if (!valid) {
        e.preventDefault();
        alert('Please fill all required fields!');
      }
    });
  });

  // Confirmation before submitting attendance
  const attendanceForm = document.querySelector('form[action="/update_attendance"]');
  if (attendanceForm) {
    attendanceForm.addEventListener('submit', (e) => {
      if (!confirm('Are you sure you want to update attendance?')) {
        e.preventDefault();
      }
    });
  }

  // Confirmation before submitting marks
  const marksForm = document.querySelector('form[action="/update_marks"]');
  if (marksForm) {
    marksForm.addEventListener('submit', (e) => {
      if (!confirm('Are you sure you want to update marks?')) {
        e.preventDefault();
      }
    });
  }

});

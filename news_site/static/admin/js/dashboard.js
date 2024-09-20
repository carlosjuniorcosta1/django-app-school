document.addEventListener('DOMContentLoaded', function () {
    const editToggle = document.getElementById('edit-toggle');
    const editForm = document.getElementById('edit-form');
    const descriptionText = document.getElementById('description-text');

    editToggle.addEventListener('change', () => {
        if (editToggle.checked) {
            descriptionText.style.display = 'none';
            editForm.style.display = 'block';
        } else {
            descriptionText.style.display = 'block';
            editForm.style.display = 'none';
        }
    });
});
alert('oi')

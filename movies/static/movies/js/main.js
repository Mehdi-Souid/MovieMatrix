document.addEventListener('DOMContentLoaded', () => {
    // Add any interactive features here
});
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('select[name="genre"], select[name="sort"]').forEach(select => {
        select.addEventListener('change', function() {
            this.form.submit();
        });
    });
});
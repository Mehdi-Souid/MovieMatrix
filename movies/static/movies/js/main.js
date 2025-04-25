// static/movies/js/main.js
document.addEventListener('DOMContentLoaded', () => {
    // Add any interactive features here
});
// static/movies/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    // Auto-submit form when filters change
    document.querySelectorAll('select[name="genre"], select[name="sort"]').forEach(select => {
        select.addEventListener('change', function() {
            this.form.submit();
        });
    });
});
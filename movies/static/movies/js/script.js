document.querySelectorAll('.wishlist-btn').forEach(button => {
    button.addEventListener('click', (e) => {
        if (!confirm('Add this movie to your wishlist?')) {
            e.preventDefault();
        }
    });
});
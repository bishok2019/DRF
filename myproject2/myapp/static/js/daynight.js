document.addEventListener('DOMContentLoaded', () => {
    const toggleCheckbox = document.getElementById('toggle-checkbox');
    const toggleIcon = document.getElementById('toggle-icon');

    const applyTheme = (theme) => {
        document.documentElement.setAttribute('data-theme', theme);
        toggleIcon.classList.toggle('sun', theme === 'light');
        toggleIcon.classList.toggle('moon', theme === 'dark');
        toggleIcon.textContent = theme === 'light' ? '☀️' : '🌙';
        localStorage.setItem('mode', theme);
    };

    toggleCheckbox.addEventListener('change', () => {
        applyTheme(toggleCheckbox.checked ? 'dark' : 'light');
    });

    // Initialize based on user preference
    const savedMode = localStorage.getItem('mode') || 'light';
    toggleCheckbox.checked = savedMode === 'dark';
    applyTheme(savedMode);
});

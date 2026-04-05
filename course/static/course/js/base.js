// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 1. DARK MODE
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const themeToggle = document.getElementById('theme-toggle');
const themeIcon   = document.getElementById('theme-icon');

// Apply saved preference on page load
if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark-mode');
    themeIcon.textContent = '☀️';
} else {
    document.body.classList.remove('dark-mode');
    themeIcon.textContent = '🌙';
}

themeToggle.addEventListener('click', () => {
    const isDark = document.body.classList.toggle('dark-mode');
    themeIcon.textContent = isDark ? '☀️' : '🌙';
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
});


// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 2. SMART SEARCH
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 2. SMART SEARCH
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
(function () {

    function safeJSON(id) {
        const el = document.getElementById(id);
        if (!el) return [];
        try {
            const parsed = JSON.parse(el.textContent);
            // Make sure it's always an array
            return Array.isArray(parsed) ? parsed : [];
        } catch (e) {
            console.error('safeJSON parse error:', e);
            return [];
        }
    }

    const COURSES = safeJSON('courses-data');
    const NOTES   = safeJSON('notes-data');

    // DEBUG — remove these two lines once search is working
    console.log('COURSES:', COURSES);
    console.log('NOTES:', NOTES);

    const path          = window.location.pathname;
    const isCoursesPage = path.includes('/courses');
    const isNotesPage   = path.includes('/notes');
    const isSearchable  = isCoursesPage || isNotesPage;

    // DEBUG — remove once working
    console.log('path:', path, '| isCoursesPage:', isCoursesPage, '| isNotesPage:', isNotesPage);

    const searchInput = document.getElementById('nav-search-input');
    const resultsBox  = document.getElementById('search-results-box');
    const resultsList = document.getElementById('search-results-list');
    const noResults   = document.getElementById('search-no-results');
    const queryLabel  = document.getElementById('search-query-label');

    if (isCoursesPage)    searchInput.placeholder = 'Search courses...';
    else if (isNotesPage) searchInput.placeholder = 'Search notes...';
    else                  searchInput.placeholder = 'Search...';

    searchInput.addEventListener('input', function () {
        const query = this.value.trim().toLowerCase();

        if (!query || !isSearchable) {
            resultsBox.style.display = 'none';
            return;
        }

        const pool    = isCoursesPage ? COURSES : NOTES;
        const matches = pool.filter(item =>
            item.title.toLowerCase().includes(query)
        );

        resultsBox.style.display = 'block';
        resultsList.innerHTML    = '';

        if (matches.length > 0) {
            noResults.style.display = 'none';
            matches.forEach(item => {
                const a     = document.createElement('a');
                a.href      = item.url || '#';
                a.className = 'search-result-item';

                const i      = item.title.toLowerCase().indexOf(query);
                const before = item.title.slice(0, i);
                const match  = item.title.slice(i, i + query.length);
                const after  = item.title.slice(i + query.length);
                a.innerHTML  = `${before}<mark>${match}</mark>${after}`;

                resultsList.appendChild(a);
            });
        } else {
            noResults.style.display = 'flex';
            queryLabel.textContent  = this.value.trim();
        }
    });

    document.addEventListener('click', function (e) {
        const wrapper = document.getElementById('search-wrapper');
        if (wrapper && !wrapper.contains(e.target)) {
            resultsBox.style.display = 'none';
        }
    });

})();

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// 3. MOBILE MENU (kept for future use)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const menuBtn    = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });
}
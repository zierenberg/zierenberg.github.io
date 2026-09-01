// --- Email obfuscation (kept JS-only on purpose: never present in static HTML) ---
(() => {
    const u = 'johannes.zierenberg';
    const d = 'ds.mpg.de';
    const e = document.getElementById('email');
    if (e) e.innerHTML = `<a href="mailto:${u}@${d}">${u}@${d}</a>`;
})();

// --- Expandable sections (CV / Publications / Talks): content is pre-rendered in the HTML ---
function initExpandable(listId) {
    const list = document.getElementById(listId);
    if (!list) return;

    const collapsed = list.dataset.collapsedHeight;
    list.style.setProperty('--collapsed-height', collapsed);

    const expandBtn = list.nextElementSibling;
    const headerBtn = list.closest('section').querySelector('.collapse-header-btn');
    const expandInner = expandBtn.querySelector('.expand-toggle-inner');
    const headerInner = headerBtn.querySelector('.expand-toggle-inner');
    const collapsedLabel = expandInner.textContent;

    function expand() {
        list.classList.add('expanded');
        expandInner.textContent = 'Show less';
        headerInner.textContent = 'Show less';
        headerBtn.style.display = 'inline-block';
    }

    function collapse() {
        list.classList.remove('expanded');
        expandInner.textContent = collapsedLabel;
        headerBtn.style.display = 'none';
    }

    expandBtn.addEventListener('click', () => {
        list.classList.contains('expanded') ? collapse() : expand();
    });

    headerBtn.addEventListener('click', collapse);
}

['cv-list', 'publications-list', 'talks-list'].forEach(initExpandable);

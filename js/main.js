// Object-Oriented System Design (BCS054 / KCS054) Interactivity Engine
document.addEventListener('DOMContentLoaded', () => {
  // Filter questions by unit and year
  const filterButtons = document.querySelectorAll('button[data-filter]');
  const searchInput = document.getElementById('search-input');
  const questionItems = document.querySelectorAll('.question-item');
  const countBadge = document.getElementById('item-count');

  let activeUnit = 'all';
  let activeYear = 'all';
  let searchQuery = '';

  function applyFilters() {
    let visibleCount = 0;

    questionItems.forEach(item => {
      const itemUnit = item.getAttribute('data-unit') || '';
      const itemYear = item.getAttribute('data-year') || '';
      const textContent = item.textContent.toLowerCase();

      const unitMatch = (activeUnit === 'all' || itemUnit === activeUnit);
      const yearMatch = (activeYear === 'all' || itemYear.includes(activeYear));
      const searchMatch = !searchQuery || textContent.includes(searchQuery);

      if (unitMatch && yearMatch && searchMatch) {
        item.style.display = '';
        visibleCount++;
      } else {
        item.style.display = 'none';
      }
    });

    if (countBadge) {
      countBadge.textContent = `${visibleCount} Questions`;
    }
  }

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const filterType = btn.getAttribute('data-filter-type');
      const filterValue = btn.getAttribute('data-filter');

      // Update active state in same group
      document.querySelectorAll(`button[data-filter-type="${filterType}"]`).forEach(b => {
        b.classList.remove('active');
      });
      btn.classList.add('active');

      if (filterType === 'unit') {
        activeUnit = filterValue;
      } else if (filterType === 'year') {
        activeYear = filterValue;
      }

      applyFilters();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim().toLowerCase();
      applyFilters();
    });
  }

  // Copy code blocks
  document.querySelectorAll('pre').forEach(pre => {
    pre.addEventListener('click', (e) => {
      if (e.target.tagName === 'BUTTON' || e.ctrlKey || e.metaKey) {
        const code = pre.querySelector('code')?.innerText || pre.innerText;
        navigator.clipboard.writeText(code).then(() => {
          const originalBorder = pre.style.borderColor;
          pre.style.borderColor = 'var(--success)';
          setTimeout(() => { pre.style.borderColor = originalBorder; }, 1000);
        });
      }
    });
  });
});

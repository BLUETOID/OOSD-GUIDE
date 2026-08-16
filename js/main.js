/**
 * BCS054: Object Oriented System Design with C++
 * Master Client Engine: Syntax Highlighter, Search Indexer, Quiz Engine, Accordions, & Theme Toggle
 */

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initReadingProgressBar();
  initSyntaxHighlighter();
  initCodeCopyButtons();
  initExamAccordions();
  initPyqFilters();
  initSearchModal();
  initBackToTop();
  initTocScrollSpy();
  initMobileMenu();
  initQuizEngine();
});

/* ==========================================================================
   1. Theme Switcher (Dark/Light with Persistence)
   ========================================================================== */
function initThemeToggle() {
  const themeToggleBtn = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  const htmlEl = document.documentElement;

  const savedTheme = localStorage.getItem('bcs054-theme') || 'dark';
  htmlEl.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = htmlEl.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      htmlEl.setAttribute('data-theme', newTheme);
      localStorage.setItem('bcs054-theme', newTheme);
      updateThemeIcon(newTheme);
    });
  }

  function updateThemeIcon(theme) {
    if (!themeIcon) return;
    if (theme === 'dark') {
      themeIcon.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
          <line x1="1" y1="12" x2="3" y2="12"></line>
          <line x1="21" y1="12" x2="23" y2="12"></line>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>`;
    } else {
      themeIcon.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>`;
    }
  }
}

/* ==========================================================================
   2. Reading Progress Bar
   ========================================================================== */
function initReadingProgressBar() {
  const progressBar = document.getElementById('reading-progress');
  if (!progressBar) return;

  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
    progressBar.style.width = `${progress}%`;
  });
}

/* ==========================================================================
   3. Syntax Highlighter Engine (C++ & C)
   ========================================================================== */
function initSyntaxHighlighter() {
  const codeBlocks = document.querySelectorAll('pre code');
  
  const keywords = [
    'alignas', 'alignof', 'and', 'and_eq', 'asm', 'atomic_cancel', 'atomic_commit',
    'atomic_noexcept', 'auto', 'bitand', 'bitor', 'bool', 'break', 'case', 'catch',
    'char', 'char8_t', 'char16_t', 'char32_t', 'class', 'compl', 'concept', 'const',
    'consteval', 'constexpr', 'constinit', 'const_cast', 'continue', 'co_await',
    'co_return', 'co_yield', 'decltype', 'default', 'delete', 'do', 'double',
    'dynamic_cast', 'else', 'enum', 'explicit', 'export', 'extern', 'false', 'float',
    'for', 'friend', 'goto', 'if', 'inline', 'int', 'long', 'mutable', 'namespace',
    'new', 'noexcept', 'not', 'not_eq', 'nullptr', 'operator', 'or', 'or_eq',
    'private', 'protected', 'public', 'reflexpr', 'register', 'reinterpret_cast',
    'requires', 'return', 'short', 'signed', 'sizeof', 'static', 'static_assert',
    'static_cast', 'struct', 'switch', 'synchronized', 'template', 'this',
    'thread_local', 'throw', 'true', 'try', 'typedef', 'typeid', 'typename',
    'union', 'unsigned', 'using', 'virtual', 'void', 'volatile', 'wchar_t', 'while',
    'xor', 'xor_eq', 'override', 'final'
  ];

  const types = [
    'string', 'vector', 'map', 'set', 'unordered_map', 'unordered_set', 'pair',
    'tuple', 'size_t', 'uint8_t', 'uint16_t', 'uint32_t', 'uint64_t', 'int8_t',
    'int16_t', 'int32_t', 'int64_t', 'ostream', 'istream', 'iostream', 'ifstream',
    'ofstream', 'stringstream', 'function', 'unique_ptr', 'shared_ptr', 'weak_ptr',
    'Complex', 'Shape', 'Circle', 'Rectangle', 'BankAccount', 'Employee', 'Customer',
    'Order', 'OrderItem', 'Matrix', 'CustomString', 'SinglyLinkedList', 'SmartBulb'
  ];

  codeBlocks.forEach(codeEl => {
    const rawText = codeEl.innerText;
    codeEl.setAttribute('data-raw-code', rawText);

    let html = escapeHtml(rawText);

    // Comments (Single line and Multi-line)
    html = html.replace(/(\/\/[^\n]*)/g, '<span class="tok-comment">$1</span>');
    html = html.replace(/(\/\*[\s\S]*?\*\/)/g, '<span class="tok-comment">$1</span>');

    // Preprocessor directives
    html = html.replace(/(^\s*#\s*[a-zA-Z_]\w*.*$)/gm, '<span class="tok-preproc">$1</span>');

    // Strings
    html = html.replace(/("(?:[^"\\]|\\.)*")/g, '<span class="tok-string">$1</span>');
    html = html.replace(/('(?:[^'\\]|\\.)*')/g, '<span class="tok-string">$1</span>');

    // Numbers
    html = html.replace(/\b(\d+(\.\d+)?([eE][+-]?\d+)?(f|F|l|L|u|U)?)\b/g, '<span class="tok-num">$1</span>');

    // Keywords
    keywords.forEach(kw => {
      const regex = new RegExp(`\\b(${kw})\\b(?![^<]*>)`, 'g');
      html = html.replace(regex, '<span class="tok-keyword">$1</span>');
    });

    // Known types
    types.forEach(t => {
      const regex = new RegExp(`\\b(${t})\\b(?![^<]*>)`, 'g');
      html = html.replace(regex, '<span class="tok-type">$1</span>');
    });

    codeEl.innerHTML = html;
  });
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

/* ==========================================================================
   4. Code Block Copy Buttons
   ========================================================================== */
function initCodeCopyButtons() {
  document.querySelectorAll('.copy-button').forEach(button => {
    button.addEventListener('click', async () => {
      const container = button.closest('.code-container');
      const codeEl = container.querySelector('code');
      const textToCopy = codeEl.getAttribute('data-raw-code') || codeEl.innerText;

      try {
        await navigator.clipboard.writeText(textToCopy);
        const originalText = button.innerText;
        button.innerText = 'Copied!';
        button.style.borderColor = 'var(--success-border)';
        button.style.color = 'var(--success-text)';

        setTimeout(() => {
          button.innerText = originalText;
          button.style.borderColor = '';
          button.style.color = '';
        }, 2000);
      } catch (err) {
        button.innerText = 'Failed';
        setTimeout(() => { button.innerText = 'Copy Code'; }, 2000);
      }
    });
  });
}

/* ==========================================================================
   5. Exam Question Accordions
   ========================================================================== */
function initExamAccordions() {
  document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', () => {
      const item = header.closest('.accordion-item');
      item.classList.toggle('open');
    });
  });
}

/* ==========================================================================
   6. PYQ Mark Filters
   ========================================================================== */
function initPyqFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const items = document.querySelectorAll('.accordion-item[data-marks]');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      items.forEach(item => {
        const itemMarks = item.getAttribute('data-marks');
        if (filter === 'all' || filter === itemMarks) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

/* ==========================================================================
   7. Interactive Quiz Engine
   ========================================================================== */
const quizQuestions = [
  {
    question: "1. Which UML diagram emphasizes the explicit chronological time-ordering of messages along vertical lifelines?",
    options: ["Collaboration Diagram", "Sequence Diagram", "Activity Diagram", "Class Diagram"],
    correct: 1,
    explanation: "Sequence Diagrams emphasize chronological time-ordering along vertical lifelines, whereas Collaboration diagrams emphasize object structural layouts."
  },
  {
    question: "2. Which C++ cast operator is evaluated at RUNTIME using RTTI for safe polymorphic downcasting?",
    options: ["static_cast", "const_cast", "dynamic_cast", "reinterpret_cast"],
    correct: 2,
    explanation: "dynamic_cast uses Run-Time Type Information (RTTI) to safely downcast base class pointers to derived classes, returning nullptr if invalid."
  },
  {
    question: "3. What is the fundamental cause of a 'Double Free Crash' when copying objects with dynamic memory?",
    options: ["Virtual destructor omission", "Shallow copying of raw pointer members", "Friend function access", "Overloaded stream operators"],
    correct: 1,
    explanation: "Default shallow copy copies the raw pointer address. When both objects are destroyed, delete is invoked twice on the exact same heap memory block."
  },
  {
    question: "4. How is the Multiple Inheritance Diamond Problem resolved in C++?",
    options: ["Using nested classes", "Declaring virtual public Base in intermediate derived classes", "Using static member functions", "Declaring private base constructors"],
    correct: 1,
    explanation: "Virtual base class inheritance (virtual public Base) guarantees that only a single shared instance of the root base class is created in memory."
  },
  {
    question: "5. Which of the following C++ operators CANNOT be overloaded?",
    options: ["+", "[]", ":: (Scope Resolution)", "=="],
    correct: 2,
    explanation: "The operators '::', '.', '.*', '?:', 'sizeof', and 'typeid' cannot be overloaded in C++."
  },
  {
    question: "6. Why can a static member function NOT access the 'this' pointer in C++?",
    options: ["Because static functions are private", "Because static functions belong to the class and are called without an object instance", "Because static functions cannot return values", "Because static functions use virtual tables"],
    correct: 1,
    explanation: "Static member functions are invoked at class scope (Class::func()) without an instantiated object memory address, so no implicit 'this' pointer exists."
  },
  {
    question: "7. In Rumbaugh's OMT methodology, which model captures state transitions and events over time?",
    options: ["Functional Model", "Dynamic Model", "Object Model", "Structural Model"],
    correct: 1,
    explanation: "The Dynamic Model represents temporal and behavioral state changes over time using statechart diagrams."
  },
  {
    question: "8. What is the primary difference between <<include>> and <<extend>> in Use Case diagrams?",
    options: ["<<include>> is optional; <<extend>> is mandatory", "<<include>> is mandatory and unconditional; <<extend>> is conditional and optional", "Both represent generalization hierarchies", "<<extend>> is executed before <<include>>"],
    correct: 1,
    explanation: "<<include>> executes the included behavior unconditionally; <<extend>> executes conditionally only when an extension point is reached."
  },
  {
    question: "9. What is Name Mangling in C++?",
    options: ["Deleting unused variable names", "Encoding parameter type signatures into symbol names for function overloading", "Converting class names to lowercase", "Macro text replacement"],
    correct: 1,
    explanation: "Name mangling is the compiler process of decorating function identifiers with their parameter types to differentiate overloaded functions for linkers."
  },
  {
    question: "10. Why MUST polymorphic base classes declare a virtual destructor (virtual ~Base())?",
    options: ["To prevent derived class construction", "To ensure the derived destructor executes upon 'delete basePtr', preventing memory leaks", "To enable multiple inheritance", "To allocate dynamic VTables"],
    correct: 1,
    explanation: "Without a virtual destructor, 'delete basePtr' performs early binding, calling only the base destructor and leaking derived class heap resources."
  },
  {
    question: "11. In procedural C, how is single inheritance mapped using structs?",
    options: ["By using global arrays", "By embedding the base struct as the FIRST member of the derived struct", "By creating multiple main functions", "By using void pointers only"],
    correct: 1,
    explanation: "Embedding the base struct first aligns the memory addresses, allowing safe pointer casting: (Shape*)&circle."
  },
  {
    question: "12. What does an open diamond symbol (◇──────) represent in a UML Class Diagram?",
    options: ["Composition (Strong part-of)", "Generalization (Is-a)", "Aggregation (Weak has-a)", "Dependency (Uses)"],
    correct: 2,
    explanation: "An open diamond represents Aggregation (weak whole-part where parts survive independently); a filled diamond (◆) represents Composition."
  },
  {
    question: "13. What are synchronization bars with multiple outgoing arrows in an Activity Diagram called?",
    options: ["Decision Nodes", "Join Bars", "Fork Bars", "Merge Nodes"],
    correct: 2,
    explanation: "A Fork bar splits a single control flow into multiple concurrent parallel flows; a Join bar synchronizes multiple incoming parallel flows."
  },
  {
    question: "14. How must Default Arguments be arranged in a C++ function parameter list?",
    options: ["From left to right", "Strictly from right to left (trailing parameters first)", "In alphabetical order", "Any arbitrary position"],
    correct: 1,
    explanation: "C++ requires all default arguments to be assigned strictly from right to left with no non-default parameters following a default parameter."
  },
  {
    question: "15. In Kruchten's 4+1 View Architecture, which view resides at the center linking all others?",
    options: ["Design View", "Process View", "Use Case View (+1)", "Deployment View"],
    correct: 2,
    explanation: "The Use Case View ('+1') sits at the center, driving and validating the Design, Process, Implementation, and Deployment views."
  }
];

function initQuizEngine() {
  const titleEl = document.getElementById('quiz-question-title');
  const optionsGroup = document.getElementById('quiz-options-group');
  const explanationEl = document.getElementById('quiz-explanation');
  const progressLabel = document.getElementById('quiz-progress-label');
  const nextBtn = document.getElementById('quiz-next-btn');
  const prevBtn = document.getElementById('quiz-prev-btn');
  const timerDisplay = document.getElementById('quiz-timer-display');
  const resultsCard = document.getElementById('quiz-results-card');
  const finalScoreEl = document.getElementById('quiz-final-score');
  const finalPctEl = document.getElementById('quiz-final-percentage');
  const restartBtn = document.getElementById('quiz-restart-btn');

  if (!titleEl) return;

  let currentIdx = 0;
  let userAnswers = new Array(quizQuestions.length).fill(null);
  let timeLeft = 15 * 60; // 15 minutes
  let timerInterval = null;

  startTimer();
  renderQuestion(currentIdx);

  function startTimer() {
    if (timerInterval) clearInterval(timerInterval);
    timerInterval = setInterval(() => {
      timeLeft--;
      if (timeLeft <= 0) {
        clearInterval(timerInterval);
        submitQuiz();
      }
      const mins = Math.floor(timeLeft / 60);
      const secs = timeLeft % 60;
      if (timerDisplay) {
        timerDisplay.innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
      }
    }, 1000);
  }

  function renderQuestion(idx) {
    const q = quizQuestions[idx];
    progressLabel.innerText = `Question ${idx + 1} of ${quizQuestions.length}`;
    titleEl.innerText = q.question;
    optionsGroup.innerHTML = '';
    explanationEl.classList.remove('visible');
    explanationEl.innerHTML = '';

    q.options.forEach((optText, optIdx) => {
      const optBtn = document.createElement('div');
      optBtn.className = 'quiz-option';
      if (userAnswers[idx] === optIdx) {
        optBtn.classList.add('selected');
        if (userAnswers[idx] === q.correct) {
          optBtn.classList.add('correct');
        } else {
          optBtn.classList.add('wrong');
        }
      }

      optBtn.innerHTML = `<strong>${String.fromCharCode(65 + optIdx)}.</strong> ${optText}`;
      optBtn.addEventListener('click', () => selectOption(idx, optIdx));
      optionsGroup.appendChild(optBtn);
    });

    if (userAnswers[idx] !== null) {
      showExplanation(idx);
    }

    if (idx === quizQuestions.length - 1) {
      nextBtn.innerText = 'Finish Examination';
    } else {
      nextBtn.innerText = 'Next Question';
    }

    if (idx > 0) {
      prevBtn.style.visibility = 'visible';
    } else {
      prevBtn.style.visibility = 'hidden';
    }
  }

  function selectOption(qIdx, optIdx) {
    if (userAnswers[qIdx] !== null) return; // Prevent changing after selection
    userAnswers[qIdx] = optIdx;
    renderQuestion(qIdx);
  }

  function showExplanation(qIdx) {
    const q = quizQuestions[qIdx];
    const isCorrect = userAnswers[qIdx] === q.correct;
    explanationEl.innerHTML = `
      <div style="font-weight: 700; color: ${isCorrect ? 'var(--success-text)' : '#f87171'}; margin-bottom: 0.35rem;">
        ${isCorrect ? '[Correct Answer]' : '[Incorrect]'}
      </div>
      <div>${q.explanation}</div>
    `;
    explanationEl.classList.add('visible');
  }

  nextBtn.addEventListener('click', () => {
    if (currentIdx < quizQuestions.length - 1) {
      currentIdx++;
      renderQuestion(currentIdx);
    } else {
      submitQuiz();
    }
  });

  prevBtn.addEventListener('click', () => {
    if (currentIdx > 0) {
      currentIdx--;
      renderQuestion(currentIdx);
    }
  });

  function submitQuiz() {
    clearInterval(timerInterval);
    let score = 0;
    quizQuestions.forEach((q, i) => {
      if (userAnswers[i] === q.correct) score++;
    });

    const pct = Math.round((score / quizQuestions.length) * 100);
    document.querySelector('.quiz-card').style.display = 'none';
    resultsCard.style.display = 'block';
    finalScoreEl.innerText = `${score} / ${quizQuestions.length}`;
    finalPctEl.innerText = `Final Score: ${pct}% (${pct >= 60 ? 'PASSED with Distinction' : 'Needs Further Revision'})`;
  }

  if (restartBtn) {
    restartBtn.addEventListener('click', () => {
      currentIdx = 0;
      userAnswers = new Array(quizQuestions.length).fill(null);
      timeLeft = 15 * 60;
      document.querySelector('.quiz-card').style.display = 'block';
      resultsCard.style.display = 'none';
      startTimer();
      renderQuestion(0);
    });
  }
}

/* ==========================================================================
   8. Global Search Modal (Ctrl+K)
   ========================================================================== */
const searchIndex = [
  { title: "Unit 1: Object Oriented Modeling Overview", url: "unit1.html#section-1", snippet: "Core principles of OOP, abstraction, encapsulation, inheritance, polymorphism." },
  { title: "Unit 1: 4+1 View Architecture (Kruchten)", url: "unit1.html#section-3", snippet: "Use Case (+1), Design, Process, Implementation, and Deployment views." },
  { title: "Unit 2: UML Class and Object Diagrams", url: "unit2.html#section-2", snippet: "Static class structure, visibility specifiers, multiplicity, and runtime object snapshots." },
  { title: "Unit 2: Sequence & Collaboration Diagrams", url: "unit2.html#section-3", snippet: "Dynamic interaction modeling, vertical lifelines, activation boxes, and message orders." },
  { title: "Unit 2: Activity & State Machine Diagrams", url: "unit2.html#section-4", snippet: "Forks, joins, swimlanes, action nodes, state transitions, and event triggers." },
  { title: "Unit 3: Combining 3 Models (Rumbaugh OMT)", url: "unit3.html#section-2", snippet: "Integration of Object Model, Dynamic Model, and Functional Model." },
  { title: "Unit 3: Mapping OOP Concepts to Procedural C", url: "unit3.html#section-5", snippet: "Translating classes into C structs, explicit this pointer, and VTable dynamic dispatch." },
  { title: "Unit 4: 4-Stage C++ Compilation Pipeline", url: "unit4.html#section-1", snippet: "Preprocessing (cpp), Compilation (g++), Assembly (as), and Linking (ld)." },
  { title: "Unit 4: Explicit Typecasting Operators", url: "unit4.html#section-1-6", snippet: "static_cast, dynamic_cast (RTTI), const_cast, and reinterpret_cast." },
  { title: "Unit 4: Inline Functions vs Preprocessor Macros", url: "unit4.html#section-2-3", snippet: "Compiler inlining, type validation, and macro side-effect hazards." },
  { title: "Unit 5: Static Class Members & Scope", url: "unit5.html#section-1", snippet: "Shared static data segment allocation and static member functions without this pointer." },
  { title: "Unit 5: Shallow vs Deep Copy Constructors", url: "unit5.html#section-1-3", snippet: "Preventing double-free crashes with custom dynamic heap allocation copy constructors." },
  { title: "Unit 5: Multiple Inheritance & Diamond Problem", url: "unit5.html#section-3", snippet: "Virtual base classes (virtual public Base) eliminating duplicate storage." },
  { title: "Unit 5: Runtime Polymorphism & VTable/VPtr", url: "unit5.html#section-4", snippet: "Virtual function tables, object _vptr dereferencing, and virtual destructors." },
  { title: "PYQ Hub: 38 Two-Mark Solved Questions", url: "pyqs.html#section-2m", snippet: "All 38 short-answer university exam questions with concise model answers." },
  { title: "PYQ Hub: 69 Seven-Mark Solved Questions", url: "pyqs.html#section-7m", snippet: "All 69 long-answer design, numerical, and coding university exam questions." },
  { title: "Quick Revision Cheat Sheet & Viva Notes", url: "cheat-sheet.html", snippet: "High-density 1-liner definitions, master comparison tables, and top 10 exam traps." },
  { title: "Interactive Mock Exam Quiz", url: "quiz.html", snippet: "15-question university pattern test with automated scoring and explanations." }
];

function initSearchModal() {
  const searchBtn = document.getElementById('search-btn');
  const backdrop = document.getElementById('search-modal-backdrop');
  const input = document.getElementById('search-input');
  const resultsContainer = document.getElementById('search-results');

  if (!backdrop || !input) return;

  function openSearch() {
    backdrop.classList.add('active');
    input.value = '';
    renderResults(searchIndex);
    input.focus();
  }

  function closeSearch() {
    backdrop.classList.remove('active');
  }

  if (searchBtn) searchBtn.addEventListener('click', openSearch);

  backdrop.addEventListener('click', (e) => {
    if (e.target === backdrop) closeSearch();
  });

  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      openSearch();
    }
    if (e.key === 'Escape' && backdrop.classList.contains('active')) {
      closeSearch();
    }
  });

  input.addEventListener('input', () => {
    const query = input.value.trim().toLowerCase();
    if (!query) {
      renderResults(searchIndex);
      return;
    }

    const filtered = searchIndex.filter(item => 
      item.title.toLowerCase().includes(query) || 
      item.snippet.toLowerCase().includes(query)
    );
    renderResults(filtered);
  });

  function renderResults(list) {
    resultsContainer.innerHTML = '';
    if (list.length === 0) {
      resultsContainer.innerHTML = `<div style="padding: 1.5rem; text-align: center; color: var(--text-muted);">No matching topics found.</div>`;
      return;
    }

    list.forEach(item => {
      const a = document.createElement('a');
      a.className = 'search-result-item';
      a.href = item.url;
      a.innerHTML = `
        <div class="search-result-title">${item.title}</div>
        <div class="search-result-snippet">${item.snippet}</div>
      `;
      a.addEventListener('click', closeSearch);
      resultsContainer.appendChild(a);
    });
  }
}

/* ==========================================================================
   9. Back to Top Button
   ========================================================================== */
function initBackToTop() {
  const backToTopBtn = document.getElementById('back-to-top');
  if (!backToTopBtn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }
  });

  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ==========================================================================
   10. TOC ScrollSpy
   ========================================================================== */
function initTocScrollSpy() {
  const tocLinks = document.querySelectorAll('.toc-link');
  if (tocLinks.length === 0) return;

  const sections = Array.from(tocLinks).map(link => {
    const id = link.getAttribute('href').replace('#', '');
    return document.getElementById(id);
  }).filter(Boolean);

  window.addEventListener('scroll', () => {
    let currentId = '';
    const scrollPos = window.scrollY + 120;

    sections.forEach(section => {
      if (section.offsetTop <= scrollPos) {
        currentId = section.getAttribute('id');
      }
    });

    tocLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${currentId}`) {
        link.classList.add('active');
      }
    });
  });
}

/* ==========================================================================
   11. Mobile Menu Toggle
   ========================================================================== */
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobile-menu-toggle');
  const sidebar = document.querySelector('.sidebar');

  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener('click', () => {
      sidebar.classList.toggle('open');
    });
  }
}

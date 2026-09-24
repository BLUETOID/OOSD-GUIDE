# -*- coding: utf-8 -*-
"""
Assembles the complete 7marks.html file from Unit 1, Unit 2, and Unit 3 question modules.
"""

from scratch.gen_unit1 import get_unit1_questions
from scratch.gen_unit2 import get_unit2_questions
from scratch.gen_unit3 import get_unit3_questions

def build_html():
    u1 = get_unit1_questions()
    u2 = get_unit2_questions()
    u3 = get_unit3_questions()

    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>7/10-Mark Solved Long Answer Bank (2020–2026) | BCS054 Academic Guide</title>
  <meta name="description" content="All 52 comprehensive previous year 7 and 10 mark university questions for Units 1, 2, and 3 completely solved with full exam length, SVG vector diagrams, and C++ code.">
  <link rel="stylesheet" href="css/style.css">
  <script defer src="js/main.js"></script>
</head>
<body>
  <header class="app-header">
    <div class="header-container">
      <div class="brand">
        <span>OOSD.GUIDE</span>
        <span class="brand-badge">7/10-Marks Bank</span>
      </div>
      <nav class="nav-links">
        <a href="index.html">Index</a>
        <a href="short_theory.html">Short Theory</a>
        <a href="unit1.html">Unit 1 Theory</a>
        <a href="unit2.html">Unit 2 Theory</a>
        <a href="unit3.html">Unit 3 Theory</a>
        <a href="2marks.html">2-Marks Bank</a>
        <a href="7marks.html" class="active">7/10-Marks Bank</a>
      </nav>
    </div>
  </header>

  <main class="app-main">
    <section>
      <h1>Long Answer Question Bank (7 &amp; 10 Marks: 2020–2026)</h1>
      <p>Comprehensive, exam-grade solutions for all 52 university long-form questions across Units 1, 2, and 3. Each answer is developed to the full university length standard (350–750+ words), containing formal definitions, architectural rationale, hand-reproducible SVG vector diagrams (zero ASCII art), and production-grade C++ / C code implementations.</p>

      <!-- Filter Controls Toolbar -->
      <div class="toolbar">
        <div class="filter-group">
          <span class="filter-label">Unit:</span>
          <button class="filter-btn active" data-filter-type="unit" data-filter="all">All</button>
          <button class="filter-btn" data-filter-type="unit" data-filter="1">Unit 1</button>
          <button class="filter-btn" data-filter-type="unit" data-filter="2">Unit 2</button>
          <button class="filter-btn" data-filter-type="unit" data-filter="3">Unit 3</button>
        </div>
        <div class="filter-group">
          <span class="filter-label">Year:</span>
          <button class="filter-btn active" data-filter-type="year" data-filter="all">All</button>
          <button class="filter-btn" data-filter-type="year" data-filter="2020-21">20-21</button>
          <button class="filter-btn" data-filter-type="year" data-filter="2021-22">21-22</button>
          <button class="filter-btn" data-filter-type="year" data-filter="2022-23">22-23</button>
          <button class="filter-btn" data-filter-type="year" data-filter="2023-24">23-24</button>
          <button class="filter-btn" data-filter-type="year" data-filter="2024-25">24-25</button>
          <button class="filter-btn" data-filter-type="year" data-filter="2025-26">25-26</button>
        </div>
        <input type="text" id="search-input" class="search-input" placeholder="Search long answers (e.g., hospital, chatbot, vtable, JSD, cone)...">
        <span class="counter-badge" id="item-count">52 Questions</span>
      </div>

      <!-- ======================================================== -->
      <!-- UNIT 1 LONG QUESTIONS (15 QUESTIONS)                     -->
      <!-- ======================================================== -->
      <h2>Unit 1: Introduction to Object Orientation &amp; UML (Long Answers: 7 &amp; 10 Marks)</h2>
"""

    def render_question(q):
        return f"""
      <!-- {q['id']} -->
      <div class="question-item" data-unit="{q['unit']}" data-year="{q['year']}">
        <div class="question-header">
          <span class="q-badge">{q['id']}</span>
          <span class="question-title">{q['title']}</span>
          <span class="q-year">{q['year_display']}</span>
        </div>
        <div class="question-body">
{q['content'].strip()}
        </div>
      </div>
"""

    for q in u1:
        html += render_question(q)

    html += """
      <!-- ======================================================== -->
      <!-- UNIT 2 LONG QUESTIONS (20 QUESTIONS)                     -->
      <!-- ======================================================== -->
      <h2>Unit 2: Basic Structural, Behavioural &amp; Architectural Modeling (Long Answers: 7 &amp; 10 Marks)</h2>
"""

    for q in u2:
        html += render_question(q)

    html += """
      <!-- ======================================================== -->
      <!-- UNIT 3 LONG QUESTIONS (17 QUESTIONS)                     -->
      <!-- ======================================================== -->
      <h2>Unit 3: Object Oriented Analysis, Design &amp; Programming Style (Long Answers: 7 &amp; 10 Marks)</h2>
"""

    for q in u3:
        html += render_question(q)

    html += """
    </section>
  </main>

  <footer class="app-footer">
    <div class="footer-container">
      <div class="footer-col">
        <div class="brand">
          <span>OOSD.GUIDE</span>
          <span class="brand-badge">Academic Reference</span>
        </div>
        <p class="footer-desc">A rigorous academic guide and solved question bank for Object-Oriented System Design (BCS054 / KCS054), covering the complete university syllabus across Units 1, 2, and 3.</p>
      </div>
      <div class="footer-col">
        <h4>Core Modules</h4>
        <ul class="footer-links">
          <li><a href="index.html">Master Syllabus Matrix</a></li>
          <li><a href="short_theory.html">Short Theory Compendium</a></li>
          <li><a href="unit1.html">Unit 1: Object Orientation &amp; UML</a></li>
          <li><a href="unit2.html">Unit 2: Structural &amp; Behavioral Modeling</a></li>
          <li><a href="unit3.html">Unit 3: Analysis, Design &amp; Styles</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Question Banks</h4>
        <ul class="footer-links">
          <li><a href="2marks.html">2-Mark Solved Questions (All 30)</a></li>
          <li><a href="7marks.html">7/10-Mark Solved Questions (All 52)</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 OOSD Guide Portal. Object-Oriented System Design Academic Companion.</p>
    </div>
  </footer>
</body>
</html>
"""
    return html

if __name__ == "__main__":
    content = build_html()
    with open("7marks.html", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully generated 7marks.html ({len(content)} bytes).")


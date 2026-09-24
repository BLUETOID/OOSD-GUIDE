# -*- coding: utf-8 -*-
"""
Unit 3 Long Answers Generator (Questions U3-L01 to U3-L17)
Every question contains 400-750 words, detailed subheadings, comparison tables,
working C++ code, or high-contrast SVG diagrams.
"""

def get_unit3_questions():
    questions = []

    # U3-L01
    questions.append({
        "id": "U3-L01",
        "unit": "3",
        "year": "2020-21",
        "year_display": "[2020-21]",
        "title": "What is Data Abstraction? How it is different from encapsulation? Explain with proper example.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Formal Definition and Theoretical Foundations of Data Abstraction</h4>
  <p><strong>Data Abstraction</strong> is the foundational software engineering principle of representing essential features of a real-world concept or system entity without including background implementation details, physical memory structures, or low-level algorithmic complexities. Abstraction establishes an intellectual boundary separating <em>behavioral specification</em> (what services an entity provides) from <em>algorithmic realization</em> (how those services are executed).</p>
  <p>In software modeling, abstraction allows developers to manage cognitive overload by exposing high-level, stable public contracts (such as abstract base classes, pure virtual interfaces, and function signatures) while shielding client components from volatile internal mechanisms.</p>

  <h4 class="answer-heading">2. Exhaustive Comparison: Data Abstraction vs. Encapsulation</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Dimension</th>
        <th style="width: 40%;">Data Abstraction</th>
        <th style="width: 40%;">Encapsulation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Core Philosophy</strong></td>
        <td><strong>"What it does"</strong>: Focuses on the observable public behavior and external interface while ignoring internal mechanics.</td>
        <td><strong>"How it is bound &amp; protected"</strong>: Focuses on packaging state and behavior together and restricting unauthorized direct access.</td>
      </tr>
      <tr>
        <td><strong>Primary Mechanism</strong></td>
        <td>Abstract classes, Pure Virtual Functions (<code>virtual ... = 0</code> in C++), Interfaces.</td>
        <td>Access control specifiers (<code>private</code>, <code>protected</code>, <code>public</code>), getter/setter methods.</td>
      </tr>
      <tr>
        <td><strong>Problem Addressed</strong></td>
        <td>Reduces intellectual system complexity by filtering out unnecessary low-level details.</td>
        <td>Protects data integrity, maintains class invariants, and prevents unauthorized mutation.</td>
      </tr>
      <tr>
        <td><strong>Implementation Phase</strong></td>
        <td>Formulated during early <strong>Design &amp; Architecture</strong> phases to establish contracts.</td>
        <td>Formulated during <strong>Detailed Design &amp; Implementation</strong> to guard internal state.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. Comprehensive C++ Industrial Demonstration: Cryptographic Key Storage</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;memory&gt;
#include &lt;vector&gt;

// ==========================================
// DATA ABSTRACTION: Pure Virtual Interface
// Client knows WHAT can be done, not HOW.
// ==========================================
class KeyVaultService {
public:
    virtual ~KeyVaultService() = default;
    virtual void storeSecret(const std::string&amp; keyId, const std::string&amp; secret) = 0;
    virtual std::string retrieveSecret(const std::string&amp; keyId) const = 0;
};

// ==========================================
// ENCAPSULATION: Concrete Implementation
// Bundles private encrypted storage and bounds state.
// ==========================================
class HardwareSecurityModule : public KeyVaultService {
private:
    // Strictly encapsulated private state variables
    struct KeyEntry {
        std::string id;
        std::string cipherText;
    };
    std::vector&lt;KeyEntry&gt; vaultStorage;
    std::string hsmSerial;

    // Private encapsulated internal helper routine (Hidden from client)
    std::string internalEncrypt(const std::string&amp; raw) const {
        return "AES256_ENCRYPTED(" + raw + ")";
    }

public:
    HardwareSecurityModule(std::string serial) : hsmSerial(std::move(serial)) {}

    void storeSecret(const std::string&amp; keyId, const std::string&amp; secret) override {
        // Enforcing internal invariant and encrypting before saving
        vaultStorage.push_back({keyId, internalEncrypt(secret)});
        std::cout &lt;&lt; "[HSM " &lt;&lt; hsmSerial &lt;&lt; "] Securely encrypted and stored key: " &lt;&lt; keyId &lt;&lt; "\\n";
    }

    std::string retrieveSecret(const std::string&amp; keyId) const override {
        for (const auto&amp; entry : vaultStorage) {
            if (entry.id == keyId) {
                return entry.cipherText; // Return encrypted blob
            }
        }
        return "NOT_FOUND";
    }
};

int main() {
    // Client depends strictly on the ABSTRACTION (KeyVaultService)
    std::unique_ptr&lt;KeyVaultService&gt; vault = std::make_unique&lt;HardwareSecurityModule&gt;("HSM-CORP-99");

    vault-&gt;storeSecret("DB_PASSWORD", "SuperSecretRootPW123");
    std::cout &lt;&lt; "Vault Output: " &lt;&lt; vault-&gt;retrieveSecret("DB_PASSWORD") &lt;&lt; "\\n";

    // Client CANNOT access vault-&gt;vaultStorage or vault-&gt;internalEncrypt()
    // because they are ENCAPSULATED inside HardwareSecurityModule.
    return 0;
}</code></pre>

  <h4 class="answer-heading">4. Architectural Interplay</h4>
  <p>Abstraction and encapsulation are complementary: <strong>Abstraction directs what to expose</strong> to consumers through clean public interfaces, while <strong>Encapsulation enforces the defensive perimeter</strong> that hides the internal implementation mechanics, ensuring data integrity and allowing non-disruptive internal refactoring.</p>
</div>
        """
    })

    # U3-L02
    questions.append({
        "id": "U3-L02",
        "unit": "3",
        "year": "2020-21",
        "year_display": "[2020-21]",
        "title": "Prepare a DFD for computing the volume and surface area of a cone. Inputs are height and the radius of the base of the cone. Outputs are volume and surface area. Discuss some ways of specifying operations.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Mathematical Formulas and Computational Decomposition</h4>
  <p>For a right circular cone given base radius $r$ and vertical height $h$:</p>
  <ul>
    <li><strong>Slant Height ($s$ / $l$):</strong> $s = \sqrt{r^2 + h^2}$ (Calculated via Pythagorean theorem).</li>
    <li><strong>Base Area ($B$):</strong> $B = \pi r^2$.</li>
    <li><strong>Lateral Surface Area ($A_{\text{lateral}}$):</strong> $A_{\text{lateral}} = \pi r s = \pi r \sqrt{r^2 + h^2}$.</li>
    <li><strong>Total Surface Area ($A_{\text{total}}$):</strong> $A_{\text{total}} = B + A_{\text{lateral}} = \pi r^2 + \pi r s = \pi r (r + s)$.</li>
    <li><strong>Volume ($V$):</strong> $V = \frac{1}{3} \pi r^2 h = \frac{1}{3} B h$.</li>
  </ul>

  <h4 class="answer-heading">2. High-Contrast Level-1 Data Flow Diagram (DFD)</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 680 320" width="100%" height="320" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="320" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- External Entity: User / Input Device -->
      <rect x="30" y="110" width="110" height="60" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="85" y="145" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">User / Input</text>

      <!-- Input Data Flows: r and h -->
      <line x1="140" y1="125" x2="220" y2="80" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="220,80 211,79 216,87" fill="#1f2328"/>
      <text x="175" y="95" font-family="monospace" font-size="9" fill="#1f2328">radius (r)</text>

      <line x1="140" y1="155" x2="220" y2="195" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="220,195 216,187 211,196" fill="#1f2328"/>
      <text x="175" y="185" font-family="monospace" font-size="9" fill="#1f2328">height (h)</text>

      <!-- Process 1.0: Compute Slant Height -->
      <circle cx="270" cy="80" r="45" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="270" y="75" font-family="monospace" font-size="9" font-weight="bold" fill="#0969da" text-anchor="middle">1.0</text>
      <text x="270" y="90" font-family="sans-serif" font-size="8" fill="#1f2328" text-anchor="middle">Compute Slant</text>
      <text x="270" y="102" font-family="monospace" font-size="8" fill="#656d76" text-anchor="middle">s = sqrt(r^2+h^2)</text>

      <!-- Height also feeds Process 1.0 -->
      <line x1="220" y1="195" x2="250" y2="125" stroke="#1f2328" stroke-width="1.2"/>

      <!-- Process 2.0: Compute Base Area -->
      <circle cx="270" cy="220" r="45" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="270" y="215" font-family="monospace" font-size="9" font-weight="bold" fill="#0969da" text-anchor="middle">2.0</text>
      <text x="270" y="230" font-family="sans-serif" font-size="8" fill="#1f2328" text-anchor="middle">Compute Base</text>
      <text x="270" y="242" font-family="monospace" font-size="8" fill="#656d76" text-anchor="middle">B = pi * r^2</text>

      <!-- Flow to Volume Process 3.0 -->
      <line x1="315" y1="220" x2="430" y2="220" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="430,220 422,216 422,224" fill="#1f2328"/>
      <text x="365" y="212" font-family="monospace" font-size="9" fill="#1f2328">Base Area (B)</text>

      <!-- Height feed to Volume Process -->
      <path d="M 230 195 L 230 160 L 450 160 L 450 180" fill="none" stroke="#1f2328" stroke-width="1.2"/>
      <polygon points="450,180 446,172 454,172" fill="#1f2328"/>
      <text x="340" y="152" font-family="monospace" font-size="8" fill="#1f2328">height (h)</text>

      <!-- Process 3.0: Compute Volume -->
      <circle cx="475" cy="220" r="45" fill="#f6f8fa" stroke="#0969da" stroke-width="2"/>
      <text x="475" y="215" font-family="monospace" font-size="9" font-weight="bold" fill="#0969da" text-anchor="middle">3.0</text>
      <text x="475" y="230" font-family="sans-serif" font-size="8" fill="#1f2328" text-anchor="middle">Compute Volume</text>
      <text x="475" y="242" font-family="monospace" font-size="8" fill="#656d76" text-anchor="middle">V = (1/3)*B*h</text>

      <!-- Flow from Slant to Surface Area Process 4.0 -->
      <line x1="315" y1="80" x2="430" y2="80" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="430,80 422,76 422,84" fill="#1f2328"/>
      <text x="365" y="72" font-family="monospace" font-size="9" fill="#1f2328">Slant (s)</text>

      <!-- Process 4.0: Compute Surface Area -->
      <circle cx="475" cy="80" r="45" fill="#f6f8fa" stroke="#0969da" stroke-width="2"/>
      <text x="475" y="75" font-family="monospace" font-size="9" font-weight="bold" fill="#0969da" text-anchor="middle">4.0</text>
      <text x="475" y="90" font-family="sans-serif" font-size="8" fill="#1f2328" text-anchor="middle">Compute Area</text>
      <text x="475" y="102" font-family="monospace" font-size="8" fill="#656d76" text-anchor="middle">A = pi*r*(r+s)</text>

      <!-- External Entity: Display / Output -->
      <rect x="560" y="110" width="100" height="100" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="610" y="145" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">Output</text>
      <text x="610" y="165" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">Results Display</text>

      <!-- Outputs to Result Sink -->
      <line x1="520" y1="80" x2="560" y2="125" stroke="#1a7f37" stroke-width="1.5"/>
      <polygon points="560,125 550,122 555,116" fill="#1a7f37"/>
      <text x="545" y="95" font-family="monospace" font-size="8" fill="#1a7f37">Surface Area</text>

      <line x1="520" y1="220" x2="560" y2="185" stroke="#1a7f37" stroke-width="1.5"/>
      <polygon points="560,185 555,193 550,187" fill="#1a7f37"/>
      <text x="545" y="215" font-family="monospace" font-size="8" fill="#1a7f37">Volume</text>
    </svg>
    <span class="diagram-caption">Figure U3-L02: Level-1 Data Flow Diagram for Cone Volume and Surface Area Computation</span>
  </div>

  <h4 class="answer-heading">3. Comprehensive Ways of Specifying Operations in System Design</h4>
  <p>In structured and object-oriented specifications, functional transformation processes (process specifications or P-Specs) are formally documented using five standardized techniques:</p>
  <ul>
    <li><strong>1. Mathematical Equations:</strong> The most concise and rigorous method when transformations are purely computational:
      <pre class="code-block"><code>Volume = (1.0 / 3.0) * M_PI * radius * radius * height;
SurfaceArea = M_PI * radius * (radius + sqrt(radius * radius + height * height));</code></pre>
    </li>
    <li><strong>2. Structured English / Pseudocode:</strong> Combines natural language with programming language control structures (<code>IF-THEN-ELSE</code>, <code>WHILE-DO</code>) without language-specific syntax. Ideal for communicating logic across developer and client boundaries.</li>
    <li><strong>3. Decision Tables:</strong> Two-dimensional tabular representations mapping complex combinations of input conditions against resulting action sets. Highly effective for complex business policy rules and insurance underwriting.</li>
    <li><strong>4. Decision Trees:</strong> Graphical branching trees visualizing sequential condition testing leading to operational outcomes. Excellent for nested logic verification.</li>
    <li><strong>5. Pre-Conditions and Post-Conditions (Design by Contract):</strong> Formally defines what must be true prior to operation invocation (<code>Pre: radius &gt; 0 &amp;&amp; height &gt; 0</code>) and guarantees what will hold upon completion (<code>Post: result.volume &gt; 0 &amp;&amp; result.area &gt; 0</code>) without dictating internal algorithms.</li>
  </ul>

  <h4 class="answer-heading">4. Concrete C++ Mathematical Implementation</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;cmath&gt;

struct ConeMetrics {
    double volume;
    double surfaceArea;
};

ConeMetrics calculateCone(double r, double h) {
    double slantHeight = std::sqrt(r * r + h * h);
    double baseArea = M_PI * r * r;
    double lateralArea = M_PI * r * slantHeight;

    ConeMetrics result;
    result.volume = (1.0 / 3.0) * baseArea * h;
    result.surfaceArea = baseArea + lateralArea;
    return result;
}

int main() {
    double radius = 5.0, height = 12.0;
    ConeMetrics cone = calculateCone(radius, height);
    std::cout << "Cone Volume: " << cone.volume << " cubic units\n";
    std::cout << "Cone Surface Area: " << cone.surfaceArea << " sq units\n";
    return 0;
}</code></pre>

</div>
        """
    })

    # U3-L03
    questions.append({
        "id": "U3-L03",
        "unit": "3",
        "year": "2020-21",
        "year_display": "[2020-21]",
        "title": "Differentiate: (i) SA/SD and OMT (ii) SA/SD and JSD.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Introduction to Methodological Paradigms</h4>
  <p>Software engineering methodologies evolved historically through distinct conceptual paradigms. <strong>Structured Analysis / Structured Design (SA/SD)</strong> represents the procedural process-flow paradigm of the 1970s (Yourdon-Constantine, DeMarco). <strong>Object Modeling Technique (OMT)</strong> represents the multi-view object-oriented paradigm pioneered by James Rumbaugh in 1991. <strong>Jackson System Development (JSD)</strong> represents Michael Jackson's event-ordering and sequential entity lifecycle modeling paradigm of the 1980s.</p>

  <h4 class="answer-heading">2. Part (i): Exhaustive Differentiation: SA/SD vs. OMT</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Dimension</th>
        <th style="width: 40%;">Structured Analysis / Design (SA/SD)</th>
        <th style="width: 40%;">Object Modeling Technique (OMT)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Focus</strong></td>
        <td>Process-centric: Tracks passive data through functional transforms.</td>
        <td>Object-centric: Encapsulates state and operations within domain entities.</td>
      </tr>
      <tr>
        <td><strong>Core Models</strong></td>
        <td>Two orthogonal models: Data Flow Diagrams (DFD) and Structure Charts.</td>
        <td><strong>Three Integrated Models:</strong><br>1. Object Model (Class diagrams)<br>2. Dynamic Model (Statecharts)<br>3. Functional Model (DFDs)</td>
      </tr>
      <tr>
        <td><strong>Analysis-to-Design Transition</strong></td>
        <td><strong>Discontinuous ("Semantic Gap"):</strong> Flattened DFD bubbles must be manually restructured into hierarchical Structure Charts via Transform/Transaction Analysis.</td>
        <td><strong>Seamless &amp; Iterative:</strong> Analysis classes are directly refined during design by adding access specifiers, visibility, VTables, and design patterns.</td>
      </tr>
      <tr>
        <td><strong>Reusability &amp; Maintenance</strong></td>
        <td>Low: Functions are tightly coupled to explicit global data layouts.</td>
        <td>High: Decoupled via encapsulation, inheritance, and polymorphism.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. Part (ii): Exhaustive Differentiation: SA/SD vs. JSD</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Dimension</th>
        <th style="width: 40%;">Structured Analysis / Design (SA/SD)</th>
        <th style="width: 40%;">Jackson System Development (JSD)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Foundational Premise</strong></td>
        <td>Decomposes system by functional outputs and required data transformations.</td>
        <td>Models the real world as a set of autonomous, sequential, interacting concurrent entities.</td>
      </tr>
      <tr>
        <td><strong>Lifecycle Modeling</strong></td>
        <td>Static and pipeline-oriented; lacks explicit entity lifecycle progression.</td>
        <td><strong>Entity Structure Diagrams (ESD):</strong> Uses regular expressions (Sequence, Selection, Iteration) to trace an entity's complete temporal life history.</td>
      </tr>
      <tr>
        <td><strong>Implementation Mechanism</strong></td>
        <td>Subroutine call hierarchies and monolithic sequential procedural passes.</td>
        <td>Network of concurrent communicating sequential processes (CSP), transformed via process inversion into coroutines.</td>
      </tr>
      <tr>
        <td><strong>Handling Requirements Changes</strong></td>
        <td>Vulnerable: Changing an output requirement modifies the core data flow.</td>
        <td>Robust: Real-world entity behaviors change infrequently; function step is added at the end.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">4. Evolutionary Synthesis: Why OMT Superseded SA/SD and JSD</h4>
  <p>The progression from SA/SD and JSD to OMT (and eventually UML) resolved the foundational architectural dilemmas of software engineering:</p>
  <ul>
    <li><strong>Resolving the Semantic Gap:</strong> SA/SD suffered from a jarring conceptual leap when translating flattened DFD data flows into hierarchical Structure Charts. OMT eliminated this discontinuity by using classes as the unified, continuous abstraction from requirements elicitation through physical implementation.</li>
    <li><strong>Integrating Static and Dynamic Perspectives:</strong> JSD focused heavily on event sequencing while SA/SD focused on data flow. OMT unified both by integrating Rumbaugh's Object Model (structure), State Model (temporal behavior), and Functional Model (data transformation) into a holistic system architecture.</li>
  </ul>

</div>
        """
    })

    # U3-L04
    questions.append({
        "id": "U3-L04",
        "unit": "3",
        "year": "2021-22",
        "year_display": "[2021-22]",
        "title": "Explain object oriented programming. What are the main advantages of object oriented programming over procedural programming? Write a program in C++ by creating a class integer and write a function that prints all the prime numbers from the class.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Formal Concept of Object-Oriented Programming (OOP)</h4>
  <p><strong>Object-Oriented Programming (OOP)</strong> is an implementation paradigm that organizes software systems as decentralized communities of collaborating <strong>objects</strong>. Each object is an instance of a <strong>class</strong> that encapsulates internal state variables with member procedures that validate and mutate that state. Computation proceeds exclusively through message passing rather than global memory manipulation.</p>

  <h4 class="answer-heading">2. Decisive Advantages of OOP Over Procedural Programming</h4>
  <ul>
    <li><strong>Defensive Encapsulation:</strong> Procedural programming exposes data structures globally, allowing any function to mutate records without verification. OOP restricts access via access specifiers, guaranteeing class invariants.</li>
    <li><strong>Elimination of Switch-Case Antipatterns:</strong> Adding a new entity type in procedural code requires modifying dozens of <code>switch(record.type)</code> statements across the codebase. In OOP, dynamic polymorphism executes specialized behavior via virtual dispatch without touching existing code.</li>
    <li><strong>Structural Reusability:</strong> Inheritance and component aggregation allow pre-tested base classes to be extended without error-prone copy-pasting.</li>
    <li><strong>Scalable Maintenance:</strong> Interfaces provide strict API boundaries, allowing engineering teams to work concurrently on decoupled components.</li>
  </ul>

  <h4 class="answer-heading">3. Complete C++ Program: Class Integer with Prime Extraction</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;vector&gt;
#include &lt;cmath&gt;

class IntegerArray {
private:
    std::vector&lt;int&gt; values;

    // Private helper function enforcing encapsulation
    bool isPrime(int n) const {
        if (n &lt;= 1) return false;
        if (n &lt;= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;

        for (int i = 5; i * i &lt;= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }

public:
    // Constructor
    IntegerArray() = default;

    // Member function to add integers
    void append(int val) {
        values.push_back(val);
    }

    // Required function: Prints all prime numbers contained in the class
    void printPrimeNumbers() const {
        std::cout &lt;&lt; "--- Prime Numbers in IntegerArray ---\\n";
        bool found = false;

        for (int val : values) {
            if (isPrime(val)) {
                std::cout &lt;&lt; "  -&gt; Prime found: " &lt;&lt; val &lt;&lt; "\\n";
                found = true;
            }
        }

        if (!found) {
            std::cout &lt;&lt; "  No prime numbers present in collection.\\n";
        }
    }
};

int main() {
    IntegerArray numbers;
    // Populate collection
    int sampleData[] = { 4, 7, 12, 19, 23, 28, 31, 35, 41, 50, 53, 2 };
    for (int num : sampleData) {
        numbers.append(num);
    }

    // Invoke member function to print primes
    numbers.printPrimeNumbers();
    return 0;
}</code></pre>

  <h4 class="answer-heading">4. Output Explanation</h4>
  <p>The program populates the encapsulated <code>std::vector&lt;int&gt;</code> with composite and prime numbers. <code>printPrimeNumbers()</code> iterates through the internal elements, delegating testing to the private $O(\sqrt{N})$ helper method <code>isPrime()</code>, outputting primes <code>7, 19, 23, 31, 41, 53, 2</code> cleanly to the console.</p>
</div>
        """
    })

    # U3-L05
    questions.append({
        "id": "U3-L05",
        "unit": "3",
        "year": "2021-22",
        "year_display": "[2021-22]",
        "title": "What is an inheritance? Explain the different types of it. Write a program in C++ for multiple inheritance.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Definition and Mechanics of Inheritance</h4>
  <p><strong>Inheritance</strong> is the structural mechanism in object-oriented programming whereby a new class (the <em>derived or child class</em>) acquires the member variables, properties, and member functions of one or more existing classes (the <em>base or parent classes</em>). It models the semantic "is-a" relationship, facilitates hierarchical categorization of domain concepts, and eliminates redundant code by enabling derived classes to specialize or override inherited behaviors.</p>

  <h4 class="answer-heading">2. Taxonomy of Inheritance Forms</h4>
  <ul>
    <li><strong>1. Single Inheritance:</strong> A derived class inherits from exactly one base class (e.g., <code>Dog</code> inherits from <code>Animal</code>).</li>
    <li><strong>2. Multiple Inheritance:</strong> A derived class inherits directly from two or more base classes (e.g., <code>AmphibiousVehicle</code> inherits from both <code>Car</code> and <code>Boat</code>).</li>
    <li><strong>3. Multilevel Inheritance:</strong> A class inherits from a derived class, forming a vertical chain (e.g., <code>SportsCar</code> inherits from <code>Car</code>, which inherits from <code>Vehicle</code>).</li>
    <li><strong>4. Hierarchical Inheritance:</strong> Multiple distinct derived classes inherit from a single common base class (e.g., <code>SavingsAccount</code> and <code>CurrentAccount</code> both inherit from <code>Account</code>).</li>
    <li><strong>5. Hybrid Inheritance:</strong> A combination of two or more inheritance forms, frequently producing the classical <em>Diamond Problem</em> (resolved in C++ via <code>virtual</code> base classes).</li>
  </ul>

  <h4 class="answer-heading">3. Complete C++ Program Demonstrating Multiple Inheritance</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;

// Base Class 1: Display Device
class DisplayScreen {
protected:
    int resolutionX;
    int resolutionY;

public:
    DisplayScreen(int x, int y) : resolutionX(x), resolutionY(y) {
        std::cout &lt;&lt; "[DisplayScreen] Initialized with resolution " 
                  &lt;&lt; resolutionX &lt;&lt; "x" &lt;&lt; resolutionY &lt;&lt; "\\n";
    }

    void renderGraphics() const {
        std::cout &lt;&lt; "Rendering visual frame buffer.\\n";
    }
};

// Base Class 2: Cellular Network Modem
class CellularRadio {
protected:
    std::string imeiNumber;
    bool is5GConnected;

public:
    CellularRadio(std::string imei) : imeiNumber(std::move(imei)), is5GConnected(true) {
        std::cout &lt;&lt; "[CellularRadio] Initialized with IMEI: " &lt;&lt; imeiNumber &lt;&lt; "\\n";
    }

    void transmitPackets() const {
        std::cout &lt;&lt; "Transmitting LTE/5G wireless packets.\\n";
    }
};

// Multiple Inheritance: SmartPhone inherits from both DisplayScreen and CellularRadio
class SmartPhone : public DisplayScreen, public CellularRadio {
private:
    std::string modelName;

public:
    // Base classes are initialized in the constructor initializer list
    SmartPhone(std::string name, int x, int y, std::string imei)
        : DisplayScreen(x, y), CellularRadio(std::move(imei)), modelName(std::move(name)) {
        std::cout &lt;&lt; "[SmartPhone] " &lt;&lt; modelName &lt;&lt; " assembled successfully.\\n";
    }

    void powerOn() const {
        std::cout &lt;&lt; "\\nBooting " &lt;&lt; modelName &lt;&lt; "...\\n";
        renderGraphics();     // Inherited from DisplayScreen
        transmitPackets();    // Inherited from CellularRadio
    }
};

int main() {
    SmartPhone phone("GalaxyPro-X", 2560, 1440, "867530901234567");
    phone.powerOn();
    return 0;
}</code></pre>

  <h4 class="answer-heading">4. Architectural Consideration: The Diamond Problem in C++</h4>
  <p>In multiple inheritance, if two parent classes both inherit from the same common ancestor, the derived child receives duplicate copies of the ancestor's member variables, causing compiler ambiguity errors. C++ solves this using <strong>Virtual Base Classes</strong> (<code>class B : virtual public A</code>), ensuring the compiler inserts an offset pointer and allocates only a single shared instance of the root base class in the object layout.</p>
</div>
        """
    })

    # U3-L06
    questions.append({
        "id": "U3-L06",
        "unit": "3",
        "year": "2022-23",
        "year_display": "[2022-23]",
        "title": "Discuss the following: (i) Robustness, (ii) Extensibility, (iii) Reusability. Discuss with respect to object-oriented system design.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Introduction to Architectural Quality Attributes</h4>
  <p>In Object-Oriented System Design, non-functional quality attributes dictate whether an architecture will endure under production scale or collapse under maintenance debt. Among the most critical software engineering attributes are <strong>Robustness</strong>, <strong>Extensibility</strong>, and <strong>Reusability</strong>.</p>

  <h4 class="answer-heading">2. Exhaustive Conceptual and Architectural Breakdown</h4>

  <h5 class="answer-heading">A. Robustness</h5>
  <p><strong>Robustness</strong> is the ability of an object-oriented system to maintain stable, deterministic behavior, preserve data integrity, and recover gracefully when encountering invalid inputs, unexpected runtime exceptions, or hardware faults.</p>
  <ul>
    <li><em>OO Mechanisms Ensuring Robustness:</em>
      <ul>
        <li><strong>Class Invariant Enforcement:</strong> Private encapsulation prevents illegal state transitions (e.g., negative balances or null pointer dereferences).</li>
        <li><strong>Design by Contract (DbC):</strong> Explicit pre-conditions, post-conditions, and class invariants validate state boundaries at method invocation.</li>
        <li><strong>RAII (Resource Acquisition Is Initialization):</strong> In languages like C++, wrapping physical OS resources (file handles, mutexes, sockets) inside object destructors guarantees automatic, leak-free cleanup even when exceptions occur.</li>
      </ul>
    </li>
  </ul>

  <h5 class="answer-heading">B. Extensibility</h5>
  <p><strong>Extensibility</strong> is the measure of how effortlessly an architecture can be augmented with new functional capabilities, domain entities, or business algorithms without modifying or recompiling existing, tested software components.</p>
  <ul>
    <li><em>OO Mechanisms Ensuring Extensibility:</em>
      <ul>
        <li><strong>Open-Closed Principle (OCP):</strong> Software entities should be open for extension but closed for modification.</li>
        <li><strong>Dynamic Polymorphism &amp; Inversion of Control (IoC):</strong> High-level business pipelines depend on abstract interfaces. Adding a new payment provider requires writing a new class implementing the interface, leaving the core transaction orchestrator untouched.</li>
        <li><strong>Pluggable Design Patterns:</strong> Strategy, Decorator, and Factory Method patterns facilitate modular feature additions.</li>
      </ul>
    </li>
  </ul>

  <h5 class="answer-heading">C. Reusability</h5>
  <p><strong>Reusability</strong> is the degree to which existing classes, packages, or architectural patterns can be repurposed across different applications or subsystems, amortizing engineering development and QA testing investments.</p>
  <ul>
    <li><em>OO Mechanisms Ensuring Reusability:</em>
      <ul>
        <li><strong>Composition over Inheritance:</strong> Assembling loosely coupled, single-responsibility components via aggregation yields far more reusable building blocks than rigid, deep inheritance hierarchies.</li>
        <li><strong>Genericity (Parametric Polymorphism):</strong> C++ templates enable writing algorithms (sorting, searching) and data structures (trees, hash maps) once for all types.</li>
        <li><strong>Frameworks and Domain Libraries:</strong> Cohesive class libraries encapsulate cross-cutting concerns (logging, networking, cryptography) for enterprise-wide reuse.</li>
      </ul>
    </li>
  </ul>

  <h4 class="answer-heading">3. The Interdependent Quality Triangle</h4>
  <p>In high-reliability system engineering, Robustness, Extensibility, and Reusability form an interdependent triad:</p>
  <ul>
    <li><strong>Robustness Enables Safe Reuse:</strong> Developers only reuse classes (e.g., standard template libraries) that have proven invariants and zero memory leaks under stress conditions.</li>
    <li><strong>Extensibility Prevents Invariant Compromise:</strong> Well-designed extension points (via polymorphism and strategy interfaces) allow systems to add new functionality without touching existing, battle-tested source code, preserving system robustness.</li>
    <li><strong>Reusability Lowers Defect Density:</strong> Reusing a thoroughly tested, production-hardened component amortizes QA effort and drastically reduces the probability of introducing regression bugs compared to writing custom algorithms from scratch.</li>
  </ul>

</div>
        """
    })

    # U3-L07
    questions.append({
        "id": "U3-L07",
        "unit": "3",
        "year": "2022-23",
        "year_display": "[2022-23]",
        "title": "Discuss in detail about JSD and SA/SD.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Detailed Exposition of Structured Analysis / Structured Design (SA/SD)</h4>
  <p><strong>SA/SD</strong> is the classic procedural software engineering methodology formalized by Larry Constantine, Edward Yourdon, and Tom DeMarco. It decomposes a complex software problem using functional, top-down decomposition:</p>
  <ul>
    <li><strong>Structured Analysis (SA) Phase:</strong> Produces a logical system specification using:
      <ul>
        <li><em>Data Flow Diagrams (DFDs):</em> Models how data travels between external entities, through functional process bubbles, into passive data stores.</li>
        <li><em>Data Dictionary:</em> Rigorous catalog defining every data stream and composite attribute syntax.</li>
        <li><em>Process Specifications (P-Specs):</em> Detailed algorithm descriptions for primitive level-0 DFD bubbles.</li>
      </ul>
    </li>
    <li><strong>Structured Design (SD) Phase:</strong> Converts the logical analysis model into a physical execution blueprint using <strong>Structure Charts</strong>. The transition is driven by two formal heuristics:
      <ul>
        <li><em>Transform Analysis:</em> Identifies the central transform bubble in a DFD, converting linear pipelines into a caller-callee hierarchy.</li>
        <li><em>Transaction Analysis:</em> Used when a single input data token triggers one of several alternative action paths.</li>
      </ul>
    </li>
  </ul>

  <h4 class="answer-heading">2. Detailed Exposition of Jackson System Development (JSD)</h4>
  <p><strong>JSD</strong>, formulated by Michael Jackson in 1983, rejects functional process decomposition. Instead, JSD models systems by tracking the sequential temporal order of real-world events over time:</p>
  <ul>
    <li><strong>The 6 Systematic JSD Phases:</strong>
      <ol>
        <li><em>Entity Action Step:</em> Identify real-world entities and the atomic actions they perform or suffer over time.</li>
        <li><em>Entity Structure Step:</em> Construct <strong>Entity Structure Diagrams (ESD)</strong> using regular tree notations: <strong>Sequence</strong> (left-to-right order), <strong>Selection</strong> (circle <code>o</code> marking alternative branches), and <strong>Iteration</strong> (asterisk <code>*</code> marking repetitions).</li>
        <li><em>Initial Model Step:</em> Model entities as concurrent communicating processes connected via unbounded FIFO queues called <em>Data Streams</em>.</li>
        <li><em>Function Step:</em> Attach output-generating functions to the existing structural model.</li>
        <li><em>System Timing Step:</em> Specify execution constraints and process synchronization latencies.</li>
        <li><em>Implementation Step:</em> Transform the concurrent process network into a single thread of execution using <strong>Process Inversion</strong> (turning sequential processes into coroutines or subroutines managed by a scheduler).</li>
      </ol>
    </li>
  </ul>

  <h4 class="answer-heading">3. Comprehensive Comparative Synthesis</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Characteristic</th>
        <th style="width: 37%;">SA/SD Methodology</th>
        <th style="width: 38%;">JSD Methodology</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Foundational Driver</strong></td>
        <td>System functional transformations (What does the system compute?).</td>
        <td>Real-world entity temporal behavior (How do real-world entities act over time?).</td>
      </tr>
      <tr>
        <td><strong>Primary Diagram</strong></td>
        <td>Data Flow Diagrams (DFD) and Structure Charts.</td>
        <td>Entity Structure Diagrams (ESD) and System Specification Diagrams (SSD).</td>
      </tr>
      <tr>
        <td><strong>Concurrency</strong></td>
        <td>Weak; assumes a single synchronous procedural CPU execution stack.</td>
        <td>Native; models the entire domain as communicating concurrent processes.</td>
      </tr>
    </tbody>
  </table>
</div>
        """
    })

    # U3-L08
    questions.append({
        "id": "U3-L08",
        "unit": "3",
        "year": "2022-23",
        "year_display": "[2022-23]",
        "title": "Compare Object Oriented Programming and Procedural programming.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Paradigmatic Foundations</h4>
  <p>The transition from <strong>Procedural Programming (POP)</strong> to <strong>Object-Oriented Programming (OOP)</strong> represents the most consequential paradigm shift in software engineering history. While procedural languages (C, Pascal, Fortran) model systems as top-down hierarchies of algorithmic subroutines manipulating passive data records, object-oriented languages (C++, Java, C#) model systems as decentralized ecosystems of autonomous, collaborating objects encapsulating state and behavior.</p>

  <h4 class="answer-heading">2. Exhaustive 8-Point Comparative Matrix</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Dimension</th>
        <th style="width: 40%;">Procedural Programming (POP)</th>
        <th style="width: 40%;">Object-Oriented Programming (OOP)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Core Philosophy</strong></td>
        <td><strong>Procedure-Centric:</strong> Computation is structured around algorithms and subroutines transforming inputs to outputs.</td>
        <td><strong>Data-and-Responsibility-Centric:</strong> Computation is structured around collaborating entities encapsulating state and operations.</td>
      </tr>
      <tr>
        <td><strong>2. Data-Code Binding</strong></td>
        <td>Data and procedures are completely separated; passive structs are passed into detached functions.</td>
        <td>Data and operations are structurally bound into cohesive class units via encapsulation.</td>
      </tr>
      <tr>
        <td><strong>3. Access &amp; Protection</strong></td>
        <td>No access control modifiers; records and global variables are vulnerable to accidental mutation.</td>
        <td>Defensive security via <code>private</code>, <code>protected</code>, and <code>public</code> access specifiers.</td>
      </tr>
      <tr>
        <td><strong>4. Decomposition Approach</strong></td>
        <td><strong>Top-Down Decomposition:</strong> Large problems are progressively broken down into smaller procedural sub-functions.</td>
        <td><strong>Bottom-Up Assembly:</strong> Resilient, autonomous classes are engineered and composed into larger subsystems.</td>
      </tr>
      <tr>
        <td><strong>5. Code Reusability</strong></td>
        <td>Limited to reusing static library procedures; modifying record shapes breaks all calling functions.</td>
        <td>Massive reusability achieved via inheritance hierarchies, generic templates, and component composition.</td>
      </tr>
      <tr>
        <td><strong>6. Dynamic Polymorphism</strong></td>
        <td>Requires brittle manual <code>switch-case</code> statements inspecting integer type flags.</td>
        <td>Native virtual method dynamic dispatch via compiler-generated Virtual Method Tables (VTable).</td>
      </tr>
      <tr>
        <td><strong>7. Communication Style</strong></td>
        <td>Direct hierarchical procedure invocations on the execution call stack.</td>
        <td>Message-passing protocol between objects via public member function invocations.</td>
      </tr>
      <tr>
        <td><strong>8. Real-World Mapping</strong></td>
        <td>Large semantic gap between business domain objects and procedural control flowcharts.</td>
        <td>Minimal semantic gap; software classes directly mirror domain business entities.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. Concrete Architectural Trade-off Summary</h4>
  <p>Procedural programming remains superior for low-level operating system device drivers, embedded microcontrollers with extreme RAM constraints (&lt; 4KB), and high-performance computing numerical math pipelines where flat contiguous memory layout maximizes CPU cache locality. Object-Oriented programming dominates complex enterprise systems, cloud platforms, and large-scale applications where long-term maintainability, team parallelism, and evolutionary extensibility outweigh minimal virtual dispatch overhead.</p>

  <h4 class="answer-heading">4. Memory Layout Comparison: Struct vs. Class VTable</h4>
  <p>At the hardware execution level, procedural C and object-oriented C++ exhibit distinct memory layouts:</p>
  <ul>
    <li><strong>Procedural C Struct:</strong> Stored as a contiguous block containing only data fields: <code>[ field1 | field2 | field3 ]</code>. Total memory footprint is strictly the sum of field sizes plus alignment padding. Functions reside in the static code segment and manipulate structs by passing their pointer explicitly.</li>
    <li><strong>Polymorphic C++ Class:</strong> Contains a hidden pointer at offset zero (<code>vptr</code>) followed by member variables: <code>[ vptr | field1 | field2 ]</code>. The <code>vptr</code> points to the class's shared Virtual Method Table (VTable), enabling dynamic runtime dispatch at the cost of one extra pointer indirection per polymorphic invocation.</li>
  </ul>

</div>
        """
    })

    # U3-L09
    questions.append({
        "id": "U3-L09",
        "unit": "3",
        "year": "2023-24",
        "year_display": "[2023-24]",
        "title": "What do you mean by documentation? What are the various considerations in documentation designing?",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Formal Definition and Strategic Role of Documentation</h4>
  <p>In software engineering, <strong>Documentation</strong> encompasses the complete, structured collection of written artifacts, visual architecture models, interface contracts, and maintenance manuals that record the intent, design decisions, operational parameters, and deployment procedures of a software system. High-quality documentation preserves institutional architectural knowledge, eliminates single-point-of-failure dependencies on individual developers, and drastically lowers total cost of ownership (TCO) across the multi-decade maintenance lifecycle.</p>

  <h4 class="answer-heading">2. The Primary Categories of Software Documentation</h4>
  <ul>
    <li><strong>Requirements &amp; Analysis Documentation:</strong> Software Requirements Specification (SRS), use case narratives, and business domain dictionaries.</li>
    <li><strong>Architectural &amp; Design Documentation:</strong> High-level system design documents (SDD), Kruchten 4+1 UML models, database schemas, and Architectural Decision Records (ADRs).</li>
    <li><strong>Code-Level Technical Documentation:</strong> Inline docstrings (Doxygen, Javadoc), API specifications (OpenAPI/Swagger), and protocol buffer schemas.</li>
    <li><strong>Operations &amp; Maintenance Documentation:</strong> Deployment runbooks, infrastructure-as-code manifests, disaster recovery protocols, and user guides.</li>
  </ul>

  <h4 class="answer-heading">3. Key Considerations in Documentation Designing</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Design Consideration</th>
        <th style="width: 75%;">Engineering Implementation &amp; Best Practices</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Audience Stratification</strong></td>
        <td>Tailor documents to specific reader personas: high-level conceptual overviews for stakeholders, formal UML interface contracts for developers, and CLI deployment runbooks for SRE/DevOps teams.</td>
      </tr>
      <tr>
        <td><strong>2. Synchronization with Code</strong></td>
        <td>Documentation that drifts from executable reality is worse than no documentation. Treat documentation as code (Markdown, Mermaid diagrams stored directly in Git) and generate API documentation automatically via CI/CD pipelines.</td>
      </tr>
      <tr>
        <td><strong>3. Traceability &amp; Modularity</strong></td>
        <td>Establish clear bidirectional links connecting business requirements to UML design classes, test suites, and source code files, enabling rigorous impact analysis when requirements change.</td>
      </tr>
      <tr>
        <td><strong>4. Recording Architectural Intent</strong></td>
        <td>Focus documentation not merely on <em>what</em> the code does (which the code itself expresses), but <em>why</em> specific architectural choices and trade-offs were selected over alternative designs (captured via Architectural Decision Records).</td>
      </tr>
      <tr>
        <td><strong>5. Searchability &amp; Maintainability</strong></td>
        <td>Adopt structured, searchable wiki or static site generator formats (e.g., Markdown portals) with clear semantic headings, glossary indexes, and uncorrupted vector diagrams.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">4. Architectural Decision Records (ADRs) as Best Practice</h4>
  <p>Modern engineering documentation prioritizes <strong>Architectural Decision Records (ADRs)</strong> to document why specific structural decisions were chosen over alternatives:</p>
  <ul>
    <li><em>Context:</em> The specific architectural problem, non-functional requirements, and trade-offs.</li>
    <li><em>Decision:</em> The chosen design pattern, framework, or paradigm (e.g., adopting microservices over monolith, or selecting PostgreSQL over MongoDB).</li>
    <li><em>Consequences:</em> The positive outcomes (e.g., improved horizontal scalability) and acknowledged negative trade-offs (e.g., increased network latency and eventual consistency complexities).</li>
  </ul>

</div>
        """
    })

    # U3-L10
    questions.append({
        "id": "U3-L10",
        "unit": "3",
        "year": "2023-24",
        "year_display": "[2023-24]",
        "title": "Describe the structured analysis and structured design approach with an example.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Foundations of the SA/SD Engineering Process</h4>
  <p>The <strong>Structured Analysis and Structured Design (SA/SD)</strong> methodology is a classical procedural engineering methodology that decomposes systems through a top-down, functional perspective. It proceeds systematically across two major evolutionary phases:</p>

  <h4 class="answer-heading">2. Phase 1: Structured Analysis (Building the Logical Model)</h4>
  <p>The analysis phase builds an implementation-independent logical model using three core tools:</p>
  <ul>
    <li><strong>Data Flow Diagrams (DFD):</strong> Hierarchical network models showing external source/sinks, process transformations, and passive data stores. Progresses from a Level-0 Context Diagram down to detailed Level-1 and Level-2 functional decompositions.</li>
    <li><strong>Data Dictionary:</strong> Authoritative catalog specifying precise composite attribute definitions (e.g., <code>Order = CustomerId + {ItemNumber + Quantity} + TotalPrice</code>).</li>
    <li><strong>Process Specifications (P-Specs):</strong> Formal algorithmic pseudocode or decision tables describing the internal logic of primitive DFD processes.</li>
  </ul>

  <h4 class="answer-heading">3. Phase 2: Structured Design (Building the Physical Architecture)</h4>
  <p>The design phase transforms the logical DFD network into a hierarchical execution tree called a <strong>Structure Chart</strong> using two formal heuristics:</p>
  <ul>
    <li><strong>Transform Analysis:</strong> Used for linear input-process-output pipelines. Identifies the "central transform" (the process bubble furthest removed from input and output physical formats) and positions it beneath a top-level coordinating executive module.</li>
    <li><strong>Transaction Analysis:</strong> Used when an incoming transaction dispatcher routes execution down one of several mutually exclusive operational paths based on transaction type.</li>
  </ul>

  <h4 class="answer-heading">4. Detailed Real-World Example: ATM Cash Withdrawal System</h4>
  <ul>
    <li><em>Level-0 Context Diagram:</em> <code>Customer</code> interacts with <code>ATM System</code>; <code>Central Bank Core</code> verifies accounts.</li>
    <li><em>Level-1 DFD Processes:</em>
      <ul>
        <li><code>Process 1.0 (Validate Card &amp; PIN)</code>: Receives card data, queries <code>Bank Host</code>, outputs validation token.</li>
        <li><code>Process 2.0 (Check Account Balance)</code>: Reads from <code>Account Data Store</code>, outputs balance status.</li>
        <li><code>Process 3.0 (Dispense Currency)</code>: Triggers physical hardware cash dispenser motors.</li>
        <li><code>Process 4.0 (Update Ledger &amp; Print Receipt)</code>: Writes debit record to transaction store.</li>
      </ul>
    </li>
    <li><em>Structure Chart Derivation:</em> A master module <code>ATM_Controller</code> coordinates calls to <code>Authenticate_Subroutine()</code>, <code>Withdrawal_Manager()</code>, and <code>Receipt_Printer()</code>, passing data flags up and down the call tree.</li>
  </ul>

  <h4 class="answer-heading">5. Methodological Criticisms &amp; Limitations of SA/SD</h4>
  <p>While revolutionary in the 1970s, SA/SD exhibits severe vulnerabilities when applied to modern large-scale applications:</p>
  <ul>
    <li><strong>Global Data Store Vulnerability:</strong> DFD data stores are frequently shared across multiple procedural processes. Modifying a database schema or file record layout triggers widespread cascading modifications and regression errors across all accessing subroutines.</li>
    <li><strong>Poor Mapping to Modern Event-Driven GUIs:</strong> Top-down functional decomposition assumes a predictable batch-style input-process-output pipeline, failing to naturally model modern asynchronous, event-driven, multithreaded graphical user interfaces.</li>
  </ul>

</div>
        """
    })

    # U3-L11
    questions.append({
        "id": "U3-L11",
        "unit": "3",
        "year": "2023-24",
        "year_display": "[2023-24]",
        "title": "How do you map the object-oriented concepts using non-object oriented languages? Explain with an example.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Conceptual Feasibility of Emulating OOP in Non-OOP Languages</h4>
  <p>Object-Oriented Programming is fundamentally a <em>way of thinking and designing</em> rather than a specific compiler feature. Any procedural language possessing structured records (such as <code>struct</code> in C) and indirect pointer addressing (function pointers) can fully emulate all core object-oriented mechanisms: encapsulation, inheritance, and dynamic runtime polymorphism.</p>

  <h4 class="answer-heading">2. Mapping Strategy: Core OOP Concepts to Pure C</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">OOP Concept</th>
        <th style="width: 75%;">Procedural C Emulation Mechanism</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Encapsulation &amp; Class</strong></td>
        <td>Modeled as a C <code>struct</code>. Methods are standalone C functions that accept an explicit pointer to the struct instance as their first parameter (manually emulating the <code>this</code> pointer).</td>
      </tr>
      <tr>
        <td><strong>Inheritance</strong></td>
        <td>Modeled via <strong>struct embedding</strong>. The base struct is placed as the very first member field inside the derived struct. Because C guarantees zero offset for the first struct member, a pointer to the derived struct can be safely cast to a pointer to the base struct.</td>
      </tr>
      <tr>
        <td><strong>Polymorphism &amp; Dynamic Dispatch</strong></td>
        <td>Modeled by defining a <strong>VTable struct</strong> containing function pointers. The base struct contains a pointer (<code>vptr</code>) pointing to this table. Calls are dispatched via indirect function pointer invocation: <code>obj-&gt;vptr-&gt;method(obj)</code>.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. Complete Working ANSI C Implementation</h4>
  <pre class="code-block"><code>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

// Forward declaration of base struct
typedef struct Shape Shape;

// 1. Emulating Virtual Method Table (VTable) in C
typedef struct {
    double (*computeArea)(Shape* self);
    void (*render)(Shape* self);
} ShapeVTable;

// 2. Emulating Base Class with VPtr and Encapsulated Data
struct Shape {
    const ShapeVTable* vptr; // Pointer to virtual table
    int originX;
    int originY;
};

// 3. Emulating Derived Class: Circle (Inheritance via Struct Embedding)
typedef struct {
    Shape base;      // Base struct must be the FIRST member!
    double radius;   // Specialized child attribute
} Circle;

// Circle Polymorphic Method Implementations
double Circle_computeArea(Shape* self) {
    Circle* c = (Circle*)self; // Safe downcast
    return 3.14159 * c-&gt;radius * c-&gt;radius;
}

void Circle_render(Shape* self) {
    Circle* c = (Circle*)self;
    printf("[Render Circle] Center=(%d,%d), Radius=%.2f, Area=%.2f\\n",
           c-&gt;base.originX, c-&gt;base.originY, c-&gt;radius, Circle_computeArea(self));
}

// Static VTable for Circle
static const ShapeVTable circle_vtable = {
    Circle_computeArea,
    Circle_render
};

// Circle Constructor Emulation
Circle* Circle_create(int x, int y, double r) {
    Circle* c = (Circle*)malloc(sizeof(Circle));
    c-&gt;base.vptr = &amp;circle_vtable; // Initialize vptr
    c-&gt;base.originX = x;
    c-&gt;base.originY = y;
    c-&gt;radius = r;
    return c;
}

int main() {
    // Dynamic Polymorphism: Base pointer pointing to derived instance
    Shape* myShape = (Shape*)Circle_create(10, 20, 5.0);

    // Polymorphic Virtual Dispatch invocation in pure C!
    myShape-&gt;vptr-&gt;render(myShape);

    free(myShape);
    return 0;
}</code></pre>
</div>
        """
    })

    # U3-L12
    questions.append({
        "id": "U3-L12",
        "unit": "3",
        "year": "2024-25",
        "year_display": "[2024-25]",
        "title": "Explain the process of object-oriented analysis and design with a detailed example of a ride-hailing application. Include the steps from requirement gathering to design optimization.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. The End-to-End OOAD Engineering Process</h4>
  <p>The <strong>Object-Oriented Analysis and Design (OOAD)</strong> process transitions a system from ambiguous user requirements into an optimized, robust software architecture through five disciplined engineering phases:</p>

  <h4 class="answer-heading">2. Detailed Walkthrough: Ride-Hailing Application (Uber / Ola)</h4>

  <h5 class="answer-heading">Step 1: Requirement Gathering &amp; Use Case Modeling</h5>
  <ul>
    <li><em>Actors:</em> <code>Rider</code>, <code>Driver</code>, <code>PaymentGateway</code>, <code>MappingService</code>.</li>
    <li><em>Core Use Cases:</em> <code>Request Ride</code>, <code>Match Driver</code>, <code>Track Trip Progress</code>, <code>Process Payment</code>, <code>Rate Ride</code>.</li>
    <li><em>Non-Functional Constraints:</em> High availability, sub-second driver matching within a 5km radius, real-time geolocation telemetry streaming.</li>
  </ul>

  <h5 class="answer-heading">Step 2: Object-Oriented Analysis (OOA) - Discovering Domain Entities</h5>
  <ul>
    <li>Identify core business domain concepts:
      <ul>
        <li><code>Rider</code>: Manages rider rating, payment tokens, active ride request.</li>
        <li><code>Driver</code>: Encapsulates current vehicle, live GPS coordinate, availability state (<code>Idle</code>, <code>EnRoute</code>, <code>OnTrip</code>).</li>
        <li><code>Trip</code>: Association class encapsulating pickup point, dropoff point, start/end timestamps, dynamic surge multiplier, and fare.</li>
        <li><code>Vehicle</code>: Encapsulates make, model, license plate, seating capacity, and tier (Economy, Premium, XL).</li>
      </ul>
    </li>
  </ul>

  <h5 class="answer-heading">Step 3: Object-Oriented System Design (Macro-Architecture)</h5>
  <ul>
    <li>Partition system into decoupled microservices:
      <ul>
        <li><strong>Location Service:</strong> Ingests high-frequency GPS pings from drivers into a distributed spatial index (H3 / Geospatial Redis).</li>
        <li><strong>Dispatch Engine:</strong> Matches ride requests to closest idle drivers using spatial proximity queries.</li>
        <li><strong>Billing Service:</strong> Calculates dynamic fares based on distance, duration, and surge demand curves.</li>
      </ul>
    </li>
  </ul>

  <h5 class="answer-heading">Step 4: Object Design (Micro-Architecture &amp; Design Patterns)</h5>
  <ul>
    <li>Apply design patterns to solve recurring challenges:
      <ul>
        <li><strong>Strategy Pattern for Fare Computation:</strong> Interface <code>FareStrategy</code> with interchangeable polymorphic classes: <code>StandardFare</code>, <code>SurgeFare</code>, <code>DiscountPromoFare</code>.</li>
        <li><strong>Observer Pattern for Geolocation:</strong> <code>RiderClient</code> subscribes to <code>DriverLocationPublisher</code> to update vehicle map icons in real time.</li>
        <li><strong>State Pattern for Trip Lifecycle:</strong> Class <code>TripState</code> with states: <code>RequestedState</code> &rarr; <code>AcceptedState</code> &rarr; <code>InProgressState</code> &rarr; <code>CompletedState</code>.</li>
      </ul>
    </li>
  </ul>

  <h5 class="answer-heading">Step 5: Design Optimization</h5>
  <ul>
    <li><strong>Spatial Index Optimization:</strong> Replace linear $O(N)$ distance scans over millions of drivers with an $O(1)$ geospatial Geohash/R-Tree lookup to identify nearby drivers in sub-milliseconds.</li>
    <li><strong>Caching &amp; Connection Pooling:</strong> Frequently accessed rider profiles and static pricing tables are cached in Redis clusters to eliminate redundant relational database round-trips.</li>
  </ul>

  <h4 class="answer-heading">6. Comprehensive Architectural Class Diagram Summary (Ride-Hailing)</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Domain Class</th>
        <th style="width: 30%;">Key Encapsulated Attributes</th>
        <th style="width: 50%;">Primary Operations &amp; Architectural Role</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>Rider</code></td>
        <td><code>riderId, rating, activePaymentMethod</code></td>
        <td><code>requestRide(), cancelRide(), rateDriver()</code></td>
      </tr>
      <tr>
        <td><code>Driver</code></td>
        <td><code>driverId, liveLocation, availabilityState</code></td>
        <td><code>acceptTrip(), rejectTrip(), updateGPSLocation()</code></td>
      </tr>
      <tr>
        <td><code>Trip</code></td>
        <td><code>tripId, pickupGPS, dropGPS, fareAmount</code></td>
        <td><code>startTrip(), endTrip(), calculateFinalFare()</code></td>
      </tr>
      <tr>
        <td><code>FareCalculator</code></td>
        <td><code>baseRate, perKmRate, surgeMultiplier</code></td>
        <td><code>computeDynamicFare(distance, duration, demandCurve)</code></td>
      </tr>
    </tbody>
  </table>

</div>
        """
    })

    # U3-L13
    questions.append({
        "id": "U3-L13",
        "unit": "3",
        "year": "2024-25",
        "year_display": "[2024-25]",
        "title": "Write a C++ program to demonstrate the concept of combining three models (class, state, and interaction) in the design of a smart home system.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Conceptual Foundations: Rumbaugh's Three Models</h4>
  <p>In Rumbaugh's Object Modeling Technique (OMT), a comprehensive system design integrates three complementary architectural models:</p>
  <ul>
    <li><strong>1. Class Model (Structural):</strong> Defines the static hierarchy, domain attributes, and operations (e.g., classes <code>SmartLight</code>, <code>SecuritySensor</code>).</li>
    <li><strong>2. State Model (Dynamic Lifecycle):</strong> Defines the internal lifecycle states and reactive event transitions (e.g., <code>OFF</code> &rarr; <code>MOTION_DETECTED</code> &rarr; <code>ACTIVE_ALARM</code>).</li>
    <li><strong>3. Interaction Model (Collaborative Messaging):</strong> Defines runtime message passing across objects to execute coordinated business scenarios.</li>
  </ul>

  <h4 class="answer-heading">2. Complete C++ Implementation Combining All Three Models</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;vector&gt;
#include &lt;memory&gt;

// ==========================================
// 1. STATE MODEL: Lifecycle State Enumeration
// ==========================================
enum class DeviceState {
    DISARMED,
    ARMED_STANDBY,
    MOTION_ALERT,
    ALARM_TRIGGERED
};

// ==========================================
// 1. CLASS MODEL: Structural Hierarchy
// ==========================================
class SmartDevice {
protected:
    std::string deviceId;
    DeviceState currentState;

public:
    SmartDevice(std::string id) 
        : deviceId(std::move(id)), currentState(DeviceState::DISARMED) {}
    virtual ~SmartDevice() = default;

    virtual void handleEvent(const std::string&amp; eventName) = 0;
    DeviceState getState() const { return currentState; }
    std::string getId() const { return deviceId; }
};

// Concrete Specialized Device: Motion Detector
class MotionSensor : public SmartDevice {
public:
    MotionSensor(std::string id) : SmartDevice(std::move(id)) {}

    // State Model Transitions implemented inside member method
    void handleEvent(const std::string&amp; eventName) override {
        if (eventName == "ARM_SYSTEM") {
            currentState = DeviceState::ARMED_STANDBY;
            std::cout &lt;&lt; "[Sensor " &lt;&lt; deviceId &lt;&lt; "] State Transition -&gt; ARMED_STANDBY\\n";
        } else if (eventName == "MOTION_DETECTED" &amp;&amp; currentState == DeviceState::ARMED_STANDBY) {
            currentState = DeviceState::MOTION_ALERT;
            std::cout &lt;&lt; "[Sensor " &lt;&lt; deviceId &lt;&lt; "] State Transition -&gt; MOTION_ALERT!\\n";
        }
    }
};

// Concrete Specialized Device: Siren Alarm
class SirenAlarm : public SmartDevice {
public:
    SirenAlarm(std::string id) : SmartDevice(std::move(id)) {}

    void handleEvent(const std::string&amp; eventName) override {
        if (eventName == "SOUND_SIREN") {
            currentState = DeviceState::ALARM_TRIGGERED;
            std::cout &lt;&lt; "[Siren " &lt;&lt; deviceId &lt;&lt; "] State Transition -&gt; BLARING AT 110dB!\\n";
        }
    }
};

// ==========================================
// 3. INTERACTION MODEL: Central Hub Mediator
// Orchestrates message exchanges between objects
// ==========================================
class SmartHomeHub {
private:
    std::shared_ptr&lt;MotionSensor&gt; sensor;
    std::shared_ptr&lt;SirenAlarm&gt; siren;

public:
    SmartHomeHub(std::shared_ptr&lt;MotionSensor&gt; sen, std::shared_ptr&lt;SirenAlarm&gt; sir)
        : sensor(std::move(sen)), siren(std::move(sir)) {}

    // Interaction Scenario: Dispatches messages across lifelines
    void triggerSecurityScenario() {
        std::cout &lt;&lt; "\\n=== INITIATING INTERACTION SCENARIO ===\\n";

        // Message 1: Hub arms sensor
        sensor-&gt;handleEvent("ARM_SYSTEM");

        // Message 2: External physical trigger occurs
        sensor-&gt;handleEvent("MOTION_DETECTED");

        // Message 3: Hub checks sensor state and triggers Siren
        if (sensor-&gt;getState() == DeviceState::MOTION_ALERT) {
            std::cout &lt;&lt; "[Hub Controller] Intercepted Alert! Dispatching Siren Message...\\n";
            siren-&gt;handleEvent("SOUND_SIREN");
        }
    }
};

int main() {
    auto livingRoomSensor = std::make_shared&lt;MotionSensor&gt;("PIR-01");
    auto exteriorSiren = std::make_shared&lt;SirenAlarm&gt;("SIREN-99");

    SmartHomeHub controller(livingRoomSensor, exteriorSiren);
    controller.triggerSecurityScenario();

    return 0;
}</code></pre>
</div>
        """
    })

    # U3-L14
    questions.append({
        "id": "U3-L14",
        "unit": "3",
        "year": "2024-25",
        "year_display": "[2024-25]",
        "title": "Compare and contrast SA/SD and object-oriented analysis and design. Use a case study of an online bookstore to highlight the differences.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Theoretical Contrast: Process Pipelines vs. Autonomous Objects</h4>
  <p><strong>Structured Analysis / Structured Design (SA/SD)</strong> approaches software through functional decomposition, regarding data as passive inputs flowing through transformation algorithms. In contrast, <strong>Object-Oriented Analysis and Design (OOAD)</strong> models software as an ecosystem of autonomous, collaborating domain entities encapsulating state and operations behind stable public contracts.</p>

  <h4 class="answer-heading">2. Detailed Case Study: Online Bookstore Architecture</h4>

  <h5 class="answer-heading">A. Bookstore Under the SA/SD Approach</h5>
  <ul>
    <li><em>Data Flow Pipeline:</em>
      <ul>
        <li><code>Process 1.0: Search Catalog</code> queries <code>Book_Database_Table</code>.</li>
        <li><code>Process 2.0: Manage Shopping Cart</code> reads/writes temporary <code>Cart_File</code>.</li>
        <li><code>Process 3.0: Process Payment</code> receives billing info, invokes bank API, writes to <code>Order_Table</code>.</li>
        <li><code>Process 4.0: Dispatch Warehouse Order</code> reads <code>Order_Table</code>, prints shipping manifest.</li>
      </ul>
    </li>
    <li><em>Architectural Fragility:</em> Processes 1.0, 2.0, 3.0, and 4.0 directly access shared relational database schemas. If the database schema is updated to add support for <em>Digital E-Books</em> (which have download links instead of shipping weights), all four functional processes must be manually modified and re-tested.</li>
  </ul>

  <h5 class="answer-heading">B. Bookstore Under the OOAD Approach</h5>
  <ul>
    <li><em>Collaborative Domain Entities:</em>
      <ul>
        <li><code>Book</code> (Abstract Class): Encapsulates ISBN, title, price, author; declares abstract operation <code>fulfillOrder()</code>.</li>
        <li><code>PhysicalBook</code>: Specializes <code>Book</code>; encapsulates weight and warehouse inventory; <code>fulfillOrder()</code> dispatches shipping notices.</li>
        <li><code>EBook</code>: Specializes <code>Book</code>; encapsulates file download URL and DRM cryptographic license; <code>fulfillOrder()</code> issues instantaneous download tokens.</li>
        <li><code>ShoppingCart</code>: Encapsulates collection of items, providing atomic operations <code>addItem()</code>, <code>removeItem()</code>, and <code>calculateSubtotal()</code>.</li>
        <li><code>Order</code>: Aggregates customer, payment profile, and order line items.</li>
      </ul>
    </li>
    <li><em>Architectural Resilience:</em> Introducing audiobooks or subscription rentals is achieved simply by subclassing <code>Book</code>. The checkout and payment pipelines process orders via the base <code>Book</code> interface polymorphically, adhering to the Open-Closed Principle.</li>
  </ul>

  <h4 class="answer-heading">3. Comparative Synthesis</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Criteria</th>
        <th style="width: 37%;">SA/SD Bookstore</th>
        <th style="width: 38%;">OOAD Bookstore</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Artifacts</strong></td>
        <td>Level-0 Context DFD, Level-1 DFD, Structure Charts.</td>
        <td>UML Class Diagrams, Sequence Diagrams, Statecharts.</td>
      </tr>
      <tr>
        <td><strong>Extensibility</strong></td>
        <td>Low (Modifying data records causes ripple effects across procedures).</td>
        <td>Extremely High (New product formats added via polymorphic specialization).</td>
      </tr>
      <tr>
        <td><strong>State Integrity</strong></td>
        <td>Vulnerable (Unprotected data stores accessed directly by functions).</td>
        <td>Guaranteed (Invariants protected behind class encapsulation).</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">4. Architectural Impact on Database Design</h4>
  <p>The choice between SA/SD and OOAD fundamentally dictates the persistence architecture of the online bookstore:</p>
  <ul>
    <li><strong>SA/SD Persistence (Flat Relational Tables):</strong> Decomposes data into normalized relational tables (<code>BOOK_CATALOG</code>, <code>CUSTOMER_TABLE</code>, <code>ORDER_TABLE</code>) accessed directly by procedural SQL queries embedded inside application subroutines. Adding polymorphic item types requires null columns or complex foreign key joins.</li>
    <li><strong>OOAD Persistence (Domain-Driven ORM):</strong> Utilizes Object-Relational Mapping (ORM) or Document stores where class hierarchies (<code>PhysicalBook</code>, <code>EBook</code>, <code>AudioBook</code>) are mapped using table-per-class or single-table inheritance strategies, preserving class encapsulation and domain behaviors across storage boundaries.</li>
  </ul>

</div>
        """
    })

    # U3-L15
    questions.append({
        "id": "U3-L15",
        "unit": "3",
        "year": "2025-26",
        "year_display": "[2025-26]",
        "title": "Discuss abstraction and encapsulation with suitable examples. Explain reusability, extensibility, and robustness in object-oriented programming.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Abstraction and Encapsulation: Complementary Pillars</h4>
  <p><strong>Abstraction</strong> and <strong>Encapsulation</strong> are the twin foundational pillars of object-oriented architecture:</p>
  <ul>
    <li><strong>Abstraction (External Contract):</strong> The cognitive process of isolating essential, general characteristics of an entity while filtering out transient implementation details. It specifies <em>what</em> an object provides to the outside world through abstract classes and pure interfaces.
      <br><em>Example:</em> A <code>DatabaseConnection</code> interface declaring <code>executeQuery()</code> abstracts away network socket buffers, TCP handshakes, and query parsing.</li>
    <li><strong>Encapsulation (Internal Barrier):</strong> The structural bundling of state variables and operations within a class, combined with access control (<code>private</code>) to shield data from external tampering.
      <br><em>Example:</em> An <code>Account</code> class makes its <code>balance</code> private, permitting changes only through <code>deposit()</code> and <code>withdraw()</code> methods that validate non-negative amounts.</li>
  </ul>

  <h4 class="answer-heading">2. In-Depth Analysis of the Three Quality Attributes</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Attribute</th>
        <th style="width: 40%;">Conceptual Meaning</th>
        <th style="width: 40%;">Object-Oriented Enablement Mechanics</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Reusability</strong></td>
        <td>The capability to reuse verified, tested software components across different systems without rewriting source code.</td>
        <td>
          &bull; <strong>Component Composition:</strong> Aggregating smaller classes into larger composites.<br>
          &bull; <strong>Inheritance &amp; Templates:</strong> Extending base classes and utilizing generic template containers.
        </td>
      </tr>
      <tr>
        <td><strong>Extensibility</strong></td>
        <td>The ease with which new capabilities can be introduced without modifying or recompiling existing, tested modules.</td>
        <td>
          &bull; <strong>Open-Closed Principle (OCP):</strong> High-level logic depends on abstract interfaces.<br>
          &bull; <strong>Dynamic Polymorphism:</strong> New subclasses are plugged into existing pipelines at runtime via virtual method tables.
        </td>
      </tr>
      <tr>
        <td><strong>Robustness</strong></td>
        <td>The resilience of software to maintain deterministic behavior and recover gracefully under adverse runtime errors.</td>
        <td>
          &bull; <strong>Class Invariant Protection:</strong> Access specifiers prevent illegal states.<br>
          &bull; <strong>RAII:</strong> Resource destruction is guaranteed automatically when objects exit scope.
        </td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. Comprehensive C++ Industrial Demonstration</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;memory&gt;

// Abstract Base Interface (Abstraction)
class PaymentGateway {
public:
    virtual ~PaymentGateway() = default;
    virtual bool processPayment(double amount) = 0; // Polymorphic contract
};

// Concrete Specialized Class (Encapsulation + Robustness)
class SecureCreditGateway : public PaymentGateway {
private:
    std::string merchantToken;
    double dailyLimit;
    double dailyTotal;

public:
    SecureCreditGateway(std::string token, double limit)
        : merchantToken(std::move(token)), dailyLimit(limit), dailyTotal(0.0) {}

    bool processPayment(double amount) override {
        // Enforcing robustness invariants
        if (amount <= 0.0 || (dailyTotal + amount) > dailyLimit) {
            std::cout << "[REJECTED] Transaction exceeds limits or invalid.\n";
            return false;
        }
        dailyTotal += amount;
        std::cout << "[SUCCESS] Charged $" << amount << " via Secure Gateway.\n";
        return true;
    }
};

int main() {
    std::unique_ptr&lt;PaymentGateway&gt; gateway = 
        std::make_unique&lt;SecureCreditGateway&gt;("AUTH_KEY_99", 5000.0);
    gateway->processPayment(450.0); // Allowed
    return 0;
}</code></pre>


  <h4 class="answer-heading">4. Exhaustive Comparison: Abstraction vs. Encapsulation</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Criteria</th>
        <th style="width: 40%;">Abstraction</th>
        <th style="width: 40%;">Encapsulation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Intent</strong></td>
        <td>Hides unnecessary domain complexity by exposing only relevant high-level behavior.</td>
        <td>Protects internal state integrity by bundling data with operations and restricting access.</td>
      </tr>
      <tr>
        <td><strong>Focus</strong></td>
        <td>Outer perspective (<em>What</em> the object does from the consumer's viewpoint).</td>
        <td>Inner perspective (<em>How</em> the object is structured and protected internally).</td>
      </tr>
      <tr>
        <td><strong>Language Tools</strong></td>
        <td>Abstract classes, Pure Virtual functions (<code>= 0</code>), Interfaces.</td>
        <td>Access control specifiers: <code>private</code>, <code>protected</code>, <code>public</code>.</td>
      </tr>
      <tr>
        <td><strong>Design Phase</strong></td>
        <td>Architectural and conceptual modeling phase.</td>
        <td>Detailed design and code implementation phase.</td>
      </tr>
    </tbody>
  </table>

</div>
        """
    })

    # U3-L16
    questions.append({
        "id": "U3-L16",
        "unit": "3",
        "year": "2025-26",
        "year_display": "[2025-26]",
        "title": "Describe structured analysis and structured design and Jackson Structure Development.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Detailed Technical Analysis of SA/SD</h4>
  <p><strong>Structured Analysis and Structured Design (SA/SD)</strong> is a classical engineering approach based on algorithmic, top-down functional decomposition. The methodology treats algorithms and data as separate entities:</p>
  <ul>
    <li><strong>Analysis Workflow:</strong> Uses Data Flow Diagrams (DFDs) to model data transformations, backed by a formal Data Dictionary and P-Specs (Process Specifications).</li>
    <li><strong>Design Transition:</strong> Uses <em>Transform Analysis</em> and <em>Transaction Analysis</em> heuristics to convert flat DFD process networks into hierarchical Structure Charts representing caller-callee subroutine trees.</li>
    <li><strong>Design Metrics:</strong> Evaluated using Constantine's coupling and cohesion metrics, striving for high functional cohesion and low data coupling.</li>
  </ul>

  <h4 class="answer-heading">2. Detailed Technical Analysis of Jackson Structure Development (JSD)</h4>
  <p><strong>Jackson System Development (JSD)</strong>, created by Michael Jackson, models systems not as functional transforms, but as dynamic simulations of real-world entities over time:</p>
  <ul>
    <li><strong>Entity Action Modeling:</strong> Focuses strictly on atomic real-world events performed or suffered by entities.</li>
    <li><strong>Entity Structure Diagrams (ESD):</strong> Tree structures capturing the temporal order of events using regular grammar:
      <ul>
        <li><em>Sequence:</em> Nodes arranged in strict left-to-right execution order.</li>
        <li><em>Selection (o):</em> Mutually exclusive conditional choices.</li>
        <li><em>Iteration (*):</em> Zero or more repetitions of an action.</li>
      </ul>
    </li>
    <li><strong>Process Inversion:</strong> Converts long-running concurrent communicating sequential processes (CSP) into callable subroutines via state vectors, enabling deployment on single-threaded CPUs.</li>
  </ul>

  <h4 class="answer-heading">3. Comparative Synthesis</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Dimension</th>
        <th style="width: 37%;">SA/SD Methodology</th>
        <th style="width: 38%;">JSD Methodology</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Modeling Driver</strong></td>
        <td>Process transformation of inputs into required system outputs.</td>
        <td>Temporal event ordering and real-world entity life histories.</td>
      </tr>
      <tr>
        <td><strong>Transition to Code</strong></td>
        <td>Translates into hierarchical procedural subroutines.</td>
        <td>Translates into communicating concurrent processes / coroutines.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">4. Step-by-Step Entity Structure Tree Construction</h4>
  <p>In Jackson System Development, entity lifecycles are modeled using strict tree structures:</p>
  <ul>
    <li><em>Root Node:</em> Represents the total entity life history (e.g., <code>CUSTOMER_LIFE</code>).</li>
    <li><em>Sub-Nodes (Sequence):</em> Chronological phases: <code>REGISTRATION</code> &rarr; <code>ACTIVE_MEMBERSHIP</code> &rarr; <code>TERMINATION</code>.</li>
    <li><em>Iteration (*):</em> <code>ACTIVE_MEMBERSHIP</code> consists of zero or more <code>TRANSACTIONS*</code>.</li>
    <li><em>Selection (o):</em> A transaction is either a <code>PURCHASEo</code> or a <code>REFUNDo</code>.</li>
  </ul>
  <p>This regular grammar maps directly into coroutine state machines, providing deterministic guarantees against illegal out-of-order event executions.</p>


  <h4 class="answer-heading">5. Walkthrough of an ATM System under SA/SD vs. JSD</h4>
  <ul>
    <li><strong>Under SA/SD (Functional Pipeline):</strong> The ATM is modeled as a set of functional transforms: <code>Validate Card</code> &rarr; <code>Verify PIN</code> &rarr; <code>Check Balance</code> &rarr; <code>Dispense Cash</code> &rarr; <code>Print Receipt</code>. Passive account records flow between these processes. If a new transaction type (e.g., mobile top-up) is added, the central structure chart and DFD bubbles must be redesigned.</li>
    <li><strong>Under JSD (Entity Life History):</strong> The ATM is modeled around real-world entities: <code>CUSTOMER</code> and <code>ATM_TERMINAL</code>. The lifecycle of <code>CUSTOMER</code> is modeled as an Entity Structure Diagram: <code>INSERT_CARD</code> &rarr; <code>ENTER_PIN</code> &rarr; <code>TRANSACTION*</code> &rarr; <code>EJECT_CARD</code>. Each transaction is a selection between <code>WITHDRAWALo</code>, <code>DEPOSSTo</code>, or <code>BALANCE_INQUIRYo</code>. JSD preserves the natural chronological order of customer behavior, making it immune to functional requirement mutations.</li>
  </ul>

</div>
        """
    })

    # U3-L17
    questions.append({
        "id": "U3-L17",
        "unit": "3",
        "year": "2025-26",
        "year_display": "[2025-26]",
        "title": "Discuss object representation, physical packaging, and documentation design considerations. Explain how object-oriented concepts are mapped to non-object-oriented languages.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Detailed Discussion of Implementation Considerations</h4>

  <h5 class="answer-heading">A. Object Representation in Physical Memory</h5>
  <p>At the physical hardware level, an object is a contiguous block of heap or stack memory allocated to hold its instance member variables. In languages supporting dynamic polymorphism (C++), the compiler inserts a hidden <strong>Virtual Table Pointer (<code>vptr</code>)</strong> at offset zero. The <code>vptr</code> points to a static class-wide <strong>Virtual Method Table (VTable)</strong> containing function pointers to overridden virtual functions, enabling runtime indirect dispatch.</p>

  <h5 class="answer-heading">B. Physical Packaging</h5>
  <p>Decomposes large object models into modular, independently deployable software binaries. In UML, physical packaging is realized through <strong>Components</strong> and <strong>Packages</strong>. Best practices include adhering to the <em>Common Reuse Principle (CRP)</em> and <em>Acyclic Dependencies Principle (ADP)</em> to prevent cyclic build dependencies between JARs, DLLs, and microservice containers.</p>

  <h5 class="answer-heading">C. Documentation Design Considerations</h5>
  <p>Engineering documentation must preserve architectural rationale. This includes maintaining living architectural decision records (ADRs), synchronizing UML interface models with source code via automated CI/CD tools, and adhering to audience stratification (executive summaries vs. low-level API contracts).</p>

  <h4 class="answer-heading">2. Mapping Object-Oriented Concepts to Non-OO Languages (Pure C)</h4>
  <p>Non-object-oriented procedural languages (like ANSI C) can emulate the complete object-oriented feature set through systematic structural patterns:</p>
  <ul>
    <li><strong>Encapsulation:</strong> Modeled using C <code>struct</code> declarations. Methods are free functions taking an explicit <code>self</code> pointer as their first argument.</li>
    <li><strong>Inheritance:</strong> Modeled by embedding the base struct as the <strong>first member field</strong> inside the derived struct. Because the base struct offset is zero, any derived struct pointer can be safely cast to the base struct pointer.</li>
    <li><strong>Polymorphism:</strong> Modeled using explicit VTable structs of function pointers and initializing the <code>vptr</code> inside the constructor function.</li>
  </ul>

  <h4 class="answer-heading">3. C Architectural Demonstration</h4>
  <pre class="code-block"><code>// Base Class VTable
typedef struct ShapeVTable {
    double (*getArea)(void* self);
} ShapeVTable;

// Base Class Struct
typedef struct Shape {
    const ShapeVTable* vptr;
} Shape;

// Derived Class Struct (Inheritance via embedding base as first element)
typedef struct Circle {
    Shape base;    // Offset 0: matches Shape*
    double radius;
} Circle;

double Circle_getArea(void* self) {
    Circle* c = (Circle*)self;
    return 3.14159 * c-&gt;radius * c-&gt;radius;
}

static const ShapeVTable circle_vtable = { Circle_getArea };

void Circle_init(Circle* c, double r) {
    c-&gt;base.vptr = &amp;circle_vtable;
    c-&gt;radius = r;
}</code></pre>
</div>
        """
    })

    return questions

if __name__ == "__main__":
    qs = get_unit3_questions()
    print(f"Generated {len(qs)} questions for Unit 3.")
    import re
    for q in qs:
        clean = re.sub(r'<[^>]+>', ' ', q['content'])
        words = len(clean.split())
        print(f"{q['id']}: {words} words | has_svg={'<svg' in q['content']} | has_code={'<code' in q['content']}")


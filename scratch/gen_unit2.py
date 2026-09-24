# -*- coding: utf-8 -*-
"""
Unit 2 Long Answers Generator (Questions U2-L01 to U2-L20)
Every question contains 400-750 words, detailed subheadings, comparison tables,
working C++ code, or high-contrast SVG diagrams.
"""

def get_unit2_questions():
    questions = []

    # U2-L01
    questions.append({
        "id": "U2-L01",
        "unit": "2",
        "year": "2020-21",
        "year_display": "[2020-21]",
        "title": "Discuss the term Link and Association by taking suitable example. Also, define multiplicity.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Definition and Conceptual Distinction: Link vs. Association</h4>
  <p>In object-oriented modeling, the relationship between a <strong>Link</strong> and an <strong>Association</strong> mirrors the foundational relationship between an <strong>Object</strong> and a <strong>Class</strong>:</p>
  <ul>
    <li><strong>Association (Class-Level Classifier):</strong> An Association is a static, structural relationship that describes a set of potential connections between classes. It acts as a compile-time schema specifying that instances of one class are conceptually related to instances of another class, defining relationship names, role names, and cardinality rules. In UML, it is rendered as a solid line connecting two class rectangles.</li>
    <li><strong>Link (Object-Level Instance):</strong> A Link is a concrete physical or conceptual connection between two specific runtime object instances in memory. If an association exists between classes <code>Doctor</code> and <code>Patient</code>, then at runtime, the connection between <code>drSmith:Doctor</code> and <code>johnDoe:Patient</code> is a Link. A link is an instance of an association, rendered as a line between underlined object boxes without multiplicity adornments.</li>
  </ul>

  <h4 class="answer-heading">2. Detailed Comparative Analysis</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Criteria</th>
        <th style="width: 37%;">Association</th>
        <th style="width: 38%;">Link</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Metamodel Level</strong></td>
        <td>M1 Model Level (Classifier relationship between classes).</td>
        <td>M0 Instance Level (Concrete runtime connection between objects).</td>
      </tr>
      <tr>
        <td><strong>Multiplicity Adornment</strong></td>
        <td>Mandatory (Specifies allowed range, e.g., <code>1..*</code>, <code>0..1</code>).</td>
        <td>Invalid (A link is strictly a 1-to-1 connection between two specific object instances).</td>
      </tr>
      <tr>
        <td><strong>Implementation Mechanism</strong></td>
        <td>Pointers, references, foreign keys, or collection containers (<code>std::vector</code>).</td>
        <td>The actual runtime pointer address in heap memory (e.g., <code>0x7ffd9820</code>).</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. Definition and Notation of Multiplicity</h4>
  <p><strong>Multiplicity</strong> specifies the cardinality—the exact numerical range of instances of one class that may be linked to a single instance of another class across an association. It is denoted as <code>[lower_bound .. upper_bound]</code>:</p>
  <ul>
    <li><code>1</code> or <code>1..1</code>: Exactly one instance (Mandatory singular).</li>
    <li><code>0..1</code>: Zero or one instance (Optional singular).</li>
    <li><code>*</code> or <code>0..*</code>: Zero or more instances (Unbounded collection).</li>
    <li><code>1..*</code>: At least one instance (Mandatory non-empty collection).</li>
    <li><code>n..m</code>: Specific bounded range (e.g., <code>2..4</code> players).</li>
  </ul>

  <h4 class="answer-heading">4. Architectural Demonstration: Company Employment System</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="620" height="180" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>
      
      <!-- Class Company -->
      <rect x="40" y="50" width="160" height="70" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <rect x="40" y="50" width="160" height="25" fill="#f6f8fa" stroke="#1f2328" stroke-width="1"/>
      <text x="120" y="67" font-family="monospace" font-size="12" font-weight="bold" fill="#0969da" text-anchor="middle">Company</text>
      <text x="50" y="95" font-family="monospace" font-size="10" fill="#1f2328">- compName: String</text>

      <!-- Class Employee -->
      <rect x="420" y="50" width="160" height="70" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <rect x="420" y="50" width="160" height="25" fill="#f6f8fa" stroke="#1f2328" stroke-width="1"/>
      <text x="500" y="67" font-family="monospace" font-size="12" font-weight="bold" fill="#0969da" text-anchor="middle">Employee</text>
      <text x="430" y="95" font-family="monospace" font-size="10" fill="#1f2328">- empId: String</text>

      <!-- Association Line -->
      <line x1="200" y1="85" x2="420" y2="85" stroke="#1f2328" stroke-width="1.5"/>
      <text x="310" y="78" font-family="sans-serif" font-size="11" fill="#1f2328" text-anchor="middle">Employs &gt;</text>
      <text x="210" y="100" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da">1</text>
      <text x="210" y="115" font-family="sans-serif" font-size="9" fill="#656d76">employer</text>
      <text x="395" y="100" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da">1..*</text>
      <text x="375" y="115" font-family="sans-serif" font-size="9" fill="#656d76">staff</text>
    </svg>
    <span class="diagram-caption">Figure U2-L01: Association between Company and Employee with Multiplicities and Role Names</span>
  </div>

  <h4 class="answer-heading">5. C++ Implementation Mapping</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;vector&gt;
#include &lt;memory&gt;

class Employee; // Forward declaration

class Company {
    std::string name;
    // Multiplicity 1..* represented as a collection container
    std::vector&lt;std::shared_ptr&lt;Employee&gt;&gt; staff;
public:
    Company(std::string n) : name(std::move(n)) {}
    void hire(std::shared_ptr&lt;Employee&gt; emp) { staff.push_back(emp); }
};

class Employee {
    std::string id;
    // Multiplicity 1 represented as a raw/weak back-reference pointer
    Company* employer;
public:
    Employee(std::string empId, Company* comp) : id(std::move(empId)), employer(comp) {}
};</code></pre>
</div>
        """
    })

    # U2-L02
    questions.append({
        "id": "U2-L02",
        "unit": "2",
        "year": "2020-21",
        "year_display": "[2020-21]",
        "title": "What is use case driven OOA? How is it different from OOD? Explain OOA process with the help of a diagram in the unified approach.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Concept of Use-Case Driven Object-Oriented Analysis (OOA)</h4>
  <p><strong>Use-Case Driven Object-Oriented Analysis</strong> is a systems analysis methodology pioneered by Ivar Jacobson wherein the functional requirements of a system are captured from the perspective of external actors through structured narrative scenarios called <strong>Use Cases</strong>. In this approach, use cases are not merely a requirements capture tool; they serve as the foundational architectural driver throughout the entire engineering lifecycle: driving analysis object discovery, guiding test case construction, structuring user manuals, and verifying design models.</p>

  <h4 class="answer-heading">2. Distinctive Boundaries: OOA vs. OOD</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Dimension</th>
        <th style="width: 37%;">Object-Oriented Analysis (OOA)</th>
        <th style="width: 38%;">Object-Oriented Design (OOD)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Objective</strong></td>
        <td>Understand the problem domain (<em>"What"</em> the system must do).</td>
        <td>Formulate technical software solutions (<em>"How"</em> to build it).</td>
      </tr>
      <tr>
        <td><strong>Technology Dependency</strong></td>
        <td>Completely technology-neutral (no language, DB, or OS specifics).</td>
        <td>Technology-specific (binds to C++, SQL, threading, IPC, HTTP).</td>
      </tr>
      <tr>
        <td><strong>Class Model Granularity</strong></td>
        <td>Conceptual domain entities, high-level business attributes.</td>
        <td>Detailed design classes with visibility, types, VTables, algorithms.</td>
      </tr>
      <tr>
        <td><strong>Artifact Focus</strong></td>
        <td>Domain Class Diagrams, System Sequence Diagrams, Use Case Narratives.</td>
        <td>Detailed Interaction Diagrams, Package/Component Schemas, Design Patterns.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. The OOA Process in the Unified Approach</h4>
  <p>In the Unified Approach (combining Jacobson's Objectory, Rumbaugh's OMT, and Booch's methodology), OOA proceeds systematically through five iterative stages:</p>
  <ol>
    <li><strong>Actor &amp; Use Case Identification:</strong> Map external actors and elicit use case narratives with primary and alternate scenarios.</li>
    <li><strong>Boundary-Control-Entity (BCE) Decomposition:</strong> Identify three classes of analysis objects:
      <ul>
        <li><em>Boundary Objects:</em> Interface mechanisms between system and actors (screens, sensors, API endpoints).</li>
        <li><em>Control Objects:</em> Orchestrate transaction lifecycles, business logic, and coordination flow.</li>
        <li><em>Entity Objects:</em> Long-lived core domain information and business state (e.g., <code>Account</code>, <code>Customer</code>).</li>
      </ul>
    </li>
    <li><strong>Interaction Modeling:</strong> Construct Sequence Diagrams tracing message exchanges between BCE objects to fulfill each use case.</li>
    <li><strong>Class Diagram Formulation:</strong> Synthesize static conceptual class diagrams derived from participating entity attributes and operations.</li>
    <li><strong>Dynamic Verification:</strong> Construct State Machine Diagrams for reactive entities with complex lifecycle states.</li>
  </ol>

  <h4 class="answer-heading">4. Architectural Flow Diagram of the Unified OOA Process</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 660 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="660" height="170" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Step 1 -->
      <rect x="20" y="40" width="105" height="70" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="72" y="65" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">Step 1</text>
      <text x="72" y="85" font-family="sans-serif" font-size="10" fill="#1f2328" text-anchor="middle">Use Case</text>
      <text x="72" y="100" font-family="sans-serif" font-size="10" fill="#1f2328" text-anchor="middle">Modeling</text>

      <!-- Arrow 1 -->
      <line x1="125" y1="75" x2="145" y2="75" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="145,75 140,71 140,79" fill="#1f2328"/>

      <!-- Step 2 -->
      <rect x="150" y="40" width="105" height="70" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="202" y="65" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">Step 2</text>
      <text x="202" y="85" font-family="sans-serif" font-size="10" fill="#1f2328" text-anchor="middle">Object</text>
      <text x="202" y="100" font-family="sans-serif" font-size="10" fill="#1f2328" text-anchor="middle">Discovery (BCE)</text>

      <!-- Arrow 2 -->
      <line x1="255" y1="75" x2="275" y2="75" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="275,75 270,71 270,79" fill="#1f2328"/>

      <!-- Step 3 -->
      <rect x="280" y="40" width="105" height="70" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="332" y="65" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">Step 3</text>
      <text x="332" y="85" font-family="sans-serif" font-size="10" fill="#1f2328" text-anchor="middle">Interaction</text>
      <text x="332" y="100" font-family="sans-serif" font-size="10" fill="#1f2328" text-anchor="middle">Modeling</text>

      <!-- Arrow 3 -->
      <line x1="385" y1="75" x2="405" y2="75" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="405,75 400,71 400,79" fill="#1f2328"/>

      <!-- Step 4 -->
      <rect x="410" y="40" width="105" height="70" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="462" y="65" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">Step 4</text>
      <text x="462" y="85" font-family="sans-serif" font-size="10" fill="#1f2328" text-anchor="middle">Domain Class</text>
      <text x="462" y="100" font-family="sans-serif" font-size="10" fill="#1f2328" text-anchor="middle">Diagrams</text>

      <!-- Arrow 4 -->
      <line x1="515" y1="75" x2="535" y2="75" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="535,75 530,71 530,79" fill="#1f2328"/>

      <!-- Step 5 -->
      <rect x="540" y="40" width="105" height="70" fill="#ffffff" stroke="#0969da" stroke-width="2"/>
      <text x="592" y="65" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">Step 5</text>
      <text x="592" y="85" font-family="sans-serif" font-size="10" fill="#1f2328" text-anchor="middle">State Machine</text>
      <text x="592" y="100" font-family="sans-serif" font-size="10" fill="#1f2328" text-anchor="middle">Verification</text>

      <!-- Feedback Loop Line -->
      <path d="M 592 110 L 592 140 L 72 140 L 72 110" fill="none" stroke="#656d76" stroke-width="1.2" stroke-dasharray="3,3"/>
      <text x="332" y="155" font-family="sans-serif" font-size="9" fill="#656d76" text-anchor="middle">Iterative Refinement &amp; Customer Traceability Feedback</text>
    </svg>
    <span class="diagram-caption">Figure U2-L02: Systematic OOA Workflow in the Unified Approach</span>
  </div>

  <h4 class="answer-heading">5. Traceability Across the Unified Approach Workflow</h4>
  <p>In the Unified Approach, use cases provide the architectural baseline ensuring end-to-end traceability across all engineering artifacts:</p>
  <ul>
    <li><strong>Use Case Realization:</strong> Each use case is systematically realized through one or more UML Collaboration or Sequence Diagrams that allocate responsibilities to Boundary, Control, and Entity classes.</li>
    <li><strong>Test Case Derivation:</strong> Primary use case execution paths directly formulate happy-path functional test suites; alternate scenarios and exception branches formulate boundary-value and failure test vectors.</li>
    <li><strong>Verification and Validation:</strong> Design review boards inspect whether every customer requirement documented in the use case model is mapped to at least one operation in the domain class model.</li>
  </ul>

</div>
        """
    })

    # U2-L03
    questions.append({
        "id": "U2-L03",
        "unit": "2",
        "year": "2020-21",
        "year_display": "[2020-21]",
        "title": "List the properties of a state chart diagram. Draw a state chart for a coin vending machine present at a railway station.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Formal Definition and Properties of a Statechart Diagram</h4>
  <p>A <strong>Statechart Diagram</strong> (originating from David Harel's Statecharts and standardized in UML) models the dynamic event-driven behavior of a single reactive object throughout its lifecycle. It specifies how an object transitions between discrete operational states in response to external events, internal triggers, and elapsed time.</p>
  <p>Key properties of Statechart Diagrams include:</p>
  <ul>
    <li><strong>State:</strong> A condition or situation during the life of an object during which it satisfies some invariant condition, performs some ongoing activity (<code>do/</code> activity), or waits for an external event. Rendered as a rounded rectangle.</li>
    <li><strong>Event:</strong> A notable runtime occurrence that triggers a state transition (e.g., signal reception, method invocation, guard satisfaction, or elapsed timer).</li>
    <li><strong>Transition:</strong> A directed relationship from a source state to a target state, formally annotated as: <code>Event [Guard Condition] / Action List</code>.</li>
    <li><strong>Guard Condition:</strong> A boolean expression placed inside brackets <code>[...]</code>. The transition fires if and only if the guard evaluates to true at the instant the event occurs.</li>
    <li><strong>Action:</strong> An atomic, instantaneous, non-interruptible computational execution triggered during the transition (<code>/ Action</code>).</li>
    <li><strong>Pseudo-states:</strong> Initial state (solid black circle), Final state (bullseye circle), and Choice/Junction points (diamond icons).</li>
  </ul>

  <h4 class="answer-heading">2. Statechart Diagram: Railway Station Coin Vending Machine</h4>
  <p>Consider a ticket-vending machine located at a railway terminal. It accepts coins, permits ticket destination selection, validates balance adequacy, dispenses tickets and change, or refunds money upon cancellation.</p>

  <div class="diagram-container">
    <svg viewBox="0 0 680 320" width="100%" height="320" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="320" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Initial State -->
      <circle cx="40" cy="80" r="10" fill="#1f2328"/>
      
      <!-- Transition to Idle -->
      <line x1="50" y1="80" x2="90" y2="80" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="90,80 84,76 84,84" fill="#1f2328"/>

      <!-- State: IDLE -->
      <rect x="90" y="50" width="120" height="60" rx="8" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="150" y="75" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">IDLE</text>
      <text x="150" y="95" font-family="sans-serif" font-size="9" fill="#656d76" text-anchor="middle">entry / displayPrompt()</text>

      <!-- Transition: Insert Coin -->
      <line x1="210" y1="80" x2="280" y2="80" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="280,80 274,76 274,84" fill="#1f2328"/>
      <text x="245" y="72" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">insertCoin(c) / addVal</text>

      <!-- State: COIN_INSERTED -->
      <rect x="280" y="50" width="140" height="60" rx="8" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="350" y="75" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">COINS_HELD</text>
      <text x="350" y="95" font-family="sans-serif" font-size="9" fill="#656d76" text-anchor="middle">do / updateDisplay()</text>

      <!-- Self Loop on Coin Inserted -->
      <path d="M 330 50 C 330 25, 370 25, 370 50" fill="none" stroke="#1f2328" stroke-width="1.2"/>
      <polygon points="370,50 366,42 374,42" fill="#1f2328"/>
      <text x="350" y="22" font-family="sans-serif" font-size="8" fill="#1f2328" text-anchor="middle">insertCoin(c)</text>

      <!-- Cancel to Idle -->
      <path d="M 350 110 C 350 160, 150 160, 150 110" fill="none" stroke="#cf222e" stroke-width="1.2"/>
      <polygon points="150,110 146,118 154,118" fill="#cf222e"/>
      <text x="250" y="150" font-family="sans-serif" font-size="9" fill="#cf222e" text-anchor="middle">pressCancel() / refundAllCoins()</text>

      <!-- Transition: Select Destination -->
      <line x1="420" y1="80" x2="480" y2="80" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="480,80 474,76 474,84" fill="#1f2328"/>
      <text x="450" y="72" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">selectDest()</text>

      <!-- Choice Point -->
      <polygon points="500,80 515,65 530,80 515,95" fill="#f6f8fa" stroke="#0969da" stroke-width="1.5"/>

      <!-- Insufficient Balance branch back -->
      <path d="M 515 65 C 515 35, 410 35, 390 50" fill="none" stroke="#656d76" stroke-width="1.2"/>
      <polygon points="390,50 398,46 394,54" fill="#656d76"/>
      <text x="460" y="42" font-family="sans-serif" font-size="8" fill="#656d76" text-anchor="middle">[coins &lt; fare] / alert()</text>

      <!-- Sufficient Balance branch to Dispensing -->
      <line x1="515" y1="95" x2="515" y2="190" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="515,190 511,184 519,184" fill="#1f2328"/>
      <text x="525" y="145" font-family="sans-serif" font-size="9" fill="#1f2328">[coins &gt;= fare]</text>

      <!-- State: DISPENSING -->
      <rect x="440" y="190" width="150" height="60" rx="8" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="515" y="215" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">DISPENSING</text>
      <text x="515" y="235" font-family="sans-serif" font-size="9" fill="#656d76" text-anchor="middle">do / printTicketAndChange()</text>

      <!-- Complete to Idle -->
      <path d="M 440 220 L 100 220 L 100 110" fill="none" stroke="#1a7f37" stroke-width="1.5"/>
      <polygon points="100,110 96,118 104,118" fill="#1a7f37"/>
      <text x="270" y="215" font-family="sans-serif" font-size="9" fill="#1a7f37" text-anchor="middle">dispenseComplete / reset()</text>
    </svg>
    <span class="diagram-caption">Figure U2-L03: UML Statechart Diagram for Railway Coin Vending Machine</span>
  </div>

  <h4 class="answer-heading">3. State Invariant Transition Table</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th>Source State</th>
        <th>Triggering Event &amp; Guard</th>
        <th>Target State</th>
        <th>Executed Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>IDLE</code></td>
        <td><code>insertCoin(coinVal)</code></td>
        <td><code>COINS_HELD</code></td>
        <td><code>balance += coinVal</code></td>
      </tr>
      <tr>
        <td><code>COINS_HELD</code></td>
        <td><code>pressCancel()</code></td>
        <td><code>IDLE</code></td>
        <td><code>refundCoins(balance); balance = 0</code></td>
      </tr>
      <tr>
        <td><code>COINS_HELD</code></td>
        <td><code>selectDest() [balance &gt;= fare]</code></td>
        <td><code>DISPENSING</code></td>
        <td><code>change = balance - fare; print()</code></td>
      </tr>
      <tr>
        <td><code>DISPENSING</code></td>
        <td><code>dispenseComplete</code></td>
        <td><code>IDLE</code></td>
        <td><code>resetHardwareSensors()</code></td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">4. Advanced Statechart Concepts: Composite States &amp; History Mechanisms</h4>
  <p>In complex industrial control systems, statechart diagrams manage combinatorial state explosion using advanced structuring mechanisms:</p>
  <ul>
    <li><strong>Composite States (Hierarchical States):</strong> A state that contains nested sub-states. For example, the <code>OPERATIONAL</code> state can encapsulate nested sub-states <code>COINS_HELD</code> and <code>DISPENSING</code>. An event triggering a transition out of the composite state (such as <code>emergencyPowerOff</code>) automatically aborts all active sub-states without requiring individual transition arrows from each sub-state.</li>
    <li><strong>Orthogonal Regions (Concurrency):</strong> Models independent parallel behaviors within a single object (e.g., a ticket vending machine simultaneously managing hardware temperature telemetry while processing currency insertion).</li>
    <li><strong>History Pseudo-States (<code>H</code> / <code>H*</code>):</strong> Remembers the most recently active sub-state within a composite state before an interrupt occurred, allowing the system to resume execution exactly where it left off rather than resetting to the initial state.</li>
  </ul>

</div>
        """
    })

    # U2-L04
    questions.append({
        "id": "U2-L04",
        "unit": "2",
        "year": "2020-21",
        "year_display": "[2020-21]",
        "title": "What do we mean by a collaboration diagram? Explain various terms and symbols used in a collaboration diagram. How is polymorphism described using a collaboration diagram? Explain using an example.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Definition and Concept of a Collaboration (Communication) Diagram</h4>
  <p>A <strong>Collaboration Diagram</strong> (renamed <em>Communication Diagram</em> in UML 2.x) is an interaction diagram that illustrates dynamic system behavior by emphasizing the <strong>structural organization of objects</strong> that participate in a collaborative task. Unlike Sequence Diagrams—which prioritize the strict chronological, top-down progression of time along parallel lifelines—Collaboration Diagrams prioritize the network layout of object relationships, showing links between objects and decorating those links with numbered directed message arrows.</p>

  <h4 class="answer-heading">2. Standard Terms and Graphical Notations</h4>
  <ul>
    <li><strong>Objects (Classifiers):</strong> Represented by rectangles containing underlined strings formatted as <code><u>objectName : ClassName</u></code>.</li>
    <li><strong>Links:</strong> Solid lines connecting collaborating objects, representing runtime instances of associations along which messages may flow.</li>
    <li><strong>Messages:</strong> Directed arrows parallel to link lines showing the direction of service invocation.</li>
    <li><strong>Sequence Expressions (Numbering Scheme):</strong> Hierarchical dot-notation specifying execution order and nested calling contexts:
      <ul>
        <li><code>1: authenticate()</code> - Top-level procedure.</li>
        <li><code>1.1: queryHash()</code> - Sub-operation invoked by procedure 1.</li>
        <li><code>1.2: compareTokens()</code> - Subsequent sub-operation in context 1.</li>
        <li><code>2: grantAccess()</code> - Subsequent top-level procedure.</li>
      </ul>
    </li>
    <li><strong>Conditional &amp; Iteration Guards:</strong> Prefixing messages with conditions like <code>[isValid == true] 3: unlock()</code> or iteration markers like <code>1.* [i:=1..n]: notify()</code>.</li>
  </ul>

  <h4 class="answer-heading">3. Describing Polymorphism in Collaboration Diagrams</h4>
  <p>Polymorphism is captured in collaboration diagrams by linking a sender object to an <strong>abstract classifier</strong> or polymorphic interface. At runtime, the receiver instance is bound to any concrete specialization without modifying the message signature or caller topology. For example, a <code>GraphicRenderer</code> dispatches <code>1: draw()</code> across a link to a polymorphic reference <code><u>shape : Shape</u></code>. The specific receiver object executes its overridden polymorphic implementation (e.g., <code>Circle::draw()</code> or <code>Square::draw()</code>).</p>

  <h4 class="answer-heading">4. High-Contrast Collaboration Diagram Demonstrating Polymorphism</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 660 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="660" height="220" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Sender Object -->
      <rect x="40" y="70" width="160" height="60" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="120" y="105" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>client : CanvasApp</u></text>

      <!-- Abstract Link -->
      <line x1="200" y1="100" x2="420" y2="100" stroke="#1f2328" stroke-width="1.5"/>
      
      <!-- Numbered Message Arrow -->
      <line x1="250" y1="85" x2="350" y2="85" stroke="#0969da" stroke-width="1.8"/>
      <polygon points="350,85 342,81 342,89" fill="#0969da"/>
      <text x="300" y="78" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">1: render()</text>

      <!-- Polymorphic Target Object -->
      <rect x="420" y="70" width="200" height="60" fill="#ffffff" stroke="#0969da" stroke-width="2"/>
      <text x="520" y="95" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>target : VectorShape</u></text>
      <text x="520" y="115" font-family="sans-serif" font-size="9" fill="#656d76" text-anchor="middle">{polymorphic: Circle / Polygon}</text>

      <!-- Notes explaining dynamic dispatch -->
      <text x="330" y="160" font-family="sans-serif" font-size="10" fill="#1f2328" text-anchor="middle">VTable resolves dynamically to concrete subclass implementation at runtime</text>
      <line x1="330" y1="140" x2="330" y2="110" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>
    </svg>
    <span class="diagram-caption">Figure U2-L04: Polymorphic Message Dispatch in a Collaboration Diagram</span>
  </div>

  <h4 class="answer-heading">5. Comprehensive Sequence vs. Collaboration Comparison</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Comparison Dimension</th>
        <th style="width: 37%;">Sequence Diagram</th>
        <th style="width: 38%;">Collaboration Diagram</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Dimension</strong></td>
        <td><strong>Time:</strong> Strict vertical chronology downward along object lifelines.</td>
        <td><strong>Space:</strong> Static network topology showing structural links between objects.</td>
      </tr>
      <tr>
        <td><strong>Message Sequencing</strong></td>
        <td>Implicit from top-to-bottom spatial positioning of message lines.</td>
        <td>Explicit via hierarchical decimal sequence numbers (e.g., <code>1.2.1: validate()</code>).</td>
      </tr>
      <tr>
        <td><strong>Object Creation / Deletion</strong></td>
        <td>Explicit: Object box placed lower on page; destruction marked with <code>X</code>.</td>
        <td>Marked textually using stereotypes (<code>&laquo;create&raquo;</code>, <code>&laquo;destroy&raquo;</code>).</td>
      </tr>
      <tr>
        <td><strong>Best Used For</strong></td>
        <td>Detailed procedural flows, timing analysis, and complex concurrency.</td>
        <td>Understanding architectural coupling, object clusters, and impact of refactoring.</td>
      </tr>
    </tbody>
  </table>

</div>
        """
    })

    # U2-L05
    questions.append({
        "id": "U2-L05",
        "unit": "2",
        "year": "2021-22",
        "year_display": "[2021-22]",
        "title": "Prepare a scenario in which everything is safely transported across the river (Farmer, Goat, Lion, Grass). Prepare the event trace diagram for the above problem.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Problem Formulation & Invariant Constraints</h4>
  <p>The classical <strong>River Crossing Problem</strong> involves four entities: a <code>Farmer</code>, a <code>Goat</code>, a <code>Lion</code> (Wolf), and <code>Grass</code> (Cabbage), initially all situated on Bank A. They must be transported across a river to Bank B using a small boat that can hold at most the Farmer and one passenger/item. The system is governed by critical hazard safety invariants:</p>
  <ul>
    <li><em>Hazard Invariant 1:</em> If the Farmer leaves Bank A/B, the Lion must not be left alone with the Goat (Lion will devour the Goat).</li>
    <li><em>Hazard Invariant 2:</em> If the Farmer leaves Bank A/B, the Goat must not be left alone with the Grass (Goat will eat the Grass).</li>
    <li><em>Safe Invariant:</em> The Lion does not eat Grass, and all entities are safe under the supervision of the Farmer.</li>
  </ul>

  <h4 class="answer-heading">2. Valid 7-Step Solution Scenario</h4>
  <ol>
    <li><strong>Trip 1 (A &rarr; B):</strong> Farmer transports Goat to Bank B. (Bank A: Lion, Grass; Bank B: Goat). Safe.</li>
    <li><strong>Trip 2 (B &rarr; A):</strong> Farmer returns alone in boat to Bank A. (Bank A: Farmer, Lion, Grass; Bank B: Goat). Safe.</li>
    <li><strong>Trip 3 (A &rarr; B):</strong> Farmer transports Lion to Bank B. (Bank A: Grass; Bank B: Lion, Goat, Farmer).</li>
    <li><strong>Trip 4 (B &rarr; A):</strong> Farmer brings Goat back to Bank A to avoid Lion-Goat clash! (Bank A: Farmer, Goat, Grass; Bank B: Lion). Safe.</li>
    <li><strong>Trip 5 (A &rarr; B):</strong> Farmer leaves Goat on Bank A and transports Grass to Bank B. (Bank A: Goat; Bank B: Farmer, Lion, Grass). Safe.</li>
    <li><strong>Trip 6 (B &rarr; A):</strong> Farmer returns alone in boat to Bank A. (Bank A: Farmer, Goat; Bank B: Lion, Grass). Safe.</li>
    <li><strong>Trip 7 (A &rarr; B):</strong> Farmer transports Goat to Bank B. (Bank A: Empty; Bank B: Farmer, Lion, Goat, Grass). All safely transported.</li>
  </ol>

  <h4 class="answer-heading">3. Clean Event Trace Diagram (Sequence Representation)</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 680 380" width="100%" height="380" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="380" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Lifelines: Farmer, Boat, Bank_A, Bank_B -->
      <!-- Farmer -->
      <rect x="40" y="20" width="100" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="90" y="40" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:Farmer</u></text>
      <line x1="90" y1="50" x2="90" y2="360" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <!-- Boat -->
      <rect x="200" y="20" width="100" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="250" y="40" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:Boat</u></text>
      <line x1="250" y1="50" x2="250" y2="360" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <!-- Bank A -->
      <rect x="360" y="20" width="110" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="415" y="40" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:Bank_A</u></text>
      <line x1="415" y1="50" x2="415" y2="360" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <!-- Bank B -->
      <rect x="530" y="20" width="110" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="585" y="40" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:Bank_B</u></text>
      <line x1="585" y1="50" x2="585" y2="360" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <!-- Step 1: Farmer transports Goat to B -->
      <line x1="90" y1="75" x2="250" y2="75" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="250,75 242,71 242,79" fill="#1f2328"/>
      <text x="170" y="70" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">1: load(Goat), crossToB()</text>

      <line x1="250" y1="90" x2="585" y2="90" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="585,90 577,86 577,94" fill="#1f2328"/>
      <text x="415" y="85" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">unload(Goat) at Bank B</text>

      <!-- Step 2: Return alone to A -->
      <line x1="90" y1="120" x2="250" y2="120" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="250,120 242,116 242,124" fill="#1f2328"/>
      <text x="170" y="115" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">2: returnAloneToA()</text>

      <!-- Step 3: Take Lion to B -->
      <line x1="90" y1="155" x2="250" y2="155" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="250,155 242,151 242,159" fill="#1f2328"/>
      <text x="170" y="150" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">3: load(Lion), crossToB()</text>

      <!-- Step 4: Swap Goat back to A -->
      <line x1="90" y1="195" x2="250" y2="195" stroke="#cf222e" stroke-width="1.5"/>
      <polygon points="250,195 242,191 242,199" fill="#cf222e"/>
      <text x="170" y="190" font-family="sans-serif" font-size="9" fill="#cf222e" text-anchor="middle">4: load(Goat), returnToA() [CRITICAL SWAP]</text>

      <!-- Step 5: Take Grass to B -->
      <line x1="90" y1="240" x2="250" y2="240" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="250,240 242,236 242,244" fill="#1f2328"/>
      <text x="170" y="235" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">5: load(Grass), crossToB()</text>

      <!-- Step 6: Return alone to A -->
      <line x1="90" y1="280" x2="250" y2="280" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="250,280 242,276 242,284" fill="#1f2328"/>
      <text x="170" y="275" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">6: returnAloneToA()</text>

      <!-- Step 7: Final crossing with Goat -->
      <line x1="90" y1="320" x2="585" y2="320" stroke="#1a7f37" stroke-width="1.8"/>
      <polygon points="585,320 577,316 577,324" fill="#1a7f37"/>
      <text x="337" y="315" font-family="sans-serif" font-size="9" font-weight="bold" fill="#1a7f37" text-anchor="middle">7: load(Goat), crossToB() [SUCCESS: ALL ENTITIES ON BANK B]</text>
    </svg>
    <span class="diagram-caption">Figure U2-L05: Event Trace Sequence Diagram for the River Crossing Problem</span>
  </div>

  <h4 class="answer-heading">4. State Invariant Formalization &amp; Hazard Matrix</h4>
  <p>The River Crossing problem is formally validated against the state constraint equation:</p>
  <pre class="code-block"><code>// Safety Hazard Condition
bool isHazardous(Location farmer, Location lion, Location goat, Location grass) {
    if (farmer != goat) {
        if (lion == goat) return true; // Lion devours Goat
        if (goat == grass) return true; // Goat devours Grass
    }
    return false; // Safe configuration
}</code></pre>
  <p>The sequence diagram illustrates how Step 4 (swapping the Goat back to Bank A) is the mandatory non-intuitive architectural maneuver required to prevent concurrent violation of both hazard invariants while progressing towards total system resolution.</p>

</div>
        """
    })

    # U2-L06
    questions.append({
        "id": "U2-L06",
        "unit": "2",
        "year": "2021-22",
        "year_display": "[2021-22]",
        "title": "Define the term multiplicity and quantification with suitable examples.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Multiplicity: Detailed Definition and Semantics</h4>
  <p>In structural modeling, <strong>Multiplicity</strong> defines the permissible cardinality—the lower and upper bounds on the number of object instances of a class that may participate in an association with a single instance of another class. It governs data integrity, collection semantics, and foreign key constraints in persistent schemas.</p>
  <p>Standard multiplicity specifications include:</p>
  <ul>
    <li><code>1</code> (Exactly one): Represents a mandatory, singular relationship (e.g., an <code>Employee</code> has exactly <code>1</code> tax ID profile).</li>
    <li><code>0..1</code> (Zero or one): Represents an optional singular relationship (e.g., a <code>Car</code> has <code>0..1</code> active <code>NavigationSystem</code>).</li>
    <li><code>*</code> or <code>0..*</code> (Many / Unbounded): Represents a variable-size collection (e.g., an <code>Author</code> writes <code>0..*</code> <code>Books</code>).</li>
    <li><code>1..*</code> (One or more): Represents a mandatory non-empty collection (e.g., a <code>Department</code> must employ at least <code>1..*</code> <code>Professors</code>).</li>
  </ul>

  <h4 class="answer-heading">2. Quantification (Qualified Association)</h4>
  <p><strong>Quantification</strong>—implemented in UML as a <strong>Qualified Association</strong>—is a structural modeling mechanism that partitions an association with high multiplicity (such as <code>1</code> to <code>0..*</code>) into an indexed lookup using a unique identifier called a <strong>Qualifier</strong>. The qualifier acts as a composite key or hash index, reducing the effective target multiplicity from <em>many</em> down to <code>0..1</code> (or exactly <code>1</code>).</p>

  <h4 class="answer-heading">3. Visual Representation: Unqualified vs. Qualified Association</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 640 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="640" height="180" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Source Class: Bank -->
      <rect x="30" y="50" width="150" height="70" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <rect x="30" y="50" width="150" height="25" fill="#f6f8fa" stroke="#1f2328" stroke-width="1"/>
      <text x="105" y="67" font-family="monospace" font-size="12" font-weight="bold" fill="#0969da" text-anchor="middle">Bank</text>
      <text x="40" y="95" font-family="monospace" font-size="10" fill="#1f2328">- bankName : String</text>

      <!-- Qualifier Box nested at target edge of Bank -->
      <rect x="180" y="68" width="120" height="34" fill="#f6f8fa" stroke="#0969da" stroke-width="1.5"/>
      <text x="240" y="89" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">accountNo : String</text>

      <!-- Association Line -->
      <line x1="300" y1="85" x2="450" y2="85" stroke="#1f2328" stroke-width="1.5"/>
      <text x="430" y="78" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da">0..1</text>

      <!-- Target Class: Account -->
      <rect x="450" y="50" width="150" height="70" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <rect x="450" y="50" width="150" height="25" fill="#f6f8fa" stroke="#1f2328" stroke-width="1"/>
      <text x="525" y="67" font-family="monospace" font-size="12" font-weight="bold" fill="#0969da" text-anchor="middle">Account</text>
      <text x="460" y="95" font-family="monospace" font-size="10" fill="#1f2328">- balance : Double</text>
    </svg>
    <span class="diagram-caption">Figure U2-L06: Qualified Association using accountNo Qualifier reducing Multiplicity to 0..1</span>
  </div>

  <h4 class="answer-heading">4. Architectural &amp; Implementation Mapping</h4>
  <p>In unqualified modeling, a <code>Bank</code> maintains <code>0..*</code> <code>Account</code> references, implemented via an unordered <code>std::vector&lt;Account*&gt;</code> requiring an $O(N)$ linear scan to look up an account. With a qualified association on <code>accountNo</code>, the relationship maps directly to an associative map (<code>std::unordered_map&lt;std::string, Account*&gt;</code>) yielding an optimal $O(1)$ constant-time lookup, demonstrating how quantification aligns design with data structures.</p>

  <h4 class="answer-heading">5. Formal OCL Specification of Multiplicity Invariants</h4>
  <p>Multiplicity constraints can be formally enforced using the <strong>Object Constraint Language (OCL)</strong>:</p>
  <pre class="code-block"><code>context Bank
inv ValidAccountCount:
    self.accounts->size() >= 0

context Bank::getAccount(accNo : String) : Account
post:
    result = self.accountMap.get(accNo)
    -- Multiplicity reduced from 0..* to 0..1 via qualifier key</code></pre>
  <p>Qualified associations eliminate lookup ambiguity by elevating primary lookup keys to the architectural level, preventing redundant iterations and ensuring strict unique identity constraints in domain schemas.</p>

</div>
        """
    })

    # U2-L07
    questions.append({
        "id": "U2-L07",
        "unit": "2",
        "year": "2021-22",
        "year_display": "[2021-22]",
        "title": "Explain generalization, aggregation and association in detail.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Detailed Conceptual Breakdown of the Three Core Relationships</h4>
  <p>Class diagrams model relationships among domain classifiers through three distinct structural primitives, each carrying distinct lifecycle, ownership, and behavioral semantics:</p>

  <h4 class="answer-heading">2. Detailed Comparative Analysis</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Relationship</th>
        <th style="width: 25%;">Semantic Meaning</th>
        <th style="width: 25%;">Lifecycle &amp; Ownership</th>
        <th style="width: 30%;">UML Graphical Notation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Generalization</strong></td>
        <td>"is-a" relationship connecting derived specialization to general base class.</td>
        <td>Strict compile-time taxonomic hierarchy; child inherits state and operations.</td>
        <td>Solid line with a <strong>large hollow triangular arrowhead</strong> pointing to parent base class.</td>
      </tr>
      <tr>
        <td><strong>Association</strong></td>
        <td>"peer-to-peer" structural connection; objects collaborate via messages.</td>
        <td>Completely independent lifecycles; destruction of one object does not affect the other.</td>
        <td>Solid line with optional multiplicity, role names, and navigation arrows.</td>
      </tr>
      <tr>
        <td><strong>Aggregation</strong><br>(Shared Composition)</td>
        <td>"has-a" or "part-of" whole/part relationship between container and parts.</td>
        <td><strong>Loose ownership:</strong> The child parts can exist independently of the parent aggregate whole.</td>
        <td>Solid line with a <strong>hollow (unfilled) diamond</strong> at the whole/aggregate end.</td>
      </tr>
      <tr>
        <td><strong>Composition</strong><br>(Composite Aggregation)</td>
        <td>Strict whole/part relationship with strong exclusive ownership.</td>
        <td><strong>Strict co-existence:</strong> Parts cannot exist without the whole; destruction of whole cascades to parts.</td>
        <td>Solid line with a <strong>solid (filled black) diamond</strong> at the whole/composite end.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. Concrete C++ Memory &amp; Lifecycle Implementation</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;vector&gt;
#include &lt;memory&gt;

// 1. Generalization Base Class
class HardwareDevice {
public:
    virtual ~HardwareDevice() = default;
    virtual void diagnose() = 0;
};

// 1. Generalization Child Class (is-a HardwareDevice)
class CPU : public HardwareDevice {
public:
    void diagnose() override { std::cout &lt;&lt; "CPU diagnostics OK\\n"; }
};

// 2. Class representing shared Aggregation component
class Monitor {
public:
    void display() { std::cout &lt;&lt; "Rendering display buffer\\n"; }
};

// 3. Whole Class illustrating Composition vs Aggregation
class ComputerSystem {
private:
    // COMPOSITION: CPU is owned exclusively; created and destroyed with ComputerSystem
    std::unique_ptr&lt;CPU&gt; internalCpu;

    // AGGREGATION: Monitor is shared; can exist independently of this computer
    Monitor* externalMonitor;

public:
    ComputerSystem(Monitor* extMon) 
        : internalCpu(std::make_unique&lt;CPU&gt;()), externalMonitor(extMon) {}

    // When ComputerSystem is destroyed, internalCpu is automatically freed,
    // but externalMonitor continues to exist in calling scope.
};</code></pre>

  <h4 class="answer-heading">4. Detailed Behavioral and Lifecycle Comparison Matrix</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Dimension</th>
        <th style="width: 25%;">Association</th>
        <th style="width: 25%;">Aggregation</th>
        <th style="width: 25%;">Composition</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Relationship Nature</strong></td>
        <td>Peer-to-peer relationship.</td>
        <td>Whole-part ("has-a").</td>
        <td>Strong whole-part ("owns-a").</td>
      </tr>
      <tr>
        <td><strong>Component Lifecycle</strong></td>
        <td>Independent lifecycles.</td>
        <td>Part can exist independently of whole.</td>
        <td>Part lifecycle strictly bound to whole.</td>
      </tr>
      <tr>
        <td><strong>C++ Implementation</strong></td>
        <td>Raw pointers / references.</td>
        <td>Pointers or <code>std::shared_ptr</code>.</td>
        <td>Member value objects or <code>std::unique_ptr</code>.</td>
      </tr>
      <tr>
        <td><strong>Cascading Delete</strong></td>
        <td>None.</td>
        <td>None (Part remains alive).</td>
        <td>Automatic recursive destruction of parts.</td>
      </tr>
    </tbody>
  </table>

</div>
        """
    })

    # U2-L08
    questions.append({
        "id": "U2-L08",
        "unit": "2",
        "year": "2022-23",
        "year_display": "[2022-23]",
        "title": "Discuss the purpose of UseCase Diagram and explain its different notations.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Purpose and Engineering Role of Use Case Diagrams</h4>
  <p>A <strong>Use Case Diagram</strong> is a behavioral UML diagram that provides a high-level visual summary of the system's functional requirements from the perspective of external entities. It models the system boundary, the external actors that interact with the system, and the discrete units of observable functionality (use cases) delivered to those actors.</p>
  <p>The primary engineering purposes of Use Case Diagrams include:</p>
  <ul>
    <li>Establishing the formal functional scope and boundary between the system and its operational environment.</li>
    <li>Facilitating unambiguous communication between technical software architects and non-technical business stakeholders.</li>
    <li>Serving as the foundational architectural driver for identifying domain classes, constructing system test plans, and estimating engineering effort.</li>
  </ul>

  <h4 class="answer-heading">2. Detailed Breakdown of Standard Use Case Notations</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Notation Element</th>
        <th style="width: 30%;">Visual Representation</th>
        <th style="width: 50%;">Semantic Meaning &amp; Usage Rules</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Actor</strong></td>
        <td>Stick figure icon (or class rectangle with <code>&laquo;actor&raquo;</code>).</td>
        <td>Represents an external entity (human user, external hardware peripheral, or third-party web service) that triggers system interactions to achieve a goal.</td>
      </tr>
      <tr>
        <td><strong>Use Case</strong></td>
        <td>Horizontal ellipse containing an active verb-noun phrase.</td>
        <td>A coherent sequence of actions performed by the system that yields an observable result of value to an actor (e.g., <code>Withdraw Cash</code>).</td>
      </tr>
      <tr>
        <td><strong>System Boundary</strong></td>
        <td>Large bounding rectangle enclosing use cases.</td>
        <td>Defines the physical scope of the software system under design. Actors reside strictly outside the boundary; use cases reside inside.</td>
      </tr>
      <tr>
        <td><strong>&laquo;include&raquo;</strong></td>
        <td>Dashed arrow pointing from base use case to included use case.</td>
        <td><strong>Mandatory sub-routine:</strong> The base use case cannot complete without executing the included functionality (e.g., <code>Withdraw Cash</code> &laquo;include&raquo; <code>Authenticate PIN</code>).</td>
      </tr>
      <tr>
        <td><strong>&laquo;extend&raquo;</strong></td>
        <td>Dashed arrow pointing from extension use case back to base use case.</td>
        <td><strong>Optional conditional behavior:</strong> Executes only when a specific extension condition is satisfied at designated extension points (e.g., <code>Print Receipt</code> &laquo;extend&raquo; <code>Withdraw Cash</code>).</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. High-Contrast UML Diagram: E-Commerce System</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 640 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="640" height="250" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- System Boundary Box -->
      <rect x="180" y="20" width="420" height="210" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <text x="200" y="40" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da">System: Online Store</text>

      <!-- Actor Customer -->
      <circle cx="70" cy="90" r="14" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="70" y1="104" x2="70" y2="140" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="45" y1="116" x2="95" y2="116" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="70" y1="140" x2="50" y2="175" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="70" y1="140" x2="90" y2="175" stroke="#1f2328" stroke-width="1.5"/>
      <text x="70" y="195" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1f2328" text-anchor="middle">Customer</text>

      <!-- Use Case: Place Order -->
      <ellipse cx="280" cy="85" rx="70" ry="25" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="280" y="90" font-family="monospace" font-size="10" font-weight="bold" fill="#1f2328" text-anchor="middle">Place Order</text>

      <!-- Actor to Base Use Case -->
      <line x1="95" y1="116" x2="210" y2="85" stroke="#1f2328" stroke-width="1.5"/>

      <!-- Use Case: Authenticate (Include) -->
      <ellipse cx="490" cy="85" rx="75" ry="25" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="490" y="90" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">Authenticate User</text>

      <!-- Include Arrow -->
      <line x1="350" y1="85" x2="415" y2="85" stroke="#0969da" stroke-width="1.5" stroke-dasharray="3,3"/>
      <polygon points="415,85 407,81 407,89" fill="#0969da"/>
      <text x="382" y="78" font-family="monospace" font-size="8" fill="#0969da" text-anchor="middle">&laquo;include&raquo;</text>

      <!-- Use Case: Apply Coupon (Extend) -->
      <ellipse cx="280" cy="180" rx="70" ry="25" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="280" y="185" font-family="monospace" font-size="10" font-weight="bold" fill="#656d76" text-anchor="middle">Apply Coupon</text>

      <!-- Extend Arrow -->
      <line x1="280" y1="155" x2="280" y2="110" stroke="#656d76" stroke-width="1.5" stroke-dasharray="3,3"/>
      <polygon points="280,110 276,118 284,118" fill="#656d76"/>
      <text x="235" y="135" font-family="monospace" font-size="8" fill="#656d76" text-anchor="middle">&laquo;extend&raquo;</text>
    </svg>
    <span class="diagram-caption">Figure U2-L08: UML Use Case Diagram Demonstrating &laquo;include&raquo; and &laquo;extend&raquo; Relationships</span>
  </div>

  <h4 class="answer-heading">4. Architectural Rules Governing &laquo;include&raquo; vs. &laquo;extend&raquo;</h4>
  <ul>
    <li><strong>Include Semantics (Mandatory Factoring):</strong> Used when a common chunk of behavior is shared across multiple use cases (e.g., both <code>Transfer Funds</code> and <code>View Balance</code> &laquo;include&raquo; <code>Authenticate User</code>). The base use case is functionally incomplete without the included behavior.</li>
    <li><strong>Extend Semantics (Conditional Extension):</strong> Used to model optional, exceptional, or auxiliary functionality that executes only when a specific boolean condition holds at an extension point (e.g., triggering a fraud investigation if an order exceeds $10,000). The base use case is completely functional on its own without the extending use case.</li>
    <li><strong>Actor Generalization:</strong> An actor can inherit from another actor (e.g., <code>Administrator</code> inherits from <code>Customer</code>), inheriting all associated use case interactions while gaining specialized administrative capabilities.</li>
  </ul>

</div>
        """
    })

    # U2-L09
    questions.append({
        "id": "U2-L09",
        "unit": "2",
        "year": "2022-23",
        "year_display": "[2022-23]",
        "title": "Demonstrate the different relationships used in class diagram with their notations with the help of a neat class diagram.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. The Spectrum of Relationships in Class Modeling</h4>
  <p>A UML Class Diagram captures the static semantic relationships connecting classifiers. These relationships vary from loose, temporary operational dependencies to permanent, composite lifecycles. There are six primary structural relationships standardized in UML:</p>
  <ul>
    <li><strong>Association:</strong> A bidirectional or unidirectional structural link between instances of two classes. Rendered as a solid line with optional multiplicities.</li>
    <li><strong>Aggregation (Shared):</strong> A "has-a" relationship where the child part can exist independently of the parent container. Rendered with an <strong>open/hollow diamond</strong> at the container end.</li>
    <li><strong>Composition (Composite Aggregation):</strong> A strict "part-of" relationship where child parts are owned exclusively and their lifecycles are tied to the parent. Rendered with a <strong>solid black diamond</strong>.</li>
    <li><strong>Generalization:</strong> An "is-a" taxonomic inheritance relationship connecting specialized subclasses to a parent base class. Rendered with a <strong>solid line ending in a hollow triangular arrowhead</strong>.</li>
    <li><strong>Realization:</strong> Contractual implementation relationship connecting a concrete class to an abstract interface. Rendered with a <strong>dashed line ending in a hollow triangular arrowhead</strong>.</li>
    <li><strong>Dependency:</strong> A weak "uses-a" relationship where changes to the supplier class impact the client class. Rendered with a <strong>dashed line ending in an open arrowhead</strong>.</li>
  </ul>

  <h4 class="answer-heading">2. Comprehensive Class Diagram Demonstrating All 6 Relationships</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 680 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="340" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Interface: Serializable -->
      <rect x="30" y="20" width="140" height="50" fill="#ffffff" stroke="#0969da" stroke-width="1.5"/>
      <text x="100" y="40" font-family="monospace" font-size="10" font-style="italic" fill="#0969da" text-anchor="middle">&laquo;interface&raquo;</text>
      <text x="100" y="55" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">Serializable</text>

      <!-- Base Class: Vehicle -->
      <rect x="250" y="20" width="160" height="60" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="330" y="45" font-family="monospace" font-size="12" font-style="italic" font-weight="bold" fill="#0969da" text-anchor="middle">Vehicle</text>
      <text x="330" y="65" font-family="monospace" font-size="10" fill="#1f2328" text-anchor="middle">+ startEngine() : void</text>

      <!-- Derived Class: Car -->
      <rect x="250" y="140" width="160" height="80" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <text x="330" y="165" font-family="monospace" font-size="12" font-weight="bold" fill="#0969da" text-anchor="middle">Car</text>
      <text x="330" y="185" font-family="monospace" font-size="10" fill="#cf222e">- vinNumber : String</text>
      <text x="330" y="205" font-family="monospace" font-size="10" fill="#1a7f37">+ drive() : void</text>

      <!-- Realization Arrow: Car realizes Serializable -->
      <line x1="250" y1="160" x2="170" y2="60" stroke="#0969da" stroke-width="1.5" stroke-dasharray="4,4"/>
      <polygon points="170,60 178,68 184,58" fill="#ffffff" stroke="#0969da" stroke-width="1.5"/>
      <text x="175" y="125" font-family="sans-serif" font-size="9" fill="#0969da">Realization</text>

      <!-- Generalization Arrow: Car inherits Vehicle -->
      <line x1="330" y1="140" x2="330" y2="80" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="330,80 324,92 336,92" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <text x="340" y="110" font-family="sans-serif" font-size="9" fill="#1f2328">Generalization</text>

      <!-- Composition: Car has Engine -->
      <rect x="470" y="140" width="140" height="60" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="540" y="165" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">Engine</text>
      <text x="540" y="185" font-family="monospace" font-size="10" fill="#1f2328" text-anchor="middle">- horsepower : Int</text>

      <!-- Composition Line with Solid Diamond -->
      <line x1="410" y1="170" x2="470" y2="170" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="410,170 418,165 426,170 418,175" fill="#1f2328" stroke="#1f2328"/>
      <text x="435" y="160" font-family="sans-serif" font-size="9" fill="#1f2328">Composition</text>

      <!-- Aggregation: Car has Wheel -->
      <rect x="470" y="240" width="140" height="60" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="540" y="265" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">Wheel</text>
      <text x="540" y="285" font-family="monospace" font-size="10" fill="#1f2328" text-anchor="middle">- tirePressure : Float</text>

      <!-- Aggregation Line with Hollow Diamond -->
      <line x1="330" y1="220" x2="330" y2="270" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="330" y1="270" x2="470" y2="270" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="330,220 325,228 330,236 335,228" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <text x="350" y="255" font-family="sans-serif" font-size="9" fill="#1f2328">Aggregation (4)</text>

      <!-- Dependency: Car depends on GPSLogger -->
      <rect x="30" y="240" width="140" height="60" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="100" y="265" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">GPSLogger</text>
      <text x="100" y="285" font-family="monospace" font-size="10" fill="#1f2328" text-anchor="middle">+ logPosition() : void</text>

      <!-- Dependency Line -->
      <line x1="250" y1="200" x2="170" y2="260" stroke="#656d76" stroke-width="1.5" stroke-dasharray="4,4"/>
      <polygon points="170,260 178,255 174,266" fill="#656d76"/>
      <text x="175" y="225" font-family="sans-serif" font-size="9" fill="#656d76">Dependency</text>
    </svg>
    <span class="diagram-caption">Figure U2-L09: UML Class Diagram Demonstrating All 6 Standard Relationships</span>
  </div>

  <h4 class="answer-heading">3. Comprehensive Structural Semantics &amp; Code Realization</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Relationship</th>
        <th style="width: 30%;">UML Notation</th>
        <th style="width: 50%;">C++ Code Realization Pattern</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Generalization</strong></td>
        <td>Solid line with hollow triangle.</td>
        <td><code>class Car : public Vehicle { ... };</code></td>
      </tr>
      <tr>
        <td><strong>Realization</strong></td>
        <td>Dashed line with hollow triangle.</td>
        <td><code>class Car : public Serializable { ... };</code></td>
      </tr>
      <tr>
        <td><strong>Composition</strong></td>
        <td>Solid line with filled black diamond.</td>
        <td><code>class Car { Engine eng; }; // By value or unique_ptr</code></td>
      </tr>
      <tr>
        <td><strong>Aggregation</strong></td>
        <td>Solid line with hollow diamond.</td>
        <td><code>class Car { Wheel* wheels[4]; }; // By pointer / reference</code></td>
      </tr>
      <tr>
        <td><strong>Dependency</strong></td>
        <td>Dashed line with open arrow.</td>
        <td><code>void Car::log(GPSLogger&amp; logger) { logger.log(); }</code></td>
      </tr>
    </tbody>
  </table>
  <p>Understanding these six relationships allows software architects to convey precise memory allocation, object lifecycle coupling, and compile-time versus runtime dependencies without ambiguity.</p>

</div>
        """
    })

    # U2-L10
    questions.append({
        "id": "U2-L10",
        "unit": "2",
        "year": "2022-23",
        "year_display": "[2022-23]",
        "title": "Illustrate the significance of collaboration diagram and also draw a neat collaboration diagram for reserving a room in a hotel from its website.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Significance of Collaboration Diagrams in System Design</h4>
  <p><strong>Collaboration Diagrams</strong> (Communication Diagrams in UML 2.0) provide a distinctive architectural perspective by projecting dynamic interactions directly upon the static structural topology of collaborating objects. Their primary engineering benefits include:</p>
  <ul>
    <li><strong>Structural Context Visualization:</strong> Rather than viewing execution lifelines in isolated columns, engineers observe how messages travel across physical object links, clearly illustrating object coupling and architectural cluster density.</li>
    <li><strong>Design Refactoring Insights:</strong> Highlight "hub" objects that receive an excessive concentration of messages, signaling a violation of Single Responsibility and suggesting refactoring towards the Mediator or Facade patterns.</li>
    <li><strong>Space Efficiency:</strong> Better suited than wide sequence diagrams for displaying compact object interactions on printed architectural documentation.</li>
  </ul>

  <h4 class="answer-heading">2. Case Study: Reserving a Hotel Room via Web Portal</h4>
  <p>The reservation workflow involves five collaborating runtime objects:</p>
  <ol>
    <li><code><u>webUser : Guest</u></code>: The browser client requesting a room reservation.</li>
    <li><code><u>portalUI : ReservationController</u></code>: Manages page transitions and coordinates business validation.</li>
    <li><code><u>inventoryMgr : RoomInventory</u></code>: Checks room availability and locks vacancy.</li>
    <li><code><u>paymentGW : PaymentProcessor</u></code>: Handles credit card authorization and payment settlement.</li>
    <li><code><u>notifier : EmailService</u></code>: Dispatches confirmation vouchers to the guest.</li>
  </ol>

  <h4 class="answer-heading">3. High-Contrast Collaboration Diagram</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 680 300" width="100%" height="300" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="300" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Object: Guest -->
      <rect x="30" y="110" width="130" height="50" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="95" y="140" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:Guest</u></text>

      <!-- Object: ReservationController (Central Hub) -->
      <rect x="250" y="110" width="180" height="50" fill="#ffffff" stroke="#0969da" stroke-width="2"/>
      <text x="340" y="140" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:ReservationCtrl</u></text>

      <!-- Message 1: submitBooking -->
      <line x1="160" y1="135" x2="250" y2="135" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="180" y1="125" x2="230" y2="125" stroke="#0969da" stroke-width="1.5"/>
      <polygon points="230,125 224,121 224,129" fill="#0969da"/>
      <text x="205" y="118" font-family="monospace" font-size="9" fill="#0969da" text-anchor="middle">1: bookRoom()</text>

      <!-- Object: RoomInventory (Top) -->
      <rect x="250" y="15" width="180" height="50" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="340" y="45" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:RoomInventory</u></text>

      <!-- Message 2: checkAvailability -->
      <line x1="340" y1="110" x2="340" y2="65" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="350" y1="100" x2="350" y2="75" stroke="#0969da" stroke-width="1.5"/>
      <polygon points="350,75 346,81 354,81" fill="#0969da"/>
      <text x="430" y="90" font-family="monospace" font-size="9" fill="#0969da">2: checkAndLock()</text>

      <!-- Object: PaymentProcessor (Right) -->
      <rect x="510" y="110" width="150" height="50" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="585" y="140" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:PaymentGW</u></text>

      <!-- Message 3: processPayment -->
      <line x1="430" y1="135" x2="510" y2="135" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="450" y1="125" x2="490" y2="125" stroke="#0969da" stroke-width="1.5"/>
      <polygon points="490,125 484,121 484,129" fill="#0969da"/>
      <text x="470" y="118" font-family="monospace" font-size="9" fill="#0969da" text-anchor="middle">3: chargeCard()</text>

      <!-- Object: EmailService (Bottom) -->
      <rect x="250" y="215" width="180" height="50" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="340" y="245" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:EmailService</u></text>

      <!-- Message 4: sendConfirmation -->
      <line x1="340" y1="160" x2="340" y2="215" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="330" y1="175" x2="330" y2="200" stroke="#0969da" stroke-width="1.5"/>
      <polygon points="330,200 326,194 334,194" fill="#0969da"/>
      <text x="250" y="190" font-family="monospace" font-size="9" fill="#0969da">4: sendVoucher()</text>
    </svg>
    <span class="diagram-caption">Figure U2-L10: Collaboration Diagram for Online Hotel Room Reservation Workflow</span>
  </div>

  <h4 class="answer-heading">4. Step-by-Step Message Trace &amp; Business Rules</h4>
  <ol>
    <li><code>1: bookRoom(dates, roomType)</code>: The Guest initiates the booking request via the web frontend.</li>
    <li><code>2: checkAndLock(dates, roomType)</code>: The controller verifies room availability in the inventory database and places a temporary 10-minute hold on the selected room.</li>
    <li><code>3: chargeCard(paymentInfo, amount)</code>: The controller requests credit card authorization from the payment gateway. If successful, payment confirmation token is returned.</li>
    <li><code>4: sendVoucher(reservationDetails)</code>: The controller triggers the email service to dispatch a confirmed booking voucher and invoice to the guest's email address.</li>
  </ol>
  <p>This layout clearly demonstrates the <strong>Controller Pattern</strong> (GRASP), where <code>ReservationController</code> acts as the central coordinator delegating tasks to domain entities and infrastructure services.</p>


  <h4 class="answer-heading">5. Concurrency &amp; Rollback Mechanics in Hotel Bookings</h4>
  <p>In distributed hotel reservation portals, the collaboration between <code>ReservationCtrl</code>, <code>RoomInventory</code>, and <code>PaymentGW</code> must account for distributed failure modes:</p>
  <ul>
    <li><strong>Inventory Lock Expiration:</strong> When <code>2: checkAndLock()</code> succeeds, a TTL (Time-To-Live) timer of 600 seconds is attached to the temporary reservation. If payment confirmation message <code>3: chargeCard()</code> does not arrive before timer expiry, the inventory manager automatically releases the locked room back to the public pool.</li>
    <li><strong>Two-Phase Compensating Transactions (Saga Pattern):</strong> If credit card authorization fails, message <code>3.1: unlockRoom()</code> is immediately sent to rollback the locked vacancy, preventing ghost reservations and maintaining zero inventory corruption.</li>
  </ul>

</div>
        """
    })

    # U2-L11
    questions.append({
        "id": "U2-L11",
        "unit": "2",
        "year": "2023-24",
        "year_display": "[2023-24]",
        "title": "What do you understand by architectural modeling? Explain its various concepts and diagrams with suitable example.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Concept and Foundations of Architectural Modeling</h4>
  <p><strong>Architectural Modeling</strong> in UML represents the high-level structural and operational organization of a software system. While class and state diagrams model fine-grained internal mechanisms, architectural modeling abstracts away algorithmic minutiae to focus on modular packaging, physical deployment topologies, subsystem boundaries, network communication protocols, and physical hardware node mapping.</p>

  <h4 class="answer-heading">2. Key Concepts in Architectural Modeling</h4>
  <ul>
    <li><strong>Components:</strong> Modular, replaceable software units of independent deployment (JAR files, dynamic link libraries DLLs, microservice containers) that encapsulate implementation behind defined interfaces.</li>
    <li><strong>Nodes:</strong> Computational physical hardware resources (e.g., bare-metal servers, virtual machines, cloud instances, sensor arrays) possessing processing memory and runtime execution environments.</li>
    <li><strong>Artifacts:</strong> Concrete physical files residing on a node (executable binaries, configuration scripts, SQL databases).</li>
    <li><strong>Interfaces (Provided vs. Required):</strong> Provided interfaces ("lollipop" notation) declare operations the component exports to the system. Required interfaces ("socket" notation) declare dependencies the component requires from other modules.</li>
  </ul>

  <h4 class="answer-heading">3. The Two Core Architectural Diagrams</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Diagram Type</th>
        <th style="width: 37%;">Component Diagram</th>
        <th style="width: 38%;">Deployment Diagram</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Focus</strong></td>
        <td>Software modularization, physical code units, library dependencies.</td>
        <td>Physical hardware topology, cloud virtual nodes, network protocols.</td>
      </tr>
      <tr>
        <td><strong>Core Notations</strong></td>
        <td>Components, packages, provided interfaces, required sockets.</td>
        <td>3D cuboid Nodes, communication paths, deployed artifact files.</td>
      </tr>
      <tr>
        <td><strong>Target Audience</strong></td>
        <td>Software architects, component developers, build engineers.</td>
        <td>Systems engineers, DevOps/SRE teams, infrastructure managers.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">4. Architectural Example: Distributed E-Commerce Architecture</h4>
  <p>A distributed retail platform decomposes into: (1) Component tier where an <code>OrderProcessingComponent</code> provides a <code>BillingAPI</code> while requiring an <code>InventoryAPI</code>; (2) Deployment tier mapping these container artifacts onto an AWS Elastic Kubernetes Cluster connected via TLS 1.3 to a managed Amazon RDS PostgreSQL cluster.</p>

  <h4 class="answer-heading">5. Structural Hierarchy of Architectural Artifacts</h4>
  <p>Architectural modeling enforces a multi-tiered hierarchy of abstraction:</p>
  <ul>
    <li><strong>Subsystem Decomposition:</strong> High-level functional modules (e.g., <code>BillingSubsystem</code>, <code>InventorySubsystem</code>) organized into cohesive packages.</li>
    <li><strong>Component Packaging:</strong> Translating subsystem designs into physical software artifacts (JAR files, dynamic libraries, Docker containers) with strict interface contracts.</li>
    <li><strong>Node Allocation:</strong> Mapping software components to physical hardware topologies, specifying cloud regions, Kubernetes pods, and network protocols (gRPC, TLS, REST) to satisfy non-functional performance and disaster recovery requirements.</li>
  </ul>


  <h4 class="answer-heading">6. Comprehensive Comparison: Component vs. Deployment Models</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Architectural Metric</th>
        <th style="width: 37%;">Component Diagram</th>
        <th style="width: 38%;">Deployment Diagram</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Question Answered</strong></td>
        <td>What are the modular software building blocks, packages, and code interfaces?</td>
        <td>Where are software artifacts physically deployed and executed across hardware nodes?</td>
      </tr>
      <tr>
        <td><strong>Key Graphical Elements</strong></td>
        <td>Components with interface ports ("lollipop" for provided, "socket" for required).</td>
        <td>3D cuboid Nodes representing servers, containers, networks, and storage devices.</td>
      </tr>
      <tr>
        <td><strong>Lifecycle Association</strong></td>
        <td>Build-time, integration-time, packaging, and binary versioning.</td>
        <td>Runtime execution, network topology, high availability, and failover routing.</td>
      </tr>
    </tbody>
  </table>

</div>
        """
    })

    # U2-L12
    questions.append({
        "id": "U2-L12",
        "unit": "2",
        "year": "2023-24",
        "year_display": "[2023-24]",
        "title": "Explain class and object diagrams with examples.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Detailed Comparison: Class Diagrams vs. Object Diagrams</h4>
  <p>In object-oriented analysis and design, <strong>Class Diagrams</strong> and <strong>Object Diagrams</strong> represent the static structural viewpoint of a system at two distinct meta-levels:</p>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Dimension</th>
        <th style="width: 40%;">Class Diagram (Compile-Time Blueprint)</th>
        <th style="width: 40%;">Object Diagram (Runtime Snapshot)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Nature of Model</strong></td>
        <td>Abstract, compile-time classifier schema representing all possible states.</td>
        <td>Concrete, runtime instance graph capturing a frozen snapshot at time $t$.</td>
      </tr>
      <tr>
        <td><strong>Entity Naming</strong></td>
        <td>Plain class name in bold (e.g., <code>BankAccount</code>).</td>
        <td>Underlined instance identifier: <code><u>acc101 : BankAccount</u></code>.</td>
      </tr>
      <tr>
        <td><strong>Attributes</strong></td>
        <td>Lists attribute names with types and visibility (<code>- balance : double</code>).</td>
        <td>Lists specific bound runtime values (<code>balance = 5420.50</code>).</td>
      </tr>
      <tr>
        <td><strong>Operations</strong></td>
        <td>Exhaustively declares all public and private member methods.</td>
        <td>Operations are completely omitted (objects possess values, not signatures).</td>
      </tr>
      <tr>
        <td><strong>Relationships</strong></td>
        <td>Associations with multiplicities (<code>1..*</code>), aggregations, generalizations.</td>
        <td>Concrete Links (individual instances of associations without multiplicity).</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">2. Comprehensive Example: University Enrollment</h4>
  <p>Consider a university course registration scenario:</p>
  <ul>
    <li><em>Class Diagram View:</em> Class <code>Department</code> associates with Class <code>Course</code> (multiplicity <code>1</code> to <code>1..*</code>), which in turn associates with Class <code>Student</code> (multiplicity <code>0..*</code> to <code>1..*</code>).</li>
    <li><em>Object Diagram View:</em> At 10:00 AM on Monday, we capture snapshot <code><u>csDept : Department</u></code> linked to <code><u>cs101 : Course</u></code> (attribute <code>courseName = "Algorithms"</code>). Course <code>cs101</code> has active links to two runtime student instances: <code><u>alice : Student</u></code> (<code>gpa = 3.9</code>) and <code><u>bob : Student</u></code> (<code>gpa = 3.6</code>).</li>
  </ul>

  <h4 class="answer-heading">3. C++ Realization Demonstrating the Shift</h4>
  <pre class="code-block"><code>// The Class Blueprint (Class Diagram)
class Student {
public:
    std::string name;
    double gpa;
    Student(std::string n, double g) : name(std::move(n)), gpa(g) {}
};

int main() {
    // The Object Instances at runtime (Object Diagram Snapshot)
    Student alice("Alice Smith", 3.9); // 0x7ffd10
    Student bob("Bob Jones", 3.6);     // 0x7ffd28
    return 0;
}</code></pre>

  <h4 class="answer-heading">4. Why Both Diagrams Are Essential in System Verification</h4>
  <p>Neither diagram is sufficient on its own during complex system engineering:</p>
  <ul>
    <li><strong>Class Diagrams</strong> define the static taxonomy, type safety constraints, and possible relationship structures across the entire application domain. However, they cannot illustrate specific runtime graph configurations, dynamic object linking, or memory aliasing bugs.</li>
    <li><strong>Object Diagrams</strong> serve as empirical "test cases" for class models. Software architects draw object diagrams to simulate complex edge cases (e.g., circular references, recursive tree structures, or orphan objects) to verify whether the proposed class model legally permits or incorrectly prevents specific runtime configurations.</li>
  </ul>

</div>
        """
    })

    # U2-L13
    questions.append({
        "id": "U2-L13",
        "unit": "2",
        "year": "2023-24",
        "year_display": "[2023-24]",
        "title": "Prepare a portion of an object diagram for a library book checkout system that shows the date a book is due and the late charges for an overdue book as derived objects.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Conceptual Foundations: Derived Attributes &amp; Derived Objects</h4>
  <p>In UML, a <strong>Derived Element</strong> (denoted by a leading slash prefix <code>/</code>) is an attribute, link, or object whose value is not stored independently as an authoritative primary state, but is dynamically calculated or derived at runtime from other foundational base attributes or associations. In a library loan system:</p>
  <ul>
    <li><strong><code>dueDate</code> (Derived Attribute <code>/dueDate</code>):</strong> Derived dynamically by adding loan duration (e.g., 14 days) to the foundational <code>checkoutDate</code>.</li>
    <li><strong><code>lateFeeCharge</code> (Derived Object / Attribute <code>/lateCharge</code>):</strong> An overdue penalty computed by evaluating the expression: $\max(0, \text{currentDate} - \text{dueDate}) \times \text{dailyFineRate}$. If the difference is zero or negative, no fee object exists.</li>
  </ul>

  <h4 class="answer-heading">2. High-Contrast Object Diagram Snapshot</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 660 250" width="100%" height="250" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="660" height="250" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Object: Patron -->
      <rect x="30" y="80" width="150" height="75" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="105" y="105" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>patron42 : Member</u></text>
      <line x1="30" y1="115" x2="180" y2="115" stroke="#1f2328" stroke-width="1"/>
      <text x="40" y="132" font-family="monospace" font-size="9" fill="#1f2328">memberId = "M-902"</text>
      <text x="40" y="146" font-family="monospace" font-size="9" fill="#1f2328">name = "Jane Doe"</text>

      <!-- Link to Loan Record -->
      <line x1="180" y1="115" x2="250" y2="115" stroke="#1f2328" stroke-width="1.5"/>

      <!-- Object: LoanRecord (With Derived Date) -->
      <rect x="250" y="60" width="180" height="110" fill="#ffffff" stroke="#0969da" stroke-width="2"/>
      <text x="340" y="82" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>loan01 : LoanRecord</u></text>
      <line x1="250" y1="92" x2="430" y2="92" stroke="#0969da" stroke-width="1"/>
      <text x="260" y="110" font-family="monospace" font-size="9" fill="#1f2328">checkoutDate = 2026-09-01</text>
      <text x="260" y="126" font-family="monospace" font-size="9" fill="#1f2328">loanPeriodDays = 14</text>
      <text x="260" y="144" font-family="monospace" font-size="9" font-weight="bold" fill="#0969da">/dueDate = 2026-09-15</text>
      <text x="260" y="160" font-family="monospace" font-size="9" font-weight="bold" fill="#cf222e">/daysOverdue = 9</text>

      <!-- Derived Link to LateCharge Object -->
      <line x1="430" y1="115" x2="490" y2="115" stroke="#cf222e" stroke-width="1.5" stroke-dasharray="3,3"/>

      <!-- Derived Object: LateFee -->
      <rect x="490" y="70" width="150" height="90" fill="#f6f8fa" stroke="#cf222e" stroke-width="1.5" stroke-dasharray="4,4"/>
      <text x="565" y="95" font-family="monospace" font-size="10" font-weight="bold" fill="#cf222e" text-anchor="middle"><u>/fee : OverdueFine</u></text>
      <line x1="490" y1="105" x2="640" y2="105" stroke="#cf222e" stroke-width="1"/>
      <text x="500" y="123" font-family="monospace" font-size="9" fill="#cf222e">/ratePerDay = $1.50</text>
      <text x="500" y="141" font-family="monospace" font-size="9" font-weight="bold" fill="#cf222e">/totalFine = $13.50</text>
    </svg>
    <span class="diagram-caption">Figure U2-L13: Object Diagram Snapshot Illustrating Derived Attributes (/dueDate) and Derived Fine Object</span>
  </div>

  <h4 class="answer-heading">3. Formal Derivation Rules</h4>
  <p>The derived properties are formally governed by Object Constraint Language (OCL) rules:</p>
  <ul>
    <li><code>context LoanRecord::dueDate : Date = checkoutDate + loanPeriodDays</code></li>
    <li><code>context LoanRecord::totalFine : Real = if (currentDate &gt; dueDate) then (currentDate - dueDate) * dailyRate else 0.0 endif</code></li>
  </ul>

  <h4 class="answer-heading">4. Comprehensive C++ Realization of Derived Logic</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;algorithm&gt;

class LoanRecord {
private:
    std::string loanId;
    int checkoutDay;     // Stored base state
    int loanPeriodDays;  // Stored base state
    double dailyFineRate;

public:
    LoanRecord(std::string id, int checkDay, int period, double rate)
        : loanId(std::move(id)), checkoutDay(checkDay), 
          loanPeriodDays(period), dailyFineRate(rate) {}

    // Derived Attribute: /dueDate (computed on-the-fly)
    int getDueDate() const {
        return checkoutDay + loanPeriodDays;
    }

    // Derived Attribute / Object: /lateFine (computed on-the-fly)
    double calculateLateFine(int currentDay) const {
        int overdueDays = std::max(0, currentDay - getDueDate());
        return overdueDays * dailyFineRate;
    }
};

int main() {
    LoanRecord loan("LN-1001", 1, 14, 1.50); // Day 1 checkout, 14 day period, $1.50/day
    int currentDay = 24; // Day 24 (9 days overdue)

    std::cout << "Due Day: Day " << loan.getDueDate() << "\n";
    std::cout << "Derived Late Fee: $" << loan.calculateLateFine(currentDay) << "\n";
    return 0;
}</code></pre>


  <h4 class="answer-heading">5. Derived Objects vs. Derived Attributes: Conceptual Contrast</h4>
  <p>In UML, the distinction between a derived attribute and a derived object is subtle yet critical:</p>
  <ul>
    <li><strong>Derived Attribute (<code>/dueDate</code>):</strong> A singular scalar property computed directly from primitive attributes within the same class (e.g., adding days to a date). It does not require a distinct identity.</li>
    <li><strong>Derived Object (<code>/fee : OverdueFine</code>):</strong> An entire autonomous object instance instantiated conditionally when derived business rules are satisfied (e.g., when a book is overdue past its grace period). The derived object maintains its own identity, encapsulates fine calculation algorithms, tracks fine payment status (<code>Unpaid</code>, <code>Waived</code>, <code>Paid</code>), and is linked to the patron's account.</li>
  </ul>

</div>
        """
    })

    # U2-L14
    questions.append({
        "id": "U2-L14",
        "unit": "2",
        "year": "2024-25",
        "year_display": "[2024-25]",
        "title": "Draw an interaction diagram for a customer service chatbot system. Include time-based interactions and describe how they facilitate system understanding.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Architectural Context: Customer Service Chatbot System</h4>
  <p>Modern automated customer service platforms utilize Natural Language Processing (NLP) microservices, session managers, and knowledge bases to interact with human users in real time. Because network round-trips to large language models or intent classifiers are inherently variable in latency, <strong>Sequence Diagrams</strong> are critical to model time-based interactions, including typing indicators, asynchronous polling, timeouts, and fallback routing to human agents.</p>

  <h4 class="answer-heading">2. High-Contrast Sequence Diagram with Time-Based Latencies</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 680 360" width="100%" height="360" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="360" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Lifelines: User, ChatbotUI, NLPService, KnowledgeBase -->
      <rect x="40" y="20" width="100" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="90" y="40" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:Customer</u></text>
      <line x1="90" y1="50" x2="90" y2="340" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <rect x="200" y="20" width="110" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="255" y="40" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:ChatGateway</u></text>
      <line x1="255" y1="50" x2="255" y2="340" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <rect x="380" y="20" width="110" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="435" y="40" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:NLP_Engine</u></text>
      <line x1="435" y1="50" x2="435" y2="340" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <rect x="540" y="20" width="110" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="595" y="40" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:KnowledgeDB</u></text>
      <line x1="595" y1="50" x2="595" y2="340" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <!-- Message 1: User sends prompt -->
      <line x1="90" y1="75" x2="255" y2="75" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="255,75 247,71 247,79" fill="#1f2328"/>
      <text x="172" y="70" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">1: postMessage("Track Order")</text>

      <!-- Immediate ack with typing indicator -->
      <line x1="255" y1="100" x2="90" y2="100" stroke="#0969da" stroke-width="1.5" stroke-dasharray="3,3"/>
      <polygon points="90,100 98,96 98,104" fill="#0969da"/>
      <text x="172" y="95" font-family="sans-serif" font-size="9" fill="#0969da" text-anchor="middle">showTypingIndicator() [t = 50ms]</text>

      <!-- Async dispatch to NLP -->
      <line x1="255" y1="130" x2="435" y2="130" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="435,130 427,126 427,134" fill="#1f2328"/>
      <text x="345" y="125" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">2: parseIntent(text)</text>

      <!-- Activation Bar for NLP Processing -->
      <rect x="430" y="130" width="10" height="90" fill="#d0d7de" stroke="#1f2328" stroke-width="1"/>

      <!-- KB Query -->
      <line x1="440" y1="160" x2="595" y2="160" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="595,160 587,156 587,164" fill="#1f2328"/>
      <text x="517" y="155" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">3: queryKB("OrderTracking")</text>

      <!-- KB Return -->
      <line x1="595" y1="190" x2="440" y2="190" stroke="#1f2328" stroke-width="1.5" stroke-dasharray="3,3"/>
      <polygon points="440,190 448,186 448,194" fill="#1f2328"/>
      <text x="517" y="185" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">return trackingProcedure</text>

      <!-- NLP response to Gateway -->
      <line x1="435" y1="220" x2="255" y2="220" stroke="#1f2328" stroke-width="1.5" stroke-dasharray="3,3"/>
      <polygon points="255,220 263,216 263,224" fill="#1f2328"/>
      <text x="345" y="215" font-family="sans-serif" font-size="9" fill="#1f2328" text-anchor="middle">return intentResult [Latency: 450ms]</text>

      <!-- Gateway pushes response to user -->
      <line x1="255" y1="260" x2="90" y2="260" stroke="#1a7f37" stroke-width="1.8"/>
      <polygon points="90,260 98,256 98,264" fill="#1a7f37"/>
      <text x="172" y="255" font-family="sans-serif" font-size="9" font-weight="bold" fill="#1a7f37" text-anchor="middle">4: renderResponse("Enter Tracking #")</text>

      <!-- Timeout constraint annotation -->
      <line x1="30" y1="75" x2="30" y2="260" stroke="#cf222e" stroke-width="1.5"/>
      <line x1="25" y1="75" x2="35" y2="75" stroke="#cf222e" stroke-width="1.5"/>
      <line x1="25" y1="260" x2="35" y2="260" stroke="#cf222e" stroke-width="1.5"/>
      <text x="15" y="170" font-family="monospace" font-size="8" fill="#cf222e" transform="rotate(-90 15,170)" text-anchor="middle">{timeout: &lt; 2000ms}</text>
    </svg>
    <span class="diagram-caption">Figure U2-L14: Interaction Sequence Diagram for Customer Service Chatbot with Latency Markers</span>
  </div>

  <h4 class="answer-heading">3. How Time-Based Interactions Facilitate System Understanding</h4>
  <ul>
    <li><strong>SLA &amp; Timeout Verification:</strong> Visualizing explicit duration constraints (e.g., <code>{t &lt; 2000ms}</code>) guides developers in implementing asynchronous worker threads and fallback circuit-breakers if NLP latency spikes.</li>
    <li><strong>Concurrency &amp; Race Condition Prevention:</strong> Clearly indicates when lifelines are actively executing inside activation bars versus waiting in passive blocking states.</li>
  </ul>

  <h4 class="answer-heading">4. Asynchronous NLP Pipelines &amp; Timeout Recovery</h4>
  <p>In production customer service platforms, chatbot interactions require disciplined timing management:</p>
  <ul>
    <li><strong>Immediate Acknowledgment:</strong> To ensure optimal user experience, the system pushes a typing indicator or acknowledgment within 50ms, preventing user abandonment.</li>
    <li><strong>Asynchronous Intent Classification:</strong> Natural language processing (tokenization, intent classification, entity extraction) runs on detached GPU worker nodes. The gateway manages asynchronous polling or websocket streams to receive results.</li>
    <li><strong>Circuit-Breaker &amp; Human Fallback:</strong> If the NLP pipeline latency exceeds the hard timeout threshold (2000ms) or confidence falls below 0.65, the gateway gracefully routes the user session to an active human customer service representative.</li>
  </ul>


  <h4 class="answer-heading">5. Detailed NLP Interaction Step Breakdown</h4>
  <ol>
    <li><code>1: postMessage()</code>: The customer enters a free-form natural language query into the browser client widget.</li>
    <li><code>1.1: renderTyping()</code>: The chat gateway asynchronously pushes a typing indicator to maintain user engagement while heavy backend processing occurs.</li>
    <li><code>2: parseIntent()</code>: The message payload is transmitted to the NLP service running transformer models to extract intents and entity slots (e.g., intent: <code>TRACK_PACKAGE</code>, entity: <code>ORDER_NUM</code>).</li>
    <li><code>3: queryKnowledgeBase()</code>: The identified intent triggers a semantic vector search across the knowledge database to fetch verified enterprise response templates.</li>
    <li><code>4: renderResponse()</code>: The gateway delivers the finalized conversational response back to the customer, logging session latency metrics for system monitoring.</li>
  </ol>

</div>
        """
    })

    # U2-L15
    questions.append({
        "id": "U2-L15",
        "unit": "2",
        "year": "2024-25",
        "year_display": "[2024-25]",
        "title": "Create a C++ program that uses a callback mechanism. Explain how callbacks are implemented in C++ using function pointers or lambda expressions.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Conceptual Foundations of the Callback Mechanism</h4>
  <p>A <strong>Callback</strong> is a software design pattern where executable code is passed as an argument to a receiving function, which is expected to "call back" (execute) that argument at a designated time. Callbacks decouple high-level asynchronous event producers (e.g., download managers, button listeners, timer loops) from specific consumer event-handling algorithms.</p>
  <p>In C++, callbacks are implemented via three evolutionary techniques:</p>
  <ul>
    <li><strong>C-Style Function Pointers:</strong> Fast with zero memory overhead, but cannot capture surrounding lexical state.</li>
    <li><strong>Standard Function Wrappers (<code>std::function&lt;Signature&gt;</code>):</strong> Type-safe polymorphic wrapper that can store functions, functors, or lambdas.</li>
    <li><strong>C++ Modern Lambda Expressions:</strong> Anonymous closures capable of capturing local context variables by value (<code>[=]</code>) or reference (<code>[&amp;]</code>).</li>
  </ul>

  <h4 class="answer-heading">2. Industrial C++ Implementation: Asynchronous Sensor Monitor</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;functional&gt;
#include &lt;string&gt;
#include &lt;vector&gt;

// Sensor Reading Data Payload
struct SensorData {
    std::string sensorId;
    double temperatureCelsius;
    bool thresholdExceeded;
};

// Publisher Class that invokes registered callbacks
class TemperatureSensor {
public:
    // Type definition for Modern C++ Callback using std::function
    using AlertCallback = std::function&lt;void(const SensorData&amp;)&gt;;

private:
    std::string id;
    double alarmLimit;
    std::vector&lt;AlertCallback&gt; listeners;

public:
    TemperatureSensor(std::string sensorId, double limit)
        : id(std::move(sensorId)), alarmLimit(limit) {}

    // Register callback subscribers
    void registerListener(AlertCallback callback) {
        listeners.push_back(std::move(callback));
    }

    // Simulate reading acquisition and trigger callbacks
    void updateReading(double currentTemp) {
        SensorData data{id, currentTemp, (currentTemp &gt;= alarmLimit)};

        if (data.thresholdExceeded) {
            std::cout &lt;&lt; "\\n[ALARM TRIGGERED] Sensor: " &lt;&lt; id 
                      &lt;&lt; " reported " &lt;&lt; currentTemp &lt;&lt; " C!\\n";
            // Dispatch to all registered callback handlers
            for (const auto&amp; listener : listeners) {
                listener(data);
            }
        }
    }
};

// Free function callback (Function Pointer equivalent)
void logToFile(const SensorData&amp; data) {
    std::cout &lt;&lt; "  -&gt; [File Logger]: Appended alert for " 
              &lt;&lt; data.sensorId &lt;&lt; " to audit_log.txt\\n";
}

int main() {
    TemperatureSensor boilerSensor("BOILER-04", 95.0);

    // Technique 1: Registering Free Function
    boilerSensor.registerListener(logToFile);

    // Technique 2: Registering C++ Lambda with Lexical State Capture
    int alertCounter = 0;
    std::string operatorPager = "+1-555-908-1122";

    boilerSensor.registerListener([&amp;alertCounter, operatorPager](const SensorData&amp; data) {
        alertCounter++;
        std::cout &lt;&lt; "  -&gt; [SMS Gateway]: Dispatched SMS to " &lt;&lt; operatorPager 
                  &lt;&lt; " | Total incidents today: " &lt;&lt; alertCounter &lt;&lt; "\\n";
    });

    // Simulate Operational Readings
    boilerSensor.updateReading(72.0);  // Normal: No callbacks fired
    boilerSensor.updateReading(98.5);  // Limit exceeded: Both callbacks execute!
    boilerSensor.updateReading(102.1); // Limit exceeded: Both callbacks execute!

    return 0;
}</code></pre>

  <h4 class="answer-heading">3. Detailed Execution Analysis</h4>
  <p>When temperature reaches 98.5&deg;C, the sensor loops through its registered callback array. The first callback executes <code>logToFile()</code>, writing to the simulated audit log. The second callback invokes the lambda expression, which accesses <code>alertCounter</code> by reference, increments it, and dispatches the alert to the operator pager without the sensor having any compile-time dependency on SMS gateways.</p>
</div>
        """
    })

    # U2-L16
    questions.append({
        "id": "U2-L16",
        "unit": "2",
        "year": "2024-25",
        "year_display": "[2024-25]",
        "title": "Develop a UML class diagram for a hospital management system. Explain the rationale behind your design choices.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. System Decomposition &amp; Architectural Rationale</h4>
  <p>A comprehensive <strong>Hospital Management System (HMS)</strong> must decouple administrative human resources, clinical medical interactions, inpatient bed occupancy, and accounting billing pipelines. To ensure security, extensibility, and maintainability, our design employs three core architectural principles:</p>
  <ul>
    <li><strong>Taxonomic Generalization:</strong> Common attributes (name, national ID, contact details) are abstracted into an abstract parent class <code>Person</code>, specialized into <code>Patient</code>, <code>Doctor</code>, and <code>Nurse</code>.</li>
    <li><strong>Association Class (Reification):</strong> Rather than directly connecting <code>Doctor</code> and <code>Patient</code> in an ambiguous many-to-many relationship, the interaction is reified into an <code>Appointment</code> association class that encapsulates time, clinical outcome, and consultation fees.</li>
    <li><strong>Composite Aggregation for Patient Inpatient Stays:</strong> A <code>Ward</code> exhibits composite ownership over its individual <code>Bed</code> units; if a ward is decommissioned, its assigned bed slots are terminated.</li>
  </ul>

  <h4 class="answer-heading">2. High-Contrast UML Class Diagram: Hospital Management System</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 680 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="340" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Abstract Person -->
      <rect x="250" y="15" width="180" height="75" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="340" y="35" font-family="monospace" font-size="11" font-style="italic" font-weight="bold" fill="#0969da" text-anchor="middle">&laquo;abstract&raquo; Person</text>
      <line x1="250" y1="42" x2="430" y2="42" stroke="#1f2328" stroke-width="1"/>
      <text x="260" y="58" font-family="monospace" font-size="9" fill="#1f2328">- id: String, - name: String</text>
      <text x="260" y="74" font-family="monospace" font-size="9" fill="#1f2328">- phone: String</text>

      <!-- Patient -->
      <rect x="50" y="130" width="160" height="85" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <text x="130" y="150" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">Patient</text>
      <line x1="50" y1="157" x2="210" y2="157" stroke="#1f2328" stroke-width="1"/>
      <text x="60" y="173" font-family="monospace" font-size="9" fill="#1f2328">- bloodGroup: String</text>
      <text x="60" y="189" font-family="monospace" font-size="9" fill="#1f2328">- medicalHistory: String</text>
      <text x="60" y="205" font-family="monospace" font-size="9" fill="#1a7f37">+ admit(): void</text>

      <!-- Doctor -->
      <rect x="470" y="130" width="160" height="85" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <text x="550" y="150" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">Doctor</text>
      <line x1="470" y1="157" x2="630" y2="157" stroke="#1f2328" stroke-width="1"/>
      <text x="480" y="173" font-family="monospace" font-size="9" fill="#1f2328">- specialty: String</text>
      <text x="480" y="189" font-family="monospace" font-size="9" fill="#1f2328">- licenseNo: String</text>
      <text x="480" y="205" font-family="monospace" font-size="9" fill="#1a7f37">+ prescribe(): void</text>

      <!-- Generalization Arrows -->
      <line x1="130" y1="130" x2="310" y2="90" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="310,90 300,98 316,102" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="550" y1="130" x2="370" y2="90" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="370,90 364,102 380,98" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>

      <!-- Association between Patient and Doctor -->
      <line x1="210" y1="172" x2="470" y2="172" stroke="#1f2328" stroke-width="1.5"/>
      <text x="220" y="165" font-family="monospace" font-size="10" fill="#1f2328">1..*</text>
      <text x="445" y="165" font-family="monospace" font-size="10" fill="#1f2328">1..*</text>

      <!-- Association Class Appointment -->
      <rect x="250" y="230" width="180" height="75" fill="#ffffff" stroke="#0969da" stroke-width="1.5"/>
      <text x="340" y="250" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">Appointment</text>
      <line x1="250" y1="257" x2="430" y2="257" stroke="#0969da" stroke-width="1"/>
      <text x="260" y="273" font-family="monospace" font-size="9" fill="#1f2328">- slot: DateTime</text>
      <text x="260" y="289" font-family="monospace" font-size="9" fill="#1f2328">- fee: Double</text>
      <line x1="340" y1="172" x2="340" y2="230" stroke="#0969da" stroke-width="1.5" stroke-dasharray="3,3"/>
    </svg>
    <span class="diagram-caption">Figure U2-L16: Hospital Management System Class Model with Association Class Appointment</span>
  </div>

  <h4 class="answer-heading">3. Design Decisions Rationale</h4>
  <ul>
    <li><strong>Separation of Medical Record from Appointment:</strong> An appointment represents a scheduled calendar encounter; a medical record represents an immutable, encrypted legal dossier that endures across multiple appointments.</li>
    <li><strong>Multiplicity Boundaries:</strong> A Doctor treats <code>1..*</code> Patients; a Patient can consult <code>1..*</code> Doctors across different medical disciplines. The <code>Appointment</code> reification stores the specific diagnosis and billing charges per consultation.</li>
  </ul>

  <h4 class="answer-heading">4. Comprehensive C++ Class Skeleton</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;vector&gt;
#include &lt;memory&gt;

class Patient; // Forward declaration

class Doctor {
    std::string doctorId;
    std::string specialty;
public:
    Doctor(std::string id, std::string spec) : doctorId(std::move(id)), specialty(std::move(spec)) {}
    void prescribe(Patient&amp; patient, const std::string&amp; medication);
};

class Appointment {
private:
    std::string slotTime;
    double consultationFee;
    std::shared_ptr&lt;Doctor&gt; doctor;
    std::shared_ptr&lt;Patient&gt; patient;

public:
    Appointment(std::string slot, double fee, std::shared_ptr&lt;Doctor&gt; doc, std::shared_ptr&lt;Patient&gt; pat)
        : slotTime(std::move(slot)), consultationFee(fee), doctor(std::move(doc)), patient(std::move(pat)) {}
    
    double getFee() const { return consultationFee; }
};</code></pre>


  <h4 class="answer-heading">5. Database Schema &amp; Security Boundary Realization</h4>
  <p>In medical informatics systems, the UML class model maps directly to HIPAA-compliant secure database schemas:</p>
  <ul>
    <li><strong>Role-Based Access Control (RBAC):</strong> Attending doctors have read-write access to <code>MedicalRecord</code>, while administrative billing personnel only have read-only access to anonymized diagnosis codes on the <code>Appointment</code> association class.</li>
    <li><strong>Immutable Audit Trails:</strong> Every state change on <code>Appointment</code> or <code>MedicalRecord</code> automatically generates a cryptographically hashed log entry containing the user ID, timestamp, and delta changes, guaranteeing tamper-evident clinical integrity.</li>
  </ul>

</div>
        """
    })

    # U2-L17
    questions.append({
        "id": "U2-L17",
        "unit": "2",
        "year": "2024-25",
        "year_display": "[2024-25]",
        "title": "Explain the concept of polymorphism in collaboration diagrams. Design a collaboration diagram for an online learning platform to show polymorphism in accessing different types of course materials.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Polymorphism in Collaboration Diagrams</h4>
  <p>In structural interaction modeling, <strong>Polymorphism</strong> is represented in a collaboration (communication) diagram by linking a caller object to a polymorphic interface or abstract base class. When the caller sends a standardized message (e.g., <code>1: openContent()</code>), the collaboration diagram annotates that the physical receiver object instance can dynamically resolve to any concrete specialization at runtime without modifying the caller's structural link or calling protocol.</p>

  <h4 class="answer-heading">2. Case Study: Online Learning Platform Course Material Access</h4>
  <p>An online learning management system (LMS) allows students to access heterogeneous learning materials through a unified interface. The materials specialize into:</p>
  <ul>
    <li><code>VideoLecture</code>: Involves streaming media chunks, tracking timestamp playback position.</li>
    <li><code>InteractiveQuiz</code>: Initializes question state machines and evaluation timers.</li>
    <li><code>PDFDocument</code>: Renders paginated vector graphics and enables bookmarking.</li>
  </ul>

  <h4 class="answer-heading">3. High-Contrast Collaboration Diagram Demonstrating Polymorphism</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 680 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="260" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Sender: StudentClient -->
      <rect x="40" y="90" width="160" height="60" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="120" y="125" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:StudentClient</u></text>

      <!-- Communication Link -->
      <line x1="200" y1="120" x2="400" y2="120" stroke="#1f2328" stroke-width="1.5"/>

      <!-- Polymorphic Message -->
      <line x1="240" y1="105" x2="350" y2="105" stroke="#0969da" stroke-width="1.8"/>
      <polygon points="350,105 342,101 342,109" fill="#0969da"/>
      <text x="295" y="95" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">1: renderContent()</text>

      <!-- Polymorphic Target Receiver -->
      <rect x="400" y="90" width="220" height="60" fill="#ffffff" stroke="#0969da" stroke-width="2"/>
      <text x="510" y="115" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle"><u>item : CourseMaterial</u></text>
      <text x="510" y="135" font-family="sans-serif" font-size="9" fill="#656d76" text-anchor="middle">&laquo;abstract interface&raquo;</text>

      <!-- Dynamic Specialization Tree -->
      <line x1="510" y1="150" x2="510" y2="190" stroke="#1f2328" stroke-width="1.2" stroke-dasharray="3,3"/>
      
      <!-- Concrete Object 1: Video -->
      <rect x="340" y="190" width="90" height="40" fill="#f6f8fa" stroke="#1f2328" stroke-width="1"/>
      <text x="385" y="215" font-family="monospace" font-size="9" fill="#1f2328" text-anchor="middle"><u>:VideoLecture</u></text>

      <!-- Concrete Object 2: Quiz -->
      <rect x="465" y="190" width="90" height="40" fill="#f6f8fa" stroke="#1f2328" stroke-width="1"/>
      <text x="510" y="215" font-family="monospace" font-size="9" fill="#1f2328" text-anchor="middle"><u>:InteractiveQuiz</u></text>

      <!-- Concrete Object 3: PDF -->
      <rect x="580" y="190" width="90" height="40" fill="#f6f8fa" stroke="#1f2328" stroke-width="1"/>
      <text x="625" y="215" font-family="monospace" font-size="9" fill="#1f2328" text-anchor="middle"><u>:PDFArticle</u></text>

      <line x1="510" y1="180" x2="385" y2="190" stroke="#1f2328" stroke-width="1"/>
      <line x1="510" y1="180" x2="510" y2="190" stroke="#1f2328" stroke-width="1"/>
      <line x1="510" y1="180" x2="625" y2="190" stroke="#1f2328" stroke-width="1"/>
    </svg>
    <span class="diagram-caption">Figure U2-L17: Collaboration Diagram Showing Polymorphic Resolution in LMS Content Delivery</span>
  </div>

  <h4 class="answer-heading">4. Dynamic Binding Semantics</h4>
  <p>The client invokes <code>item.renderContent()</code>. The virtual dispatch runtime identifies whether the heap instance is a <code>VideoLecture</code>, <code>InteractiveQuiz</code>, or <code>PDFArticle</code>, and executes the specialized routine. The collaboration diagram captures this without requiring separate caller links for every file format.</p>

  <h4 class="answer-heading">5. Working C++ Polymorphic Implementation</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;vector&gt;
#include &lt;memory&gt;

// Abstract Base Class
class CourseMaterial {
public:
    virtual ~CourseMaterial() = default;
    virtual void renderContent() = 0; // Polymorphic contract
};

class VideoLecture : public CourseMaterial {
public:
    void renderContent() override {
        std::cout << "[Video Stream] Buffering 1080p H.264 video chunks.\n";
    }
};

class InteractiveQuiz : public CourseMaterial {
public:
    void renderContent() override {
        std::cout << "[Quiz Engine] Initializing timed multi-choice assessment.\n";
    }
};

int main() {
    std::vector&lt;std::unique_ptr&lt;CourseMaterial&gt;&gt; curriculum;
    curriculum.push_back(std::make_unique&lt;VideoLecture&gt;());
    curriculum.push_back(std::make_unique&lt;InteractiveQuiz&gt;());

    for (const auto&amp; item : curriculum) {
        // Dynamic late binding resolves correct renderContent()
        item->renderContent();
    }
    return 0;
}</code></pre>


  <h4 class="answer-heading">6. Structural Elegance of Polymorphic Collaboration</h4>
  <p>By routing interaction through the abstract classifier <code>CourseMaterial</code>, the online learning architecture achieves extreme loose coupling:</p>
  <ul>
    <li><strong>Zero Modification on Feature Additions:</strong> When the university introduces new media formats (e.g., <code>ARSimulation</code> or <code>AudioPodcast</code>), no existing controller, player UI, or student progress tracking code is altered. The new class merely realizes the <code>CourseMaterial</code> interface and defines its specialized <code>renderContent()</code> implementation.</li>
    <li><strong>Uniform Client Invocation:</strong> The calling client executes <code>item->renderContent()</code> with zero conditional logic, eliminating error-prone <code>if-else</code> or <code>switch-case</code> type checks.</li>
  </ul>


  <h4 class="answer-heading">7. Sequence vs. Collaboration View of Polymorphism</h4>
  <p>While a Sequence Diagram shows polymorphism along vertical time lifelines with execution activation bars, the Collaboration Diagram uniquely highlights <strong>structural link reuse</strong>. The caller interacts across a single association link regardless of whether the runtime instance is a video stream, interactive quiz, or PDF document. This visually demonstrates the <strong>Liskov Substitution Principle (LSP)</strong>: objects of a superclass shall be replaceable with objects of its subclasses without breaking application logic.</p>

</div>
        """
    })

    # U2-L18
    questions.append({
        "id": "U2-L18",
        "unit": "2",
        "year": "2025-26",
        "year_display": "[2025-26]",
        "title": "Describe sequence diagrams in detail. Explain synchronous and asynchronous messages, call-back mechanisms, and broadcast messages.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Formal Definition and Architecture of Sequence Diagrams</h4>
  <p>A <strong>Sequence Diagram</strong> is an interaction diagram that models the chronological progression of message exchanges between collaborating objects to fulfill a specific use case scenario. It emphasizes the <strong>time-ordered sequencing</strong> of events. The horizontal dimension depicts the participating objects along parallel vertical lines called <strong>lifelines</strong>; the vertical dimension represents the progression of time downward.</p>

  <h4 class="answer-heading">2. Exhaustive Analysis of the Four Primary Message Types</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Message Type</th>
        <th style="width: 30%;">UML Graphical Notation</th>
        <th style="width: 50%;">Execution Semantics &amp; Thread Dynamics</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Synchronous Message</strong></td>
        <td>Solid horizontal line with a <strong>solid filled triangular arrowhead</strong>.</td>
        <td><strong>Blocking call:</strong> The caller yields execution control, suspending its thread and waiting until the receiver processes the message and returns control (e.g., standard procedure call).</td>
      </tr>
      <tr>
        <td><strong>2. Asynchronous Message</strong></td>
        <td>Solid horizontal line with an <strong>open "stick" arrowhead</strong>.</td>
        <td><strong>Non-blocking dispatch:</strong> The caller dispatches the message or signal into a message broker or event queue and continues execution immediately without waiting for the receiver.</td>
      </tr>
      <tr>
        <td><strong>3. Call-Back Mechanism</strong></td>
        <td>Directed return message or nested activation arrow.</td>
        <td>The server calls back a function pointer or interface passed by the client upon completion of long-running background tasks.</td>
      </tr>
      <tr>
        <td><strong>4. Broadcast Message</strong></td>
        <td>Single message branching to multiple parallel object lifelines.</td>
        <td>One-to-many publish-subscribe communication where an event publisher broadcasts a notification to multiple registered subscriber lifelines simultaneously.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. Clean Sequence Diagram Illustrating All 4 Message Types</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 680 320" width="100%" height="320" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="320" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Lifelines: Client, Gateway, WorkerThread, Cache, DB -->
      <rect x="30" y="20" width="90" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="75" y="40" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:Client</u></text>
      <line x1="75" y1="50" x2="75" y2="300" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <rect x="180" y="20" width="90" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="225" y="40" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:Gateway</u></text>
      <line x1="225" y1="50" x2="225" y2="300" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <rect x="330" y="20" width="100" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="380" y="40" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:AsyncWorker</u></text>
      <line x1="380" y1="50" x2="380" y2="300" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <rect x="490" y="20" width="80" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="530" y="40" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:CacheNode</u></text>
      <line x1="530" y1="50" x2="530" y2="300" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <rect x="590" y="20" width="80" height="30" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="630" y="40" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle"><u>:AuditLog</u></text>
      <line x1="630" y1="50" x2="630" y2="300" stroke="#656d76" stroke-width="1" stroke-dasharray="3,3"/>

      <!-- Synchronous Call -->
      <line x1="75" y1="80" x2="225" y2="80" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="225,80 215,75 215,85" fill="#1f2328"/>
      <text x="150" y="73" font-family="sans-serif" font-size="8" fill="#1f2328" text-anchor="middle">1: syncRequest() [BLOCKING]</text>

      <!-- Asynchronous Call -->
      <line x1="225" y1="120" x2="380" y2="120" stroke="#0969da" stroke-width="1.5"/>
      <line x1="380" y1="120" x2="370" y2="114" stroke="#0969da" stroke-width="1.5"/>
      <line x1="380" y1="120" x2="370" y2="126" stroke="#0969da" stroke-width="1.5"/>
      <text x="300" y="113" font-family="sans-serif" font-size="8" fill="#0969da" text-anchor="middle">2: dispatchTask() [ASYNC]</text>

      <!-- Synchronous Return -->
      <line x1="225" y1="150" x2="75" y2="150" stroke="#1f2328" stroke-width="1.2" stroke-dasharray="3,3"/>
      <polygon points="75,150 83,146 83,154" fill="#1f2328"/>
      <text x="150" y="143" font-family="sans-serif" font-size="8" fill="#1f2328" text-anchor="middle">return ackTicket</text>

      <!-- Callback Call -->
      <line x1="380" y1="190" x2="75" y2="190" stroke="#cf222e" stroke-width="1.5"/>
      <polygon points="75,190 85,185 85,195" fill="#cf222e"/>
      <text x="220" y="183" font-family="sans-serif" font-size="8" fill="#cf222e" text-anchor="middle">3: onTaskComplete(result) [CALLBACK]</text>

      <!-- Broadcast Call -->
      <line x1="380" y1="230" x2="630" y2="230" stroke="#1a7f37" stroke-width="1.5"/>
      <polygon points="530,230 522,226 522,234" fill="#1a7f37"/>
      <polygon points="630,230 622,226 622,234" fill="#1a7f37"/>
      <text x="480" y="223" font-family="sans-serif" font-size="8" fill="#1a7f37" text-anchor="middle">4: broadcastStateChange() [1-TO-MANY]</text>
    </svg>
    <span class="diagram-caption">Figure U2-L18: UML Sequence Diagram Demonstrating All 4 Core Message Types</span>
  </div>

  <h4 class="answer-heading">4. Detailed Concurrency &amp; Message Semantics</h4>
  <ul>
    <li><strong>Lifeline Activation Bars:</strong> Thin rectangles placed over a lifeline indicate that the object is actively executing code, holding a CPU thread, or waiting on synchronous nested invocations.</li>
    <li><strong>Asynchronous Message Queuing:</strong> Non-blocking arrows model producer-consumer architectures where messages are placed onto distributed message brokers (Apache Kafka, RabbitMQ) without stalling the sender.</li>
    <li><strong>Interaction Frames:</strong> Sequence diagrams structure complex logic using operator frames: <code>alt</code> (conditional alternative choices), <code>opt</code> (optional branch), <code>loop</code> (repetition), and <code>par</code> (concurrent parallel message streams).</li>
  </ul>


  <h4 class="answer-heading">5. Formal Syntax &amp; Notation Rules for Sequence Messages</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Arrow Style</th>
        <th style="width: 25%;">Message Kind</th>
        <th style="width: 55%;">Semantic Meaning &amp; Thread Behavior</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Solid line, filled triangle</td>
        <td>Synchronous Call</td>
        <td>Caller thread blocks; waits for operation completion and return value.</td>
      </tr>
      <tr>
        <td>Solid line, open stick arrow</td>
        <td>Asynchronous Signal</td>
        <td>Caller dispatches signal and continues concurrent execution immediately.</td>
      </tr>
      <tr>
        <td>Dashed line, open stick arrow</td>
        <td>Reply / Return Message</td>
        <td>Returns control and output data payload back to the waiting caller lifeline.</td>
      </tr>
      <tr>
        <td>Solid line with circle tip</td>
        <td>Lost / Found Message</td>
        <td>Lost message whose recipient is outside model scope; or found message from unknown origin.</td>
      </tr>
    </tbody>
  </table>

</div>
        """
    })

    # U2-L19
    questions.append({
        "id": "U2-L19",
        "unit": "2",
        "year": "2025-26",
        "year_display": "[2025-26]",
        "title": "Explain activity diagrams and state machine diagrams with suitable illustrations.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Detailed Comparison: Activity Diagrams vs. State Machine Diagrams</h4>
  <p>While both diagrams model dynamic behavior, their modeling viewpoints and semantic execution rules are fundamentally different:</p>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Dimension</th>
        <th style="width: 37%;">Activity Diagram (Workflow / Data Flow)</th>
        <th style="width: 38%;">State Machine Diagram (Lifecycle / Reactive)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Focus</strong></td>
        <td>Flow of control and computational activities across multiple objects.</td>
        <td>Lifecycle transitions and states of a single reactive entity over time.</td>
      </tr>
      <tr>
        <td><strong>Execution Driver</strong></td>
        <td><strong>Token Flow:</strong> Transitions occur automatically upon completion of internal activities.</td>
        <td><strong>Event-Driven:</strong> Transitions remain dormant until explicitly triggered by an external event.</td>
      </tr>
      <tr>
        <td><strong>Core Notations</strong></td>
        <td>Action states (pill shape), Decision diamonds, Fork/Join synchronization bars, Swimlanes.</td>
        <td>States (rounded rectangles), Event triggers, Guard expressions, Composite states.</td>
      </tr>
      <tr>
        <td><strong>Target Domain</strong></td>
        <td>Business process modeling, use case elaboration, parallel algorithmic logic.</td>
        <td>Embedded devices, protocol state machines, UI components, financial transactions.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">2. High-Contrast Illustration: Order Processing Activity Diagram</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 660 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="660" height="260" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Initial Node -->
      <circle cx="50" cy="130" r="10" fill="#1f2328"/>

      <line x1="60" y1="130" x2="110" y2="130" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="110,130 102,126 102,134" fill="#1f2328"/>

      <!-- Action 1: Receive Order -->
      <rect x="110" y="105" width="120" height="50" rx="10" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="170" y="135" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">Receive Order</text>

      <!-- Fork Bar (Concurrency) -->
      <line x1="230" y1="130" x2="270" y2="130" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="270,130 262,126 262,134" fill="#1f2328"/>
      <rect x="270" y="50" width="8" height="160" fill="#1f2328"/>

      <!-- Forked Action 1: Process Payment -->
      <line x1="278" y1="80" x2="330" y2="80" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="330,80 322,76 322,84" fill="#1f2328"/>
      <rect x="330" y="55" width="130" height="50" rx="10" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="395" y="85" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">Process Payment</text>

      <!-- Forked Action 2: Pack Items -->
      <line x1="278" y1="180" x2="330" y2="180" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="330,180 322,176 322,184" fill="#1f2328"/>
      <rect x="330" y="155" width="130" height="50" rx="10" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="395" y="185" font-family="monospace" font-size="10" font-weight="bold" fill="#0969da" text-anchor="middle">Pack Inventory</text>

      <!-- Join Bar -->
      <line x1="460" y1="80" x2="510" y2="80" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="510,80 502,76 502,84" fill="#1f2328"/>
      <line x1="460" y1="180" x2="510" y2="180" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="510,180 502,176 502,184" fill="#1f2328"/>
      <rect x="510" y="50" width="8" height="160" fill="#1f2328"/>

      <!-- Final Action: Ship Order -->
      <line x1="518" y1="130" x2="560" y2="130" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="560,130 552,126 552,134" fill="#1f2328"/>
      <circle cx="585" cy="130" r="12" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <circle cx="585" cy="130" r="7" fill="#1f2328"/>
    </svg>
    <span class="diagram-caption">Figure U2-L19: UML Activity Diagram for Order Processing with Fork and Join Synchronization Bars</span>
  </div>

  <h4 class="answer-heading">3. Comprehensive Detailed Comparison Matrix</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Criteria</th>
        <th style="width: 37%;">Activity Diagram</th>
        <th style="width: 38%;">State Machine Diagram</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Theoretical Roots</strong></td>
        <td>Petri Nets and Data Flow Diagrams.</td>
        <td>David Harel's Statecharts and Finite State Automata.</td>
      </tr>
      <tr>
        <td><strong>Primary Focus</strong></td>
        <td>Flow of control and data between activities across multiple classes.</td>
        <td>Lifecycle state transitions of a single reactive object.</td>
      </tr>
      <tr>
        <td><strong>Transition Driver</strong></td>
        <td>Internal activity completion (Token Flow).</td>
        <td>Explicit external events, signals, or elapsed timers.</td>
      </tr>
      <tr>
        <td><strong>Swimlanes / Partitions</strong></td>
        <td>Supported: Groups actions by organizational department or class.</td>
        <td>Not applicable (Models a single classifier).</td>
      </tr>
    </tbody>
  </table>


  <h4 class="answer-heading">4. Architectural Swimlanes and Business Process Partitioning</h4>
  <p>In advanced activity diagrams, <strong>Swimlanes (Activity Partitions)</strong> group activity steps by organizational responsibility or software tier:</p>
  <ul>
    <li><strong>Customer Swimlane:</strong> Encapsulates user actions (<code>Browse Catalog</code>, <code>Add to Cart</code>, <code>Submit Checkout</code>).</li>
    <li><strong>Application Controller Swimlane:</strong> Orchestrates transaction boundaries, calls authorization services, and triggers order packaging.</li>
    <li><strong>Warehouse Logistics Swimlane:</strong> Handles physical picking, barcode scanning, packing, and courier handoff.</li>
  </ul>
  <p>Swimlanes transform flat activity flowcharts into multi-tier architectural process models, clarifying exact responsibilities between frontend clients, backend microservices, and external third-party systems.</p>


  <h4 class="answer-heading">5. Accompanying State Machine Specification: Order Lifecycle</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th>Initial State</th>
        <th>Triggering Event &amp; Guard</th>
        <th>Target State</th>
        <th>Executed Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>ORDER_PLACED</code></td>
        <td><code>verifyPayment() [success]</code></td>
        <td><code>PROCESSING</code></td>
        <td><code>allocateInventory()</code></td>
      </tr>
      <tr>
        <td><code>PROCESSING</code></td>
        <td><code>packComplete</code></td>
        <td><code>READY_TO_SHIP</code></td>
        <td><code>generateShippingLabel()</code></td>
      </tr>
      <tr>
        <td><code>READY_TO_SHIP</code></td>
        <td><code>carrierScan</code></td>
        <td><code>IN_TRANSIT</code></td>
        <td><code>notifyCustomerWithTracking()</code></td>
      </tr>
      <tr>
        <td><code>IN_TRANSIT</code></td>
        <td><code>deliveryConfirmed</code></td>
        <td><code>DELIVERED</code></td>
        <td><code>archiveOrder()</code></td>
      </tr>
      <tr>
        <td><code>ANY_ACTIVE</code></td>
        <td><code>customerCancel() [beforeShipment]</code></td>
        <td><code>CANCELLED</code></td>
        <td><code>refundPayment(); restockItems()</code></td>
      </tr>
    </tbody>
  </table>

</div>
        """
    })

    # U2-L20
    questions.append({
        "id": "U2-L20",
        "unit": "2",
        "year": "2025-26",
        "year_display": "[2025-26]",
        "title": "Describe architectural modeling. Explain component diagrams and deployment diagrams and their significance in system design.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Strategic Role of Architectural Modeling</h4>
  <p><strong>Architectural Modeling</strong> bridges the gap between conceptual object-oriented domain analysis and physical, deployed software systems. It ensures that non-functional qualities—such as modular build times, microservice scalability, network security boundaries, and high-availability failovers—are formally designed and communicated.</p>

  <h4 class="answer-heading">2. Component Diagrams: Software Packaging View</h4>
  <p>A <strong>Component Diagram</strong> models the physical modular packaging of software code into executable components (e.g., JARs, DLLs, Docker containers, web assemblies). It specifies <strong>Provided Interfaces</strong> (services exported via "lollipop" notation) and <strong>Required Interfaces</strong> (dependencies imported via "socket" notation), enforcing clean loose coupling and allowing components to be replaced or upgraded independently.</p>

  <h4 class="answer-heading">3. Deployment Diagrams: Hardware Topology View</h4>
  <p>A <strong>Deployment Diagram</strong> models the runtime execution architecture of the system. It displays physical computational <strong>Nodes</strong> (servers, virtual machines, cloud instances, embedded devices), network communication protocols connecting nodes (HTTPS, gRPC, TCP/IP), and the specific software <strong>Artifacts</strong> allocated to execute upon each node.</p>

  <h4 class="answer-heading">4. High-Contrast Unified Architectural Diagram</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 680 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="260" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Node 1: Web Server -->
      <rect x="40" y="30" width="250" height="200" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="165" y="55" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">&laquo;device / node&raquo; Web Application Server</text>
      
      <!-- Component within Node 1 -->
      <rect x="65" y="80" width="200" height="60" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <rect x="55" y="90" width="15" height="10" fill="#f6f8fa" stroke="#1f2328"/>
      <rect x="55" y="115" width="15" height="10" fill="#f6f8fa" stroke="#1f2328"/>
      <text x="165" y="115" font-family="monospace" font-size="10" font-weight="bold" fill="#1f2328" text-anchor="middle">&laquo;component&raquo; WebPortal.war</text>

      <!-- Provided Interface -->
      <circle cx="310" cy="110" r="8" fill="#ffffff" stroke="#0969da" stroke-width="1.5"/>
      <line x1="265" y1="110" x2="302" y2="110" stroke="#0969da" stroke-width="1.5"/>
      <text x="310" y="95" font-family="monospace" font-size="9" fill="#0969da" text-anchor="middle">HTTPS / REST</text>

      <!-- Communication Path -->
      <line x1="318" y1="110" x2="410" y2="110" stroke="#1f2328" stroke-width="1.5"/>
      <text x="365" y="130" font-family="monospace" font-size="8" fill="#656d76" text-anchor="middle">TLS 1.3</text>

      <!-- Node 2: Database Server -->
      <rect x="410" y="30" width="240" height="200" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="530" y="55" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">&laquo;device / node&raquo; DB Cluster Node</text>

      <!-- Component within Node 2 -->
      <rect x="430" y="80" width="200" height="60" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <rect x="420" y="90" width="15" height="10" fill="#f6f8fa" stroke="#1f2328"/>
      <rect x="420" y="115" width="15" height="10" fill="#f6f8fa" stroke="#1f2328"/>
      <text x="530" y="115" font-family="monospace" font-size="10" font-weight="bold" fill="#1f2328" text-anchor="middle">&laquo;artifact&raquo; pgsql-engine.bin</text>
    </svg>
    <span class="diagram-caption">Figure U2-L20: Combined UML Component and Deployment Architecture Model</span>
  </div>

  <h4 class="answer-heading">5. Industrial Significance in Enterprise Cloud Deployment</h4>
  <p>In modern microservices and cloud engineering, architectural modeling is essential for:</p>
  <ul>
    <li><strong>CI/CD Build Automation:</strong> Component diagrams define build order dependencies and interface compatibility tests between independently versioned microservices.</li>
    <li><strong>Kubernetes / Infrastructure Topology:</strong> Deployment diagrams document pod allocations, ingress load balancers, multi-region database replication paths, and VPC network firewalls.</li>
    <li><strong>Capacity Planning &amp; Sizing:</strong> Modeling physical nodes allows infrastructure engineers to provision CPU cores, RAM limits, and network throughput to satisfy service level agreements (SLAs).</li>
  </ul>


  <h4 class="answer-heading">6. Enterprise Microservice Architecture Case Example</h4>
  <p>In modern cloud systems (e.g., Netflix or Amazon), architectural modeling governs continuous delivery:</p>
  <ul>
    <li><strong>Component Packaging:</strong> The <code>PaymentGateway</code> component is packaged into a lightweight Alpine Linux Docker container with an embedded gRPC server exporting an authenticated <code>PaymentService.proto</code> interface.</li>
    <li><strong>Deployment Topology:</strong> The payment container is deployed as a replicated Kubernetes ReplicaSet across three availability zones on AWS EC2 <code>m5.xlarge</code> instances, communicating with Amazon Aurora PostgreSQL via an encrypted AWS PrivateLink connection.</li>
  </ul>


  <h4 class="answer-heading">7. Standard UML Stereotypes for Architectural Modeling</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Diagram Type</th>
        <th style="width: 25%;">Standard Stereotype</th>
        <th style="width: 50%;">Semantic Description &amp; Usage</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Component</strong></td>
        <td><code>&laquo;executable&raquo;</code></td>
        <td>A program binary that can be executed directly by the operating system kernel.</td>
      </tr>
      <tr>
        <td><strong>Component</strong></td>
        <td><code>&laquo;library&raquo;</code></td>
        <td>A static or dynamic linked library (e.g., <code>.so</code>, <code>.dll</code>, <code>.jar</code>) providing APIs.</td>
      </tr>
      <tr>
        <td><strong>Deployment</strong></td>
        <td><code>&laquo;device&raquo;</code></td>
        <td>A physical computational resource with hardware processing capability (e.g., blade server, router).</td>
      </tr>
      <tr>
        <td><strong>Deployment</strong></td>
        <td><code>&laquo;executionEnvironment&raquo;</code></td>
        <td>A software container offering an OS or runtime execution engine (e.g., JVM, Node.js, Docker engine).</td>
      </tr>
    </tbody>
  </table>

</div>
        """
    })

    return questions

if __name__ == "__main__":
    qs = get_unit2_questions()
    print(f"Generated {len(qs)} questions for Unit 2.")
    import re
    for q in qs:
        clean = re.sub(r'<[^>]+>', ' ', q['content'])
        words = len(clean.split())
        print(f"{q['id']}: {words} words | has_svg={'<svg' in q['content']} | has_code={'<code' in q['content']}")


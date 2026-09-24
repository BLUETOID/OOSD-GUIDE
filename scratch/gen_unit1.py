# -*- coding: utf-8 -*-
"""
Unit 1 Long Answers Generator (Questions U1-L01 to U1-L15)
Every question contains 400-750 words, detailed subheadings, comparison tables,
working C++ code, or high-contrast SVG diagrams.
"""

def get_unit1_questions():
    questions = []

    # U1-L01
    questions.append({
        "id": "U1-L01",
        "unit": "1",
        "year": "2020-21 2023-24",
        "year_display": "[2020-21], [2023-24]",
        "title": "What do you understand by Object-Oriented Technology? Discuss the pros and cons of object-oriented technology with suitable example.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Formal Definition & Philosophy of Object-Oriented Technology (OOT)</h4>
  <p><strong>Object-Oriented Technology (OOT)</strong> is an overarching software engineering paradigm encompassing Object-Oriented Analysis (OOA), Object-Oriented Design (OOD), and Object-Oriented Programming (OOP). In OOT, software systems are conceptualized and organized not as hierarchical trees of subroutines manipulating passive data structures, but as dynamic, decentralized networks of collaborating, autonomous computational entities known as <strong>objects</strong>.</p>
  <p>Each object encapsulates its internal <em>state</em> (represented by private instance variables and data structures) and its external <em>behavior</em> (manifested through public methods or operations). Computation proceeds exclusively via <strong>message passing</strong>: client objects invoke member functions on server objects, requesting services without needing or possessing knowledge of the server's internal algorithmic implementation or physical memory layout.</p>

  <h4 class="answer-heading">2. Comprehensive Advantages (Pros) of Object-Oriented Technology</h4>
  <ul>
    <li><strong>Information Hiding and Robust Encapsulation:</strong> By restricting direct field access through access specifiers (<code>private</code>, <code>protected</code>), state mutations are funneled through validated member functions. Invariants remain protected from external corruption, drastically reducing regression bugs during software evolution.</li>
    <li><strong>Software Reusability via Inheritance and Composition:</strong> Thoroughly debugged and tested base classes can be reused across multiple projects through specialization (inheritance) or assembly into composite components. This amortizes development costs and shortens time-to-market.</li>
    <li><strong>Extensibility and Open-Closed Principle (OCP):</strong> Polymorphic dynamic dispatch allows systems to introduce new domain entity subtypes (e.g., a new <code>CryptoPayment</code> subclass in a financial gateway) without modifying or recompiling existing transaction processing pipelines.</li>
    <li><strong>Direct Real-World Domain Mapping:</strong> The semantic gap between requirements engineering and code implementation is minimized because classes mirror real-world business entities (e.g., <code>Account</code>, <code>Policy</code>, <code>PatientRecord</code>) rather than technical procedural subroutines.</li>
    <li><strong>Concurrent Development & High Maintainability:</strong> Explicit interfaces allow disparate engineering teams to independently build, mock, unit-test, and refine individual subsystems with minimal cross-team coordination bottlenecks.</li>
  </ul>

  <h4 class="answer-heading">3. Limitations and Criticisms (Cons) of Object-Oriented Technology</h4>
  <ul>
    <li><strong>Execution and Memory Overhead:</strong> Dynamic polymorphism relies on virtual method tables (VTables) and runtime indirect function pointer lookups. In deep inheritance hierarchies, object representations require hidden virtual table pointers (<code>vptr</code>), leading to increased memory footprints and cache miss penalties.</li>
    <li><strong>Steep Conceptual Learning Curve:</strong> Designing robust object-oriented architectures demands mastering subtle design heuristics, polymorphism, abstraction boundaries, and patterns (e.g., SOLID principles, Gang of Four design patterns). Novice engineers frequently create brittle, overly deep inheritance trees.</li>
    <li><strong>Increased Object Creep and Code Verbosity:</strong> Basic algorithms frequently require extensive boilerplate (class definitions, interfaces, constructors, factory classes, getters, and setters), resulting in substantially higher source-code line counts than equivalent procedural or functional scripts.</li>
    <li><strong>Inefficient Modeling of Pure Cross-Cutting Concerns:</strong> Concerns such as transaction logging, metric collection, and distributed tracing are inherently orthogonal to class boundaries, requiring additional paradigms like Aspect-Oriented Programming (AOP) or interceptor middleware.</li>
  </ul>

  <h4 class="answer-heading">4. Architectural Case Example: Automated Banking Transaction System</h4>
  <p>Consider an automated financial transaction processing engine. In a procedural system, a global array of account records is passed across distinct procedures (<code>deposit()</code>, <code>calculate_interest()</code>, <code>audit()</code>). Any change to the record structure breaks all procedures. Under OOT, an abstract base class <code>BankAccount</code> encapsulates balance invariants and declares a pure virtual operation <code>applyMonthlyFees()</code>:</p>

  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;memory&gt;
#include &lt;vector&gt;

// Abstract Domain Entity
class BankAccount {
protected:
    std::string accountNumber;
    double balance;

public:
    BankAccount(const std::string&amp; accNo, double initialBalance)
        : accountNumber(accNo), balance(initialBalance) {}
    virtual ~BankAccount() = default;

    void deposit(double amount) {
        if (amount &gt; 0) balance += amount;
    }

    virtual bool withdraw(double amount) {
        if (amount &gt; 0 &amp;&amp; balance &gt;= amount) {
            balance -= amount;
            return true;
        }
        return false;
    }

    virtual void applyMonthlyFees() = 0; // Polymorphic interface

    double getBalance() const { return balance; }
};

// Concrete Specialized Subclass 1
class SavingsAccount : public BankAccount {
    double interestRate;
public:
    SavingsAccount(const std::string&amp; id, double bal, double rate)
        : BankAccount(id, bal), interestRate(rate) {}

    void applyMonthlyFees() override {
        balance += (balance * interestRate / 12.0); // Interest credit
    }
};

// Concrete Specialized Subclass 2
class CheckingAccount : public BankAccount {
    double maintenanceFee;
public:
    CheckingAccount(const std::string&amp; id, double bal, double fee)
        : BankAccount(id, bal), maintenanceFee(fee) {}

    void applyMonthlyFees() override {
        balance -= maintenanceFee; // Account maintenance debit
    }
};

int main() {
    std::vector&lt;std::unique_ptr&lt;BankAccount&gt;&gt; ledger;
    ledger.push_back(std::make_unique&lt;SavingsAccount&gt;("SA-101", 5000.0, 0.04));
    ledger.push_back(std::make_unique&lt;CheckingAccount&gt;("CA-202", 1200.0, 25.0));

    // Dynamic Polymorphic Processing (Open-Closed Principle)
    for (const auto&amp; acc : ledger) {
        acc-&gt;applyMonthlyFees();
        std::cout &lt;&lt; "Updated Balance: $" &lt;&lt; acc-&gt;getBalance() &lt;&lt; std::endl;
    }
    return 0;
}</code></pre>
  <p><strong>Analysis of Case Example:</strong> When the bank introduces a new <code>MoneyMarketAccount</code>, no existing batch processing code is altered or recompiled. The new subclass simply implements <code>applyMonthlyFees()</code>, demonstrating the extensibility and safety of OOT.</p>
</div>
        """
    })

    # U1-L02
    questions.append({
        "id": "U1-L02",
        "unit": "1",
        "year": "2020-21",
        "year_display": "[2020-21]",
        "title": "Why Object-Oriented Programming (OOP) is so important for software industries or in real life? Explain with example. Discuss the pros and cons of object-oriented technology with suitable example.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Industrial and Real-Life Imperative of Object-Oriented Programming</h4>
  <p>Modern commercial software systems—such as cloud platforms, operating systems, enterprise resource planning (ERP) suites, and autonomous vehicle controllers—scale to tens of millions of lines of code developed by thousands of distributed engineers over decades. In such large-scale settings, the traditional structured or procedural programming model breaks down catastrophically due to three foundational crises:</p>
  <ol>
    <li><strong>Shared State Corruption:</strong> Global variables and unstructured data structs passed across hundreds of procedural functions allow any programmer to mutate memory states without validation, producing unpredictable side-effects.</li>
    <li><strong>Exponential Ripple Effects of Schema Changes:</strong> Modifying a struct definition requires finding, modifying, and re-testing every procedural function that directly accesses any field of that struct across the entire codebase.</li>
    <li><strong>Cognitive Overload and Semantic Mismatch:</strong> Procedural decomposition forces engineers to translate business reality into algorithmic flowcharts, losing the direct intuitive connection between domain entities and software components.</li>
  </ol>
  <p><strong>OOP resolves these crises</strong> by bounding cognitive complexity within explicit, cohesive class boundaries, enforcing strict access barriers, and enabling scalable component assembly through interfaces.</p>

  <h4 class="answer-heading">2. Real-World Case Study: Commercial Airline Flight Reservation and Fleet Management</h4>
  <p>Consider an international airline platform managing aircraft fleets, passengers, seat reservations, and ticketing. A real-world flight system exhibits diverse aircraft models (Boeing 787, Airbus A350), multiple passenger tiers (Economy, Business, First Class), and volatile dynamic pricing algorithms.</p>
  <p>Under an OOP paradigm, the domain is organized into collaborating classes:</p>
  <ul>
    <li><code>Aircraft</code>: Abstract base class encapsulating fuel capacity, seating layout matrices, and maintenance schedules. Specializations (<code>Boeing787</code>, <code>AirbusA350</code>) encapsulate specific avionics constraints.</li>
    <li><code>Seat</code>: Encapsulates state (<code>Available</code>, <code>Reserved</code>, <code>Locked</code>) and ensures that race conditions during concurrent bookings are resolved inside atomic method calls (e.g., <code>reserveSeat(passengerId)</code>).</li>
    <li><code>PricingStrategy</code>: An interface enabling polymorphic dynamic swapping of pricing logic (e.g., <code>EarlyBirdPricing</code>, <code>SurgeDemandPricing</code>, <code>FrequentFlyerDiscount</code>) at runtime without halting the reservation engine.</li>
  </ul>

  <h4 class="answer-heading">3. Comprehensive Pros and Cons of OOT in Industry</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Dimension</th>
        <th style="width: 40%;">Industrial Advantage (Pro)</th>
        <th style="width: 40%;">Trade-off / Limitation (Con)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Maintainability & Evolution</strong></td>
        <td>Modifications to internal data formats remain localized inside class implementations. Public contracts protect consumers.</td>
        <td>Over-abstracted object hierarchies can create "spaghetti inheritance" requiring significant effort to trace runtime execution paths.</td>
      </tr>
      <tr>
        <td><strong>Engineering Scalability</strong></td>
        <td>Large engineering teams divide work along class and interface boundaries with clear ownership and API mocking.</td>
        <td>Initial architectural planning, domain analysis, and interface design require significantly higher upfront time and senior architectural expertise.</td>
      </tr>
      <tr>
        <td><strong>Runtime Performance</strong></td>
        <td>Modern optimizing compilers (JIT, LTO, devirtualization) mitigate invocation overhead for well-structured classes.</td>
        <td>Virtual method dynamic dispatch (VTable dereferencing) and scattered heap allocations impose CPU cache penalties compared to data-oriented flat arrays.</td>
      </tr>
      <tr>
        <td><strong>Code Reusability</strong></td>
        <td>Standardized framework libraries (e.g., Spring, Qt, .NET BCL) offer battle-tested foundational building blocks.</td>
        <td>Inheritance hierarchies can couple subclasses tightly to base class quirks (the "fragile base class" problem).</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">4. Architectural Implementation Pattern</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;memory&gt;

// Abstract Strategy Interface
class FareCalculationStrategy {
public:
    virtual ~FareCalculationStrategy() = default;
    virtual double computeFare(double basePrice) const = 0;
};

class EconomyFare : public FareCalculationStrategy {
public:
    double computeFare(double basePrice) const override {
        return basePrice * 1.05; // 5% regulatory taxes
    }
};

class BusinessFare : public FareCalculationStrategy {
public:
    double computeFare(double basePrice) const override {
        return (basePrice * 2.8) + 150.0; // Premium service charges
    }
};

// Flight Ticket Context Class
class FlightTicket {
private:
    std::string ticketNumber;
    double baseDistanceRate;
    std::unique_ptr&lt;FareCalculationStrategy&gt; fareStrategy;

public:
    FlightTicket(std::string tNo, double rate, std::unique_ptr&lt;FareCalculationStrategy&gt; strategy)
        : ticketNumber(std::move(tNo)), baseDistanceRate(rate), fareStrategy(std::move(strategy)) {}

    void setFareStrategy(std::unique_ptr&lt;FareCalculationStrategy&gt; newStrategy) {
        fareStrategy = std::move(newStrategy);
    }

    double calculateTotal() const {
        return fareStrategy-&gt;computeFare(baseDistanceRate);
    }
};

int main() {
    FlightTicket ticket("TK-98712", 450.0, std::make_unique&lt;EconomyFare&gt;());
    std::cout &lt;&lt; "Economy Total: $" &lt;&lt; ticket.calculateTotal() &lt;&lt; std::endl;

    ticket.setFareStrategy(std::make_unique&lt;BusinessFare&gt;());
    std::cout &lt;&lt; "Upgraded Business Total: $" &lt;&lt; ticket.calculateTotal() &lt;&lt; std::endl;
    return 0;
}</code></pre>
</div>
        """
    })

    # U1-L03
    questions.append({
        "id": "U1-L03",
        "unit": "1",
        "year": "2021-22",
        "year_display": "[2021-22]",
        "title": "Explain all basic concepts of object oriented programming.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Introduction to Core OOP Concepts</h4>
  <p>Object-Oriented Programming is grounded upon eight fundamental architectural concepts that collectively govern system decomposition, abstraction, and communication:</p>

  <h4 class="answer-heading">2. The Eight Pillar Concepts</h4>
  <ol>
    <li><strong>Objects:</strong> The foundational runtime entities in an object-oriented system. An object represents a specific instance of a concept, physical entity, or business artifact. It encapsulates:
      <ul>
        <li><em>Identity:</em> A unique, immutable system handle or memory address distinguishing it from all other objects regardless of attribute equality.</li>
        <li><em>State:</em> The current values held by its member variables at any given point in time.</li>
        <li><em>Behavior:</em> The set of operations and state transitions it can execute in response to received messages.</li>
      </ul>
    </li>
    <li><strong>Classes:</strong> The compile-time syntactic blueprint, user-defined type, or template from which individual object instances are constructed. A class specifies the structural member fields, method signatures, access controls, and lifecycle contracts (constructors and destructors).</li>
    <li><strong>Data Abstraction:</strong> The cognitive process of identifying essential characteristics of an entity while filtering out irrelevant implementation complexities and background details. Abstraction creates clear external interfaces (e.g., abstract base classes or pure virtual interfaces) through which users interact with services without understanding the internal algorithms.</li>
    <li><strong>Encapsulation:</strong> The structural bundling of state variables and the operations that manipulate them within a single defensive perimeter (the class boundary), combined with <em>information hiding</em> via access modifiers (<code>private</code>, <code>protected</code>, <code>public</code>).</li>
    <li><strong>Inheritance (Generalization/Specialization):</strong> The structural mechanism whereby a derived child class inherits attributes, properties, and behaviors from one or more parent base classes. It establishes an "is-a" relationship, facilitates hierarchical classification, and enables systematic code reuse without code replication.</li>
    <li><strong>Polymorphism:</strong> The capability of a single entity (such as a function identifier, operator, or reference variable) to manifest in multiple behavioral forms depending on context. It is bifurcated into:
      <ul>
        <li><em>Static (Compile-Time) Polymorphism:</em> Function overloading, operator overloading, and template metaprogramming resolved during compilation.</li>
        <li><em>Dynamic (Runtime) Polymorphism:</em> Virtual member function invocations dispatched at runtime through virtual table lookups based on actual object type.</li>
      </ul>
    </li>
    <li><strong>Dynamic (Late) Binding:</strong> The mechanism wherein the physical code address of the procedure called in response to a message is resolved at runtime rather than at compile time or link time. This is the runtime foundation enabling dynamic polymorphism.</li>
    <li><strong>Message Passing:</strong> The operational protocol through which objects communicate. A client object sends a message comprising the destination object handle, the target operation name, and associated argument parameters. The receiver receives the message, binds it to an internal method, mutates its internal state, and optionally returns a response value.</li>
  </ol>

  <h4 class="answer-heading">3. Comprehensive Unified C++ Code Demonstration</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;vector&gt;
#include &lt;memory&gt;

// Concept 3: Data Abstraction (Abstract Interface)
class Device {
private:
    // Concept 4: Encapsulation & Information Hiding
    std::string deviceId;
    bool powerState;

protected:
    Device(const std::string&amp; id) : deviceId(id), powerState(false) {}

public:
    virtual ~Device() = default;

    // Public Contract
    void powerOn() { powerState = true; onStateChanged(); }
    void powerOff() { powerState = false; onStateChanged(); }
    bool isPowered() const { return powerState; }
    std::string getId() const { return deviceId; }

    // Concept 6 & 7: Polymorphism and Dynamic Binding
    virtual void executeTask() = 0; // Pure virtual function

protected:
    virtual void onStateChanged() {}
};

// Concept 5: Inheritance
class SensorNode : public Device {
    double readingCelsius;

public:
    SensorNode(const std::string&amp; id) : Device(id), readingCelsius(22.5) {}

    void executeTask() override {
        std::cout &lt;&lt; "[Sensor " &lt;&lt; getId() &lt;&lt; "] Transmitting Temperature: " 
                  &lt;&lt; readingCelsius &lt;&lt; " C" &lt;&lt; std::endl;
    }
};

class ActuatorNode : public Device {
    int valvePositionDegrees;

public:
    ActuatorNode(const std::string&amp; id) : Device(id), valvePositionDegrees(0) {}

    void executeTask() override {
        valvePositionDegrees = (valvePositionDegrees + 45) % 360;
        std::cout &lt;&lt; "[Actuator " &lt;&lt; getId() &lt;&lt; "] Rotating Valve to: " 
                  &lt;&lt; valvePositionDegrees &lt;&lt; " deg" &lt;&lt; std::endl;
    }
};

// Concept 8: Message Passing Controller
int main() {
    // Concept 1 & 2: Objects and Classes instantiated
    std::vector&lt;std::unique_ptr&lt;Device&gt;&gt; network;
    network.push_back(std::make_unique&lt;SensorNode&gt;("TH-01"));
    network.push_back(std::make_unique&lt;ActuatorNode&gt;("VLV-99"));

    for (const auto&amp; node : network) {
        node-&gt;powerOn();
        // Dynamic late binding resolves correct executeTask at runtime
        node-&gt;executeTask();
    }
    return 0;
}</code></pre>
</div>
        """
    })

    # U1-L04
    questions.append({
        "id": "U1-L04",
        "unit": "1",
        "year": "2021-22",
        "year_display": "[2021-22]",
        "title": "What is UML? List all building blocks of UML. Explain all types of things used in UML.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Formal Definition of UML</h4>
  <p>The <strong>Unified Modeling Language (UML)</strong> is the international standard visual modeling language ratified by the Object Management Group (OMG) for specifying, visualizing, constructing, and documenting the artifacts of software-intensive systems. UML is not a proprietary programming language or a prescriptive software development methodology; rather, it provides a standardized graphical meta-model and notation that enables software architects, systems engineers, and business analysts to communicate complex system structures and operational dynamics unambiguously across all phases of the software lifecycle.</p>

  <h4 class="answer-heading">2. The Three Primary Building Blocks of UML</h4>
  <p>UML architecture is systematically organized around three foundational building blocks:</p>
  <ol>
    <li><strong>Things:</strong> The primary structural, behavioral, grouping, and annotational abstractions that constitute the basic model atoms.</li>
    <li><strong>Relationships:</strong> The semantic glues that tie Things together, specifying structural connections, behavioral interactions, inheritance hierarchies, and operational dependencies.</li>
    <li><strong>Diagrams:</strong> Graph-based visual projections representing coherent collections of Things and Relationships viewed from specific architectural viewpoints (e.g., static structure, dynamic sequence, physical deployment).</li>
  </ol>

  <h4 class="answer-heading">3. Exhaustive Analysis of All Four Types of Things in UML</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Category of Things</th>
        <th style="width: 25%;">Specific Elements</th>
        <th style="width: 55%;">Semantic Meaning, Visual Notation & Role</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Structural Things</strong><br><em>(Static building blocks)</em></td>
        <td>
          &bull; Class<br>
          &bull; Interface<br>
          &bull; Collaboration<br>
          &bull; Use Case<br>
          &bull; Active Class<br>
          &bull; Component<br>
          &bull; Node
        </td>
        <td>
          The physical and conceptual nouns of a model.
          <br>&bull; <strong>Class:</strong> 3-compartment rectangle (Name, Attributes, Operations).
          <br>&bull; <strong>Interface:</strong> Named circle ("lollipop") or rectangle with <code>&laquo;interface&raquo;</code> declaring a collection of operations.
          <br>&bull; <strong>Use Case:</strong> Solid ellipse representing a discrete unit of system functionality offering observable value to an actor.
          <br>&bull; <strong>Component:</strong> Modular packaging unit with tabs or stereotype icon representing physical software code (JAR, DLL, executable).
          <br>&bull; <strong>Node:</strong> 3D cuboid representing a computational physical hardware resource (server, sensor, mobile device) possessing memory and processing capacity.
        </td>
      </tr>
      <tr>
        <td><strong>2. Behavioral Things</strong><br><em>(Dynamic building blocks)</em></td>
        <td>
          &bull; Interaction (Message)<br>
          &bull; State Machine (State)
        </td>
        <td>
          The verbs of a model representing dynamic behavior over space and time.
          <br>&bull; <strong>Interaction:</strong> Represents a message exchange between objects characterized by a directed arrow accompanied by sequence numbers, method signatures, and return parameters.
          <br>&bull; <strong>State:</strong> A rounded rectangle representing a discrete operational condition or phase in the lifecycle of an object during which it satisfies certain conditions, executes an activity, or waits for an event.
        </td>
      </tr>
      <tr>
        <td><strong>3. Grouping Things</strong><br><em>(Organizational blocks)</em></td>
        <td>
          &bull; Package
        </td>
        <td>
          The organizational, hierarchical mechanisms used to decompose complex models into modular subsystems.
          <br>&bull; <strong>Package:</strong> Tabbed folder icon. Packages can enclose structural things, use cases, or other nested packages to define namespace boundaries, access visibilities, and deployment units.
        </td>
      </tr>
      <tr>
        <td><strong>4. Annotational Things</strong><br><em>(Explanatory blocks)</em></td>
        <td>
          &bull; Note (Comment)
        </td>
        <td>
          The explanatory and documentation elements of a model.
          <br>&bull; <strong>Note:</strong> A dog-eared rectangle connected via a dashed line to the target element. Used to express architectural design rationale, mathematical constraints, performance requirements, or informal engineering comments.
        </td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">4. Architectural Relationships Connecting Things</h4>
  <p>These Things are bound through four fundamental relationships: <strong>Dependency</strong> (dashed line with open arrowhead showing that changes to one element affect another), <strong>Association</strong> (solid line showing structural connections, with aggregations/compositions as specialized forms), <strong>Generalization</strong> (solid line with hollow triangular arrowhead denoting inheritance), and <strong>Realization</strong> (dashed line with hollow triangular arrowhead denoting interface implementation).</p>
</div>
        """
    })

    # U1-L05
    questions.append({
        "id": "U1-L05",
        "unit": "1",
        "year": "2022-23",
        "year_display": "[2022-23]",
        "title": "Explain the architecture of UML.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Introduction to UML Architecture & The 4+1 View Model</h4>
  <p>Software architecture represents the set of significant design decisions regarding the organization of a software system, the selection of structural elements and their interfaces, their behavior as specified in collaborations, and their composition into progressively larger subsystems. To manage this multi-faceted complexity without cluttering a single visual diagram, UML utilizes the celebrated <strong>4+1 Architectural View Model</strong> formulated by Philippe Kruchten.</p>

  <h4 class="answer-heading">2. Detailed Breakdown of the 4+1 Views</h4>
  <ul>
    <li><strong>1. Use Case View (The "+1" Center):</strong> Serves as the central organizing pivot that drives all other views. It captures the external functional requirements from the perspective of external actors (users, third-party systems). <em>Primary diagrams:</em> Use Case Diagrams, Activity Diagrams.</li>
    <li><strong>2. Design / Logical View:</strong> Models the static vocabulary of the problem domain and the functional decomposition into classes, interfaces, and collaborative structures. It addresses <em>what</em> functional services the system provides. <em>Primary diagrams:</em> Class Diagrams, Object Diagrams, State Machine Diagrams.</li>
    <li><strong>3. Implementation / Development View:</strong> Focuses on the actual software artifact modules, package structures, source code management, build artifacts, libraries, and binaries. It addresses <em>how</em> code is organized and packaged. <em>Primary diagrams:</em> Component Diagrams, Package Diagrams.</li>
    <li><strong>4. Process View:</strong> Addresses runtime concurrency, threading models, synchronization, throughput, system availability, and inter-process communication (IPC). It represents the dynamic execution environment. <em>Primary diagrams:</em> Sequence Diagrams, Communication Diagrams, Activity Diagrams with concurrency swimlanes.</li>
    <li><strong>5. Deployment / Physical View:</strong> Models the physical hardware topology, computing nodes, networking links, cloud infrastructure, and the mapping of software components onto execution environments. <em>Primary diagrams:</em> Deployment Diagrams.</li>
  </ul>

  <h4 class="answer-heading">3. Clean Architectural Diagram (4+1 Views)</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 680 340" width="100%" height="340" xmlns="http://www.w3.org/2000/svg">
      <!-- Background -->
      <rect x="0" y="0" width="680" height="340" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>
      
      <!-- Top Left: Design View -->
      <rect x="40" y="30" width="220" height="90" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="150" y="55" font-family="monospace" font-size="13" font-weight="bold" fill="#0969da" text-anchor="middle">DESIGN / LOGICAL VIEW</text>
      <text x="150" y="75" font-family="sans-serif" font-size="11" fill="#1f2328" text-anchor="middle">Vocabulary &amp; Functionality</text>
      <text x="150" y="95" font-family="monospace" font-size="10" fill="#656d76" text-anchor="middle">Class &amp; State Diagrams</text>

      <!-- Top Right: Process View -->
      <rect x="420" y="30" width="220" height="90" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="530" y="55" font-family="monospace" font-size="13" font-weight="bold" fill="#0969da" text-anchor="middle">PROCESS VIEW</text>
      <text x="530" y="75" font-family="sans-serif" font-size="11" fill="#1f2328" text-anchor="middle">Concurrency &amp; Performance</text>
      <text x="530" y="95" font-family="monospace" font-size="10" fill="#656d76" text-anchor="middle">Sequence &amp; Thread Models</text>

      <!-- Center: Use Case View -->
      <rect x="230" y="130" width="220" height="80" fill="#ffffff" stroke="#0969da" stroke-width="2"/>
      <text x="340" y="155" font-family="monospace" font-size="13" font-weight="bold" fill="#0969da" text-anchor="middle">USE CASE VIEW (+1)</text>
      <text x="340" y="175" font-family="sans-serif" font-size="11" fill="#1f2328" text-anchor="middle">System Requirements &amp; Scenarios</text>
      <text x="340" y="195" font-family="monospace" font-size="10" fill="#656d76" text-anchor="middle">Drives All 4 Surrounding Views</text>

      <!-- Bottom Left: Implementation View -->
      <rect x="40" y="220" width="220" height="90" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="150" y="245" font-family="monospace" font-size="13" font-weight="bold" fill="#0969da" text-anchor="middle">IMPLEMENTATION VIEW</text>
      <text x="150" y="265" font-family="sans-serif" font-size="11" fill="#1f2328" text-anchor="middle">Component Organization &amp; Build</text>
      <text x="150" y="285" font-family="monospace" font-size="10" fill="#656d76" text-anchor="middle">Component &amp; Package Diagrams</text>

      <!-- Bottom Right: Deployment View -->
      <rect x="420" y="220" width="220" height="90" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="530" y="245" font-family="monospace" font-size="13" font-weight="bold" fill="#0969da" text-anchor="middle">DEPLOYMENT VIEW</text>
      <text x="530" y="265" font-family="sans-serif" font-size="11" fill="#1f2328" text-anchor="middle">Hardware Topology &amp; Cloud Infra</text>
      <text x="530" y="285" font-family="monospace" font-size="10" fill="#656d76" text-anchor="middle">Nodes, Networks &amp; Execution</text>

      <!-- Connecting Lines to Central Use Case View -->
      <line x1="200" y1="120" x2="250" y2="140" stroke="#0969da" stroke-width="1.5" stroke-dasharray="4,4"/>
      <line x1="480" y1="120" x2="430" y2="140" stroke="#0969da" stroke-width="1.5" stroke-dasharray="4,4"/>
      <line x1="200" y1="220" x2="250" y2="200" stroke="#0969da" stroke-width="1.5" stroke-dasharray="4,4"/>
      <line x1="480" y1="220" x2="430" y2="200" stroke="#0969da" stroke-width="1.5" stroke-dasharray="4,4"/>
    </svg>
    <span class="diagram-caption">Figure U1-L05: Kruchten's 4+1 Architectural View Model of UML</span>
  </div>

  <h4 class="answer-heading">4. OMG 4-Layer Metamodeling Hierarchy (M0 to M3)</h4>
  <p>Beyond the functional views, UML itself is architected on a rigorous four-layer metamodel hierarchy standardized by the Object Management Group:</p>
  <ul>
    <li><strong>M0 Layer (User Objects / Runtime Instances):</strong> Concrete runtime entities residing in physical memory (e.g., <code>johnsAccount:SavingsAccount</code> at address <code>0x7ffee1b</code>).</li>
    <li><strong>M1 Layer (UML Models):</strong> The classes, associations, and states modeled by software developers (e.g., class <code>BankAccount</code>, association <code>TransfersTo</code>).</li>
    <li><strong>M2 Layer (UML Metamodel):</strong> The definitions of UML concepts themselves (e.g., <code>Class</code>, <code>Attribute</code>, <code>Operation</code>, <code>Association</code>).</li>
    <li><strong>M3 Layer (Meta-Object Facility - MOF):</strong> The foundational root meta-metamodel that defines the grammar for constructing metamodels (e.g., <code>MOF_Class</code>, <code>MOF_Property</code>).</li>
  </ul>
</div>
        """
    })

    # U1-L06
    questions.append({
        "id": "U1-L06",
        "unit": "1",
        "year": "2022-23",
        "year_display": "[2022-23]",
        "title": "Explain the principles and importance of modelling.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Concept and Definition of Modeling</h4>
  <p>A <strong>model</strong> is an explicit simplification of reality—an abstract representation of a system constructed to understand, specify, design, analyze, or verify the system prior to its physical implementation. Just as aeronautical engineers construct scale wind-tunnel models of airfoils rather than immediately manufacturing full-scale jet airliners, software engineers build UML models to simulate behavioral dynamics, evaluate architectural trade-offs, and detect design flaws early when the cost of remediation is minimal.</p>

  <h4 class="answer-heading">2. The Four Foundational Principles of Modeling (Booch, Rumbaugh, Jacobson)</h4>
  <ol>
    <li><strong>Principle 1: The Choice of What Models to Create Has a Profound Influence on How a Problem Is Attacked and How a Solution Is Shaped:</strong>
      <p>The choice of modeling paradigm fundamentally dictates the architecture of the solution. If one chooses an algorithmic procedural model (e.g., Data Flow Diagrams), the solution crystallizes around centralized sequential transformations of passive data. If one chooses an object-oriented model (UML), the system emerges as an ecosystem of autonomous, collaborating entities encapsulating state and behavior.</p>
    </li>
    <li><strong>Principle 2: Every Model May Be Expressed at Different Levels of Precision:</strong>
      <p>A single system must be modelable at multiple granularities of detail. Early in requirements elicitation, an architect constructs high-level, elided models (e.g., conceptual class diagrams with class names only) to communicate system boundaries with executive stakeholders. Later during implementation design, the same model is refined with rigorous precision, specifying typed method signatures, parameter passing semantics, thread safety locks, and algorithmic pre/post-conditions.</p>
    </li>
    <li><strong>Principle 3: The Best Models Are Connected to Reality:</strong>
      <p>A model cannot exist as an abstract mathematical fantasy disconnected from physical computing reality. Software models must directly account for hardware topologies, network bandwidth limits, database transaction isolation guarantees, and programming language constructs. A clean architecture ensures that when changes occur in the business domain, the corresponding modifications map directly and traceably to the software model and its code.</p>
    </li>
    <li><strong>Principle 4: No Single Model Is Ever Sufficient; Every Non-Trivial System Requires Multiple Nearly Independent Views:</strong>
      <p>A complex software system cannot be captured completely in a single monolithic diagram. Attempting to display static data structures, asynchronous network messaging, thread pools, and physical servers simultaneously yields illegible visual chaos. High-integrity engineering necessitates decomposing the model into multiple complementary, orthogonal viewpoints (e.g., static structural view, behavioral interaction view, physical deployment view) as captured by Kruchten's 4+1 view architecture.</p>
    </li>
  </ol>

  <h4 class="answer-heading">3. Critical Importance of Modeling in Software Engineering</h4>
  <ul>
    <li><strong>Visualizing the System as It Is or as It Needs to Be:</strong> Visual models allow teams to comprehend architectural patterns and relationships that are obscured within millions of lines of flat text files.</li>
    <li><strong>Specifying Structure and Behavior Unambiguously:</strong> Standardized UML notations remove natural language ambiguities from requirement documents, providing formal contracts for developers.</li>
    <li><strong>Providing a Template for System Construction:</strong> Models directly guide code generation and implementation, serving as the blueprint from which class definitions, database schemas, and API routes are derived.</li>
    <li><strong>Documenting Architectural Decisions Made:</strong> Models capture critical design rationales, invariants, and trade-offs, preserving institutional knowledge against developer turnover.</li>
    <li><strong>Risk Mitigation and Cost Reduction:</strong> Discovering an architectural defect in a UML class or sequence diagram costs roughly 1/100th of discovering and refactoring that same flaw after deployment to production.</li>
  </ul>
</div>
        """
    })

    # U1-L07
    questions.append({
        "id": "U1-L07",
        "unit": "1",
        "year": "2022-23",
        "year_display": "[2022-23]",
        "title": "Discuss the conceptual model of UML in detail.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Architecture of the Conceptual Model of UML</h4>
  <p>To master the Unified Modeling Language, one must understand its <strong>Conceptual Model</strong>. The conceptual model of UML is founded upon three integrated pillars: <strong>Building Blocks</strong>, <strong>Rules of UML</strong>, and <strong>Common Mechanisms</strong>. Together, these pillars define the grammar, vocabulary, and semantic execution principles of the language.</p>

  <h4 class="answer-heading">2. Pillar 1: Building Blocks of UML</h4>
  <p>As established in the OMG specification, the building blocks are categorized into three core components:</p>
  <ul>
    <li><strong>Things:</strong> The primary model atoms comprising Structural Things (classes, interfaces, nodes, use cases), Behavioral Things (interactions, state machines), Grouping Things (packages), and Annotational Things (notes).</li>
    <li><strong>Relationships:</strong> The semantic bindings between things:
      <ul>
        <li><em>Dependency:</em> Semantic connection where change to independent element impacts dependent element (dashed arrow).</li>
        <li><em>Association:</em> Structural relationship describing a set of links between object instances (solid line with multiplicity).</li>
        <li><em>Generalization:</em> Specialization relationship connecting child class to parent base class (solid line with open triangular head).</li>
        <li><em>Realization:</em> Contractual relationship where an implementation agrees to satisfy an interface specification (dashed line with open triangular head).</li>
      </ul>
    </li>
    <li><strong>Diagrams:</strong> Graphical visualizations of model elements representing Structural Diagrams (Class, Object, Component, Deployment) and Behavioral Diagrams (Use Case, Sequence, Communication, State Machine, Activity).</li>
  </ul>

  <h4 class="answer-heading">3. Pillar 2: Rules of UML (Semantic Well-Formedness)</h4>
  <p>The rules of UML define the syntactic and semantic constraints that govern how building blocks are legally assembled:</p>
  <ul>
    <li><strong>Names:</strong> Every element (class, attribute, operation) must have a legal textual identifier conforming to scope and namespace uniqueness constraints.</li>
    <li><strong>Scope:</strong> Defines the context that bounds a name, preventing naming collisions across packages or class namespaces.</li>
    <li><strong>Visibility:</strong> Dictates whether an element can be accessed outside its defining scope (<code>+</code> Public, <code>-</code> Private, <code>#</code> Protected, <code>~</code> Package).</li>
    <li><strong>Integrity:</strong> Rules dictating how elements legally relate to one another (e.g., an interface cannot directly inherit from a concrete class; an association cannot connect to a note).</li>
    <li><strong>Execution:</strong> Dynamic semantics defining what it means to run or simulate an interaction or state transition over time.</li>
  </ul>

  <h4 class="answer-heading">4. Pillar 3: Common Mechanisms of UML</h4>
  <p>UML achieves visual simplicity and universal applicability by consistently applying four common mechanisms across all diagram types:</p>
  <ol>
    <li><strong>Specifications:</strong> Behind every visual graphical symbol lies a detailed textual specification containing full typing rules, constraints, invariants, and implementation semantics.</li>
    <li><strong>Adornments:</strong> Every visual element has a basic canonical notation that can be embellished with textual adornments (e.g., multiplicity <code>0..*</code>, navigation arrows, abstract italicization).</li>
    <li><strong>Common Divisions:</strong>
      <ul>
        <li><em>Class vs. Object:</em> Separation between the abstract type classifier (e.g., <code>Account</code>) and its runtime instance (e.g., <code><u>acc1 : Account</u></code>).</li>
        <li><em>Interface vs. Implementation:</em> Separation between public behavioral contracts and private algorithmic realization.</li>
      </ul>
    </li>
    <li><strong>Extensibility Mechanisms:</strong> Allows UML to be tailored to specialized technical domains (e.g., Real-Time Embedded Systems, Web Engineering) without altering the foundational metamodel:
      <ul>
        <li><em>Stereotypes (<code>&laquo;stereotype&raquo;</code>):</em> Extends the vocabulary of UML by introducing new domain-specific model elements (e.g., <code>&laquo;entity&raquo;</code>, <code>&laquo;service&raquo;</code>, <code>&laquo;thread&raquo;</code>).</li>
        <li><em>Tagged Values (<code>{tag = value}</code>):</em> Extends properties of an element with arbitrary metadata (e.g., <code>{version = 2.4}</code>, <code>{author = "DBA"}</code>).</li>
        <li><em>Constraints (<code>{expression}</code>):</em> Formal rules restricting semantics (e.g., <code>{balance &gt;= 0}</code>, <code>{ordered}</code>).</li>
      </ul>
    </li>
  </ol>
</div>
        """
    })

    # U1-L08
    questions.append({
        "id": "U1-L08",
        "unit": "1",
        "year": "2023-24",
        "year_display": "[2023-24]",
        "title": "Discuss the concept of encapsulation with suitable example.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Formal Definition and Conceptual Architecture of Encapsulation</h4>
  <p><strong>Encapsulation</strong> is the fundamental object-oriented design mechanism that binds together data fields (state) and the operations (behavior) that manipulate them into a single, cohesive structural unit called a <strong>class</strong>, while strictly hiding the internal representation and memory layout from external manipulation. It acts as a protective barrier preventing external client code from directly accessing or corrupting an object's internal state.</p>
  <p>Encapsulation is operationalized through three standardized access control specifiers:</p>
  <ul>
    <li><strong>Private (<code>-</code>):</strong> Inaccessible to any code outside the declaring class. Strictly used for state variables and internal helper procedures to guarantee class invariant integrity.</li>
    <li><strong>Protected (<code>#</code>):</strong> Accessible to member functions of the declaring class and its derived child classes, facilitating white-box reuse.</li>
    <li><strong>Public (<code>+</code>):</strong> Accessible globally across the entire system. Represents the formal, stable service contract offered to consumers.</li>
  </ul>

  <h4 class="answer-heading">2. Practical Necessity: Invariant Protection & Loose Coupling</h4>
  <p>Without encapsulation, data structs allow client code to assign arbitrary, invalid values (e.g., assigning a negative account balance, or setting a date to February 31st). With encapsulation, mutations occur exclusively through public setter methods or domain operations that validate inputs, enforce business constraints, and preserve the object's <strong>class invariants</strong>.</p>

  <h4 class="answer-heading">3. Comprehensive C++ Industrial Demonstration: Secure Digital Wallet</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;stdexcept&gt;

class DigitalWallet {
private:
    // Strictly encapsulated private state variables
    std::string walletId;
    double balance;
    double dailySpendLimit;
    double currentDailySpent;

    // Private internal helper function (encapsulated logic)
    bool isTransactionAllowed(double amount) const {
        return (amount &gt; 0.0) &amp;&amp; 
               (balance &gt;= amount) &amp;&amp; 
               ((currentDailySpent + amount) &lt;= dailySpendLimit);
    }

public:
    // Constructor enforcing state validity at initialization
    DigitalWallet(const std::string&amp; id, double initialDeposit, double limit)
        : walletId(id), dailySpendLimit(limit), currentDailySpent(0.0) {
        if (initialDeposit &lt; 0.0 || limit &lt;= 0.0) {
            throw std::invalid_argument("Initial funds and limits must be positive.");
        }
        balance = initialDeposit;
    }

    // Public business operations enforcing invariants
    bool transferFunds(double amount, const std::string&amp; destinationAccount) {
        if (!isTransactionAllowed(amount)) {
            std::cout &lt;&lt; "[REJECTED] Transaction of $" &lt;&lt; amount 
                      &lt;&lt; " violates balance or daily spending limit.\\n";
            return false;
        }

        balance -= amount;
        currentDailySpent += amount;
        std::cout &lt;&lt; "[SUCCESS] Transferred $" &lt;&lt; amount &lt;&lt; " to " &lt;&lt; destinationAccount 
                  &lt;&lt; ". Remaining Balance: $" &lt;&lt; balance &lt;&lt; "\\n";
        return true;
    }

    void deposit(double amount) {
        if (amount &lt;= 0.0) {
            std::cout &lt;&lt; "[ERROR] Deposit amount must be strictly positive.\\n";
            return;
        }
        balance += amount;
        std::cout &lt;&lt; "[DEPOSIT] Added $" &lt;&lt; amount &lt;&lt; ". Current Balance: $" &lt;&lt; balance &lt;&lt; "\\n";
    }

    // Controlled read-only access (Getters)
    double getBalance() const { return balance; }
    std::string getWalletId() const { return walletId; }
};

int main() {
    DigitalWallet myWallet("WAL-9081", 1000.0, 500.0);

    // External client cannot do: myWallet.balance = -999999; (Compile Error)
    myWallet.deposit(200.0);
    myWallet.transferFunds(350.0, "MERCHANT-AMAZON"); // Allowed ($350 <= $500 limit)
    myWallet.transferFunds(200.0, "MERCHANT-APPLE");  // Rejected (Total $550 > $500 limit)

    return 0;
}</code></pre>

  <h4 class="answer-heading">4. Encapsulation vs. Information Hiding</h4>
  <p>While often used interchangeably, subtle technical distinctions exist: <strong>Encapsulation</strong> is the structural packaging mechanism (enclosing data and methods in a class container), whereas <strong>Information Hiding</strong> is the architectural principle of intentionally concealing design decisions and physical data representations behind an immutable interface so clients cannot depend on implementation volatility.</p>
</div>
        """
    })

    # U1-L09
    questions.append({
        "id": "U1-L09",
        "unit": "1",
        "year": "2023-24",
        "year_display": "[2023-24]",
        "title": "What do you mean by polymorphism? Explain it with an example.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Definition and Essence of Polymorphism</h4>
  <p>Derived from Greek roots meaning <em>"many forms"</em> (<em>poly</em> = many, <em>morph</em> = form), <strong>Polymorphism</strong> is the foundational object-oriented capability that enables a single identifier, method name, or operator to exhibit distinct behaviors depending on the actual underlying type of the object invoked or the signature of arguments supplied at call-site.</p>
  <p>Polymorphism decouples high-level business policies from low-level execution details. Systems can manipulate collections of diverse entities uniformly through an abstract base interface, while each specific subtype automatically executes its specialized behavior at runtime.</p>

  <h4 class="answer-heading">2. Taxonomy: Compile-Time vs. Runtime Polymorphism</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Characteristic</th>
        <th style="width: 37%;">Compile-Time (Static) Polymorphism</th>
        <th style="width: 38%;">Runtime (Dynamic) Polymorphism</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Resolution Mechanism</strong></td>
        <td>Resolved at compile/link time by static type analysis and name mangling.</td>
        <td>Resolved at runtime via Virtual Method Tables (VTable) and <code>vptr</code> dereference.</td>
      </tr>
      <tr>
        <td><strong>Language Constructs</strong></td>
        <td>Function Overloading, Operator Overloading, C++ Templates.</td>
        <td>Virtual member functions, pure virtual interfaces, base pointers/references.</td>
      </tr>
      <tr>
        <td><strong>Performance Impact</strong></td>
        <td>Zero runtime overhead; calls can be aggressively inlined by compiler.</td>
        <td>Minor overhead due to indirect pointer dereference (memory read) and inability to inline.</td>
      </tr>
      <tr>
        <td><strong>Flexibility</strong></td>
        <td>Types must be known at compile time; inflexible to plugin architectures.</td>
        <td>Highly extensible; new derived classes can be linked at runtime without recompilation.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. Comprehensive C++ Example: Industrial Notification Gateway</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;vector&gt;
#include &lt;memory&gt;

// Abstract Base Class declaring polymorphic interface
class NotificationChannel {
public:
    virtual ~NotificationChannel() = default;

    // Pure virtual method establishing dynamic polymorphic contract
    virtual void sendNotification(const std::string&amp; recipient, 
                                 const std::string&amp; message) = 0;
};

// Concrete Derived Class 1: SMS Gateway
class SMSChannel : public NotificationChannel {
public:
    void sendNotification(const std::string&amp; recipient, 
                          const std::string&amp; message) override {
        std::cout &lt;&lt; "[SMS-GATEWAY] Sending SMS to " &lt;&lt; recipient 
                  &lt;&lt; " via Cellular Network. Payload: \"" &lt;&lt; message &lt;&lt; "\"\\n";
    }
};

// Concrete Derived Class 2: Email Gateway
class EmailChannel : public NotificationChannel {
public:
    void sendNotification(const std::string&amp; recipient, 
                          const std::string&amp; message) override {
        std::cout &lt;&lt; "[SMTP-GATEWAY] Dispatching Email to " &lt;&lt; recipient 
                  &lt;&lt; " via TLS port 587. Subject: Alert, Body: \"" &lt;&lt; message &lt;&lt; "\"\\n";
    }
};

// Concrete Derived Class 3: Push Notification
class PushNotificationChannel : public NotificationChannel {
public:
    void sendNotification(const std::string&amp; recipient, 
                          const std::string&amp; message) override {
        std::cout &lt;&lt; "[APNS/FCM] Pushing Cloud Alert to Token: " &lt;&lt; recipient 
                  &lt;&lt; ". Sound: Default, Message: \"" &lt;&lt; message &lt;&lt; "\"\\n";
    }
};

// Client Subsystem (Adheres to Open-Closed Principle)
void broadcastAlert(const std::vector&lt;std::shared_ptr&lt;NotificationChannel&gt;&gt;&amp; channels,
                    const std::string&amp; userTarget, const std::string&amp; urgentMessage) {
    for (const auto&amp; channel : channels) {
        // Dynamic late binding resolves appropriate sendNotification at runtime
        channel-&gt;sendNotification(userTarget, urgentMessage);
    }
}

int main() {
    std::vector&lt;std::shared_ptr&lt;NotificationChannel&gt;&gt; alertPipeline;
    alertPipeline.push_back(std::make_shared&lt;SMSChannel&gt;());
    alertPipeline.push_back(std::make_shared&lt;EmailChannel&gt;());
    alertPipeline.push_back(std::make_shared&lt;PushNotificationChannel&gt;());

    broadcastAlert(alertPipeline, "+1-555-019-2834 / user@corp.net", "Security Alert: Unauthorized Login Detected");
    return 0;
}</code></pre>

  <h4 class="answer-heading">4. Architectural Underpinning: The VTable Mechanism</h4>
  <p>When a class declares a <code>virtual</code> function, the compiler creates a static array of function pointers called the <strong>Virtual Method Table (VTable)</strong> for that class. Every object instantiated from that class has an invisible pointer (<code>vptr</code>) inserted at offset zero in its memory layout. When <code>channel-&gt;sendNotification()</code> is called, the CPU dereferences <code>channel-&gt;vptr</code>, indexes the slot for <code>sendNotification</code>, and executes an indirect jump to the exact derived function address.</p>
</div>
        """
    })

    # U1-L10
    questions.append({
        "id": "U1-L10",
        "unit": "1",
        "year": "2024-25",
        "year_display": "[2024-25]",
        "title": "Explain the concept of encapsulation and information hiding. How do these principles ensure system security and maintainability? Provide a UML example to demonstrate these principles.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Conceptual Foundations: Encapsulation & Information Hiding</h4>
  <p><strong>Encapsulation</strong> is the structural practice of packing attributes and the operations that process them into an indivisible class container. <strong>Information Hiding</strong> (originally formulated by David Parnas) is the foundational design principle stating that client modules should only be exposed to the necessary public interface contracts of a component, while all internal data structures, algorithms, and storage mechanisms remain hidden.</p>

  <h4 class="answer-heading">2. How These Principles Ensure System Security & Maintainability</h4>
  <ul>
    <li><strong>System Security & Data Integrity:</strong>
      <ul>
        <li><em>Prevents Illegal State Corruption:</em> By marking internal variables <code>private</code>, external malicious or buggy code cannot bypass validation logic (e.g., balance cannot be set to negative or credit card CVV cannot be leaked).</li>
        <li><em>Enforces Privilege Boundaries:</em> In multi-tiered architectures, sensitive cryptographic keys, database connections, and session tokens remain inaccessible to client layers, preventing injection and state-tampering exploits.</li>
      </ul>
    </li>
    <li><strong>System Maintainability & Evolutionary Agility:</strong>
      <ul>
        <li><em>Zero Ripple Effect on Refactoring:</em> A software team can completely rewrite an internal algorithm (e.g., replacing an in-memory <code>std::vector</code> with an indexed B-tree or caching layer) without requiring a single line of client code to be altered or recompiled, provided the public method signatures remain constant.</li>
        <li><em>Localized Unit Testing:</em> Encapsulated components can be isolated, mocked, and thoroughly stress-tested in unit-test suites independently of external system dependencies.</li>
      </ul>
    </li>
  </ul>

  <h4 class="answer-heading">3. Clean UML Class Diagram Demonstrating Encapsulation</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 520 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="520" height="220" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>
      
      <!-- Class Box -->
      <rect x="60" y="20" width="400" height="180" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      
      <!-- Header Compartment -->
      <rect x="60" y="20" width="400" height="35" fill="#f6f8fa" stroke="#1f2328" stroke-width="1"/>
      <text x="260" y="42" font-family="monospace" font-size="14" font-weight="bold" fill="#0969da" text-anchor="middle">PaymentAccount</text>
      
      <!-- Attributes Compartment (Private Information Hiding) -->
      <line x1="60" y1="55" x2="460" y2="55" stroke="#1f2328" stroke-width="1"/>
      <text x="75" y="75" font-family="monospace" font-size="11" fill="#cf222e">- accountId : String</text>
      <text x="75" y="93" font-family="monospace" font-size="11" fill="#cf222e">- secretPinHash : String</text>
      <text x="75" y="111" font-family="monospace" font-size="11" fill="#cf222e">- balanceAmount : Double</text>
      <text x="75" y="129" font-family="monospace" font-size="11" fill="#cf222e">- failedAttempts : Integer</text>
      
      <!-- Operations Compartment (Public Service Contract) -->
      <line x1="60" y1="138" x2="460" y2="138" stroke="#1f2328" stroke-width="1"/>
      <text x="75" y="156" font-family="monospace" font-size="11" fill="#1a7f37">+ authenticate(enteredPin : String) : Boolean</text>
      <text x="75" y="174" font-family="monospace" font-size="11" fill="#1a7f37">+ debitFunds(amount : Double, pin : String) : Boolean</text>
      <text x="75" y="192" font-family="monospace" font-size="11" fill="#1a7f37">+ getSanitizedBalance() : Double</text>
    </svg>
    <span class="diagram-caption">Figure U1-L10: UML Class Diagram Illustrating Information Hiding via Access Specifiers</span>
  </div>

  <h4 class="answer-heading">4. Architectural Security Realization in C++</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;

class PaymentAccount {
private:
    // Hidden private data: Never accessible directly by clients
    std::string secretPinHash;
    double balanceAmount;
    int failedAttempts;

    bool verifyPin(const std::string&amp; enteredPin) {
        // Internal security check
        return (enteredPin == "1234");
    }

public:
    PaymentAccount(std::string pin, double initialBalance)
        : secretPinHash(pin), balanceAmount(initialBalance), failedAttempts(0) {}

    bool debitFunds(double amount, const std::string&amp; pin) {
        if (!verifyPin(pin)) {
            failedAttempts++;
            std::cout &lt;&lt; "[ALERT] Authentication Failure. Attempt: " &lt;&lt; failedAttempts &lt;&lt; "\\n";
            return false;
        }
        if (amount &gt; balanceAmount) {
            std::cout &lt;&lt; "[REJECT] Insufficient funds.\\n";
            return false;
        }
        balanceAmount -= amount;
        std::cout &lt;&lt; "[SECURITY-CLEARED] Debited $" &lt;&lt; amount &lt;&lt; "\\n";
        return true;
    }
};</code></pre>

  <h4 class="answer-heading">5. Architectural Security Heuristics (Parnas' Principles)</h4>
  <p>David Parnas established that a module's design should conceal decisions that are most likely to change or most vulnerable to unauthorized modification. In financial and medical enterprise systems, encapsulating security invariants guarantees:</p>
  <ul>
    <li><strong>Tamper-Resistant State Transitions:</strong> Variables such as <code>balanceAmount</code> or <code>failedAttempts</code> cannot be modified by arbitrary pointers or external modules without executing cryptographic PIN validation.</li>
    <li><strong>Auditability and Regulatory Compliance:</strong> Centralizing mutations inside explicit member methods provides a single choke-point where security audit logging (e.g., logging every debit attempt to an immutable SIEM system) is guaranteed to execute without relying on client compliance.</li>
  </ul>
</div>
"""
    })

    # U1-L11
    questions.append({
        "id": "U1-L11",
        "unit": "1",
        "year": "2024-25",
        "year_display": "[2024-25]",
        "title": "Compare and contrast object-oriented modeling with structured modeling. Provide a detailed example of a banking system modeled using both approaches.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Paradigm Foundations: Structured vs. Object-Oriented Modeling</h4>
  <p><strong>Structured Modeling</strong> (traditionally implemented via Structured Analysis and Structured Design - SA/SD) decomposes a system based on <em>functions and data flows</em>. It treats data and algorithms as fundamentally separate entities: passive data structures flow through a pipeline of active transforms or subroutines. In contrast, <strong>Object-Oriented Modeling (OOM)</strong> models systems as collaborative societies of autonomous <em>objects</em> that encapsulate both data structure and behavior within unified boundaries.</p>

  <h4 class="answer-heading">2. Detailed Comparative Analysis</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">Dimension</th>
        <th style="width: 40%;">Structured Modeling (SA/SD)</th>
        <th style="width: 40%;">Object-Oriented Modeling (OOM)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Primary Focus</strong></td>
        <td>Process-centric: What functions/procedures transform input data to output data?</td>
        <td>Data-and-Responsibility-centric: Which domain entities encapsulate state and operational contracts?</td>
      </tr>
      <tr>
        <td><strong>Basic Artifacts</strong></td>
        <td>Data Flow Diagrams (DFDs), Structure Charts, Data Dictionaries, State Transition Diagrams.</td>
        <td>UML Class, Object, Sequence, State Machine, and Use Case Diagrams.</td>
      </tr>
      <tr>
        <td><strong>Coupling &amp; Cohesion</strong></td>
        <td>Functions frequently share global data structures, leading to subtle cross-module coupling.</td>
        <td>High cohesion within classes; low coupling achieved via strict public interfaces.</td>
      </tr>
      <tr>
        <td><strong>Reusability</strong></td>
        <td>Subroutines can be reused, but procedural code is tightly coupled to specific data shapes.</td>
        <td>Extremely high through inheritance, polymorphic abstraction, and component composition.</td>
      </tr>
      <tr>
        <td><strong>Scalability to Large Systems</strong></td>
        <td>Becomes unmanageable when hundreds of procedures share evolving data stores.</td>
        <td>Excels in enterprise systems by partitioning complexity into self-governing classes and packages.</td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. Detailed Case Study: Banking System Modeling</h4>
  
  <h5 class="answer-heading">A. Structured Approach (Process-Driven Pipeline)</h5>
  <p>In structured analysis, the banking system is decomposed into a top-level Context Diagram and functional Level-1 Data Flow Diagrams (DFD):</p>
  <ul>
    <li><strong>External Entities:</strong> <code>Customer</code>, <code>Central Bank Clearinghouse</code>.</li>
    <li><strong>Processes:</strong> <code>Process 1.0: Authenticate Customer</code>, <code>Process 2.0: Process Withdrawal</code>, <code>Process 3.0: Calculate Monthly Interest</code>, <code>Process 4.0: Generate Statement</code>.</li>
    <li><strong>Data Stores:</strong> <code>D1: Account Database Table</code>, <code>D2: Transaction Ledger File</code>.</li>
    <li><em>Critical Architectural Weakness:</em> Both Process 2.0 and Process 3.0 directly read and write to <code>D1: Account Database</code>. If a new attribute (e.g., <code>overdraftLimit</code> or <code>currencyType</code>) is added to the database record, both Process 2.0, Process 3.0, and Process 4.0 code routines must be manually revised and re-tested.</li>
  </ul>

  <h5 class="answer-heading">B. Object-Oriented Approach (Collaborative Entity Society)</h5>
  <p>In OOM, the system is modeled as discrete domain entities with clear encapsulation barriers and polymorphic specializations:</p>
  <ul>
    <li><strong>Classes:</strong>
      <ul>
        <li><code>Customer</code>: Encapsulates customer credentials, identity verification, and a collection of owned accounts.</li>
        <li><code>Account</code> (Abstract Class): Encapsulates private <code>accountNumber</code>, <code>balance</code>, and transactions history; defines operations <code>deposit()</code>, <code>withdraw()</code>, and abstract <code>applyMonthlyMaintenance()</code>.</li>
        <li><code>SavingsAccount</code> &amp; <code>CurrentAccount</code>: Inherit from <code>Account</code>; specialize overdraft and interest rules polymorphically.</li>
        <li><code>TransactionRecord</code>: Encapsulates timestamp, debit/credit metadata, and audit checksums.</li>
      </ul>
    </li>
    <li><em>Architectural Advantage:</em> Database schema details are hidden within persistence mappings. Adding currency support or overdraft accounts modifies only the specific class internals without affecting external banking transaction services.</li>
  </ul>
</div>
        """
    })

    # U1-L12
    questions.append({
        "id": "U1-L12",
        "unit": "1",
        "year": "2024-25",
        "year_display": "[2024-25]",
        "title": "Discuss the importance of architecture in object-oriented modeling. Design a UML architecture diagram for a cloud-based file-sharing system.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Strategic Importance of Architecture in Object-Oriented Systems</h4>
  <p>In software engineering, <strong>Architecture</strong> represents the master blueprint that defines the fundamental organization of a system, its high-level components, their structural relationships, communication protocols, and the evolutionary design principles that guide its construction. Without a disciplined architecture, object-oriented systems inevitably degrade into an unstructured morass of tightly coupled classes, often termed the <em>"Big Ball of Mud"</em>.</p>
  <p>Architecture fulfills four vital roles in OO modeling:</p>
  <ul>
    <li><strong>Complexity Partitioning:</strong> Divides massive systems into manageable, decoupled architectural tiers (Presentation, Business Logic, Persistence, Infrastructure) and microservices.</li>
    <li><strong>Non-Functional Requirement Enforcement:</strong> Directs how quality attributes such as scalability, fault tolerance, low latency, and distributed security are realized across runtime nodes.</li>
    <li><strong>Team Parallelism and Governance:</strong> Establishes clear API contracts allowing dozens of autonomous feature teams to develop and deploy independent subsystems simultaneously.</li>
    <li><strong>Lifecycle Longevity:</strong> Accommodates technology churn (e.g., swapping SQL databases or cloud storage providers) without invalidating core business domain models.</li>
  </ul>

  <h4 class="answer-heading">2. UML Architectural Diagram: Cloud-Based File-Sharing System</h4>
  <p>Below is the architectural deployment and component model for a high-scale file-sharing platform (analogous to Google Drive or Dropbox), displaying client tiers, API gateways, decoupled microservices, and storage layers:</p>

  <div class="diagram-container">
    <svg viewBox="0 0 680 380" width="100%" height="380" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="380" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Client Tier Node -->
      <rect x="30" y="40" width="160" height="290" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="110" y="65" font-family="monospace" font-size="12" font-weight="bold" fill="#0969da" text-anchor="middle">&laquo;device&raquo;</text>
      <text x="110" y="85" font-family="sans-serif" font-size="12" font-weight="bold" fill="#1f2328" text-anchor="middle">Client Tier</text>
      
      <rect x="45" y="110" width="130" height="45" fill="#ffffff" stroke="#1f2328" stroke-width="1"/>
      <text x="110" y="135" font-family="monospace" font-size="10" fill="#1f2328" text-anchor="middle">&laquo;component&raquo; Web App</text>
      
      <rect x="45" y="170" width="130" height="45" fill="#ffffff" stroke="#1f2328" stroke-width="1"/>
      <text x="110" y="195" font-family="monospace" font-size="10" fill="#1f2328" text-anchor="middle">&laquo;component&raquo; Mobile App</text>

      <rect x="45" y="230" width="130" height="45" fill="#ffffff" stroke="#1f2328" stroke-width="1"/>
      <text x="110" y="255" font-family="monospace" font-size="10" fill="#1f2328" text-anchor="middle">&laquo;component&raquo; Desktop Sync</text>

      <!-- API Gateway -->
      <rect x="230" y="130" width="120" height="110" fill="#f6f8fa" stroke="#0969da" stroke-width="2"/>
      <text x="290" y="155" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">&laquo;node&raquo;</text>
      <text x="290" y="175" font-family="sans-serif" font-size="11" font-weight="bold" fill="#1f2328" text-anchor="middle">API Gateway</text>
      <text x="290" y="200" font-family="monospace" font-size="9" fill="#656d76" text-anchor="middle">TLS / Auth / Route</text>

      <!-- Connections Client to Gateway -->
      <line x1="175" y1="135" x2="230" y2="165" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="175" y1="195" x2="230" y2="185" stroke="#1f2328" stroke-width="1.5"/>
      <line x1="175" y1="255" x2="230" y2="205" stroke="#1f2328" stroke-width="1.5"/>

      <!-- Microservices Tier -->
      <rect x="390" y="40" width="250" height="140" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="515" y="60" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">&laquo;cluster&raquo; Application Services</text>

      <rect x="405" y="75" width="105" height="40" fill="#ffffff" stroke="#1f2328" stroke-width="1"/>
      <text x="457" y="100" font-family="monospace" font-size="9" fill="#1f2328" text-anchor="middle">File Metadata</text>

      <rect x="525" y="75" width="105" height="40" fill="#ffffff" stroke="#1f2328" stroke-width="1"/>
      <text x="577" y="100" font-family="monospace" font-size="9" fill="#1f2328" text-anchor="middle">User Auth</text>

      <rect x="405" y="125" width="105" height="40" fill="#ffffff" stroke="#1f2328" stroke-width="1"/>
      <text x="457" y="150" font-family="monospace" font-size="9" fill="#1f2328" text-anchor="middle">Chunking Engine</text>

      <rect x="525" y="125" width="105" height="40" fill="#ffffff" stroke="#1f2328" stroke-width="1"/>
      <text x="577" y="150" font-family="monospace" font-size="9" fill="#1f2328" text-anchor="middle">Sync Event Bus</text>

      <!-- Gateway to Microservices -->
      <line x1="350" y1="185" x2="390" y2="110" stroke="#1f2328" stroke-width="1.5"/>

      <!-- Storage Tier -->
      <rect x="390" y="210" width="250" height="120" fill="#f6f8fa" stroke="#1f2328" stroke-width="1.5"/>
      <text x="515" y="230" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">&laquo;persistence&raquo; Cloud Storage Tier</text>

      <rect x="405" y="245" width="105" height="40" fill="#ffffff" stroke="#1f2328" stroke-width="1"/>
      <text x="457" y="270" font-family="monospace" font-size="9" fill="#1f2328" text-anchor="middle">PostgreSQL (Meta)</text>

      <rect x="525" y="245" width="105" height="40" fill="#ffffff" stroke="#1f2328" stroke-width="1"/>
      <text x="577" y="270" font-family="monospace" font-size="9" fill="#1f2328" text-anchor="middle">S3 Object Store</text>

      <!-- Microservices to Storage -->
      <line x1="457" y1="165" x2="457" y2="245" stroke="#1f2328" stroke-width="1.5" stroke-dasharray="3,3"/>
      <line x1="457" y1="165" x2="577" y2="245" stroke="#1f2328" stroke-width="1.5" stroke-dasharray="3,3"/>
    </svg>
    <span class="diagram-caption">Figure U1-L12: UML Architecture Diagram for Cloud-Based File-Sharing Platform</span>
  </div>

  <h4 class="answer-heading">3. Detailed Tier Breakdown & Technical Rationale</h4>
  <ul>
    <li><strong>Client Tier:</strong> Runs rich client applications that perform local file hashing (SHA-256) and delta-chunking. Only modified chunks are transmitted across the WAN, conserving network bandwidth.</li>
    <li><strong>API Gateway Node:</strong> Acts as the single entry perimeter performing SSL/TLS termination, rate limiting, and token-based OAuth2 authentication before routing requests internally.</li>
    <li><strong>Application Microservices Cluster:</strong> Stateless containerized services running on Kubernetes. Separates metadata operations (file directory trees, permissions) from heavy binary stream handling (Chunking Service).</li>
    <li><strong>Dual Storage Tier:</strong> Decouples structured relational metadata (PostgreSQL ensuring ACID transactions for file trees and user privileges) from immutable binary blob storage (Amazon S3 / Ceph ensuring 99.999999999% durability at scale).</li>
  </ul>

  <h4 class="answer-heading">4. Non-Functional Quality Attributes Realized by This Architecture</h4>
  <ul>
    <li><strong>Horizontal Elastic Scalability:</strong> Stateless application microservices scale dynamically behind load balancers in response to CPU utilization, while heavy multi-gigabyte payload transfers bypass application servers via direct presigned S3 URLs.</li>
    <li><strong>High Availability & Disaster Recovery:</strong> The persistence tier utilizes asynchronous multi-region database replication and cross-region blob synchronization, ensuring sub-minute Recovery Point Objectives (RPO) during cloud datacenter outages.</li>
    <li><strong>Zero-Trust Identity Isolation:</strong> All inter-service communications enforce mutual TLS (mTLS) with cryptographically signed JSON Web Tokens (JWT), guaranteeing that an intrusion into a public edge gateway cannot compromise the internal storage tier.</li>
  </ul>
</div>
        """
    })

    # U1-L13
    questions.append({
        "id": "U1-L13",
        "unit": "1",
        "year": "2025-26",
        "year_display": "[2025-26]",
        "title": "Explain the concept of object orientation. Discuss object identity, information hiding, polymorphism, and generosity with suitable examples.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. The Philosophical and Technical Core of Object Orientation</h4>
  <p><strong>Object Orientation (OO)</strong> is a software design philosophy that organizes complex systems into autonomous, interacting software components (objects) that combine encapsulated state with defined behavioral capabilities. Rather than structuring software around rigid procedural algorithms that execute top-down on detached global records, OO systems distribute responsibilities across specialized domain entities communicating via message-passing protocols.</p>

  <h4 class="answer-heading">2. Detailed Discussion of the Four Key Concepts</h4>

  <h5 class="answer-heading">A. Object Identity (OID)</h5>
  <p><strong>Object Identity</strong> is the unique, immutable property of an object that distinguishes it from all other objects in the system, even if two objects possess identical attribute values. In memory, identity is represented by physical heap addresses or unique system identifiers (UUID/OID):</p>
  <ul>
    <li><em>State Equality (Value Equivalence):</em> <code>acc1.balance == acc2.balance</code> (both hold $500).</li>
    <li><em>Identity Equality (Object Reference):</em> <code>&amp;acc1 == &amp;acc2</code> (they reference the exact same memory instance). Two distinct customers may both have $500 balances, but their financial accounts have strictly distinct identities.</li>
  </ul>

  <h5 class="answer-heading">B. Information Hiding</h5>
  <p>Conceals the internal implementation details and data structures of an object behind an abstract public interface. Clients can only request operations via public member methods, ensuring that internal state variables (marked <code>private</code>) cannot be corrupted and internal algorithmic refactorings do not impact consuming clients.</p>

  <h5 class="answer-heading">C. Polymorphism</h5>
  <p>Enables a single uniform interface to control disparate concrete behaviors. Through dynamic binding and virtual method tables, calling <code>shape-&gt;render()</code> automatically executes the correct drawing routine for a <code>Circle</code>, <code>Rectangle</code>, or <code>Polygon</code> based on the runtime instance type.</p>

  <h5 class="answer-heading">D. Generosity (Genericity / Parameterized Types)</h5>
  <p><strong>Generosity</strong> (also known as <em>Genericity</em> or Parametric Polymorphism) is the programming mechanism that allows classes, interfaces, and algorithms to be defined with <em>type parameters</em> rather than concrete types. This empowers engineers to author highly reusable, type-safe data structures (e.g., generic stacks, queues, hash maps) once, and instantiate them for integers, floating-point numbers, or custom user objects without resorting to dangerous <code>void*</code> casts or code duplication.</p>

  <h4 class="answer-heading">3. Comprehensive C++ Program Demonstrating All Four Concepts</h4>
  <pre class="code-block"><code>#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;vector&gt;
#include &lt;memory&gt;

// Concept 4: Generosity (Generic Container Template)
template &lt;typename T&gt;
class SecureRepository {
private:
    std::vector&lt;T&gt; items;
public:
    void add(const T&amp; item) { items.push_back(item); }
    size_t count() const { return items.size(); }
    const T&amp; get(size_t index) const { return items.at(index); }
};

// Concept 2: Information Hiding & Abstract Base
class BankCustomer {
private:
    std::string nationalId; // Hidden internal state
    std::string fullName;

public:
    BankCustomer(std::string id, std::string name) 
        : nationalId(std::move(id)), fullName(std::move(name)) {}
    virtual ~BankCustomer() = default;

    // Concept 3: Polymorphic method
    virtual void printCustomerProfile() const {
        std::cout &lt;&lt; "[Standard Customer] Name: " &lt;&lt; fullName &lt;&lt; "\\n";
    }

    std::string getId() const { return nationalId; }
};

// Specialized Subtype
class VIPCustomer : public BankCustomer {
    double creditAllowance;
public:
    VIPCustomer(std::string id, std::string name, double credit)
        : BankCustomer(std::move(id), std::move(name)), creditAllowance(credit) {}

    void printCustomerProfile() const override {
        std::cout &lt;&lt; "[VIP Customer] Name: " &lt;&lt; getId() 
                  &lt;&lt; " | Credit Limit: $" &lt;&lt; creditAllowance &lt;&lt; "\\n";
    }
};

int main() {
    // Concept 1: Object Identity Demonstration
    BankCustomer custA("ID-101", "Alice Smith");
    BankCustomer custB("ID-101", "Alice Smith"); // Identical state

    std::cout &lt;&lt; "custA memory address: " &lt;&lt; &amp;custA &lt;&lt; "\\n";
    std::cout &lt;&lt; "custB memory address: " &lt;&lt; &amp;custB &lt;&lt; "\\n";
    std::cout &lt;&lt; "Are identities identical? " &lt;&lt; ((&amp;custA == &amp;custB) ? "YES" : "NO") &lt;&lt; "\\n";

    // Concept 4: Utilizing Generosity
    SecureRepository&lt;std::shared_ptr&lt;BankCustomer&gt;&gt; repo;
    repo.add(std::make_shared&lt;BankCustomer&gt;("ID-101", "Alice Smith"));
    repo.add(std::make_shared&lt;VIPCustomer&gt;("ID-202", "Robert Bruce", 50000.0));

    // Concept 3: Polymorphism in Action
    for (size_t i = 0; i &lt; repo.count(); ++i) {
        repo.get(i)-&gt;printCustomerProfile();
    }
    return 0;
}</code></pre>
</div>
        """
    })

    # U1-L14
    questions.append({
        "id": "U1-L14",
        "unit": "1",
        "year": "2025-26",
        "year_display": "[2025-26]",
        "title": "Explain the UML architecture and its relationship with object-oriented analysis and design.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. Introduction to UML in the Engineering Lifecycle</h4>
  <p>The <strong>Unified Modeling Language (UML)</strong> is the standardized visual meta-model that serves as the communication medium throughout the entire <strong>Object-Oriented Analysis and Design (OOAD)</strong> lifecycle. While OOAD provides the conceptual and engineering methodology (what steps to take, how to discover entities, how to refine architectures), UML provides the formal graphical notation and semantic grammar to document, validate, and communicate those artifacts across iterative development cycles.</p>

  <h4 class="answer-heading">2. Mapping UML Diagrams Across the OOAD Phases</h4>
  <p>A mature object-oriented development process (such as the Unified Process / Rational Unified Process) progresses through systematic phases. UML diagrams map specifically to each distinct engineering phase:</p>

  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 20%;">OOAD Phase</th>
        <th style="width: 35%;">Engineering Objectives</th>
        <th style="width: 45%;">Applied UML Architectural Diagrams</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Inception &amp; Requirements Elicitation</strong></td>
        <td>Establish project scope, identify external stakeholders, and define functional requirements.</td>
        <td>
          &bull; <strong>Use Case Diagrams:</strong> Capture business actors and system functional boundaries.<br>
          &bull; <strong>Activity Diagrams:</strong> Model high-level business workflows.
        </td>
      </tr>
      <tr>
        <td><strong>2. Object-Oriented Analysis (OOA)</strong></td>
        <td>Discover domain concepts, establish conceptual boundaries, and model system behavior without committing to implementation technologies.</td>
        <td>
          &bull; <strong>Domain Class Diagrams:</strong> High-level conceptual classes with pure business attributes.<br>
          &bull; <strong>System Sequence Diagrams:</strong> Map actor-to-system events and inputs/outputs.<br>
          &bull; <strong>State Machine Diagrams:</strong> Model lifecycle transitions of core business entities.
        </td>
      </tr>
      <tr>
        <td><strong>3. Object-Oriented Design (OOD)</strong></td>
        <td>Refine analysis models into detailed physical software architectures. Select design patterns, define visibility, parameter typing, and physical storage.</td>
        <td>
          &bull; <strong>Detailed Class Diagrams:</strong> Include private attributes, method signatures, navigation arrows, and design pattern roles.<br>
          &bull; <strong>Collaboration / Sequence Diagrams:</strong> Map internal object message dispatching.<br>
          &bull; <strong>Component Diagrams:</strong> Organize classes into packages, JARs, and microservices.
        </td>
      </tr>
      <tr>
        <td><strong>4. Implementation &amp; Deployment</strong></td>
        <td>Translate models into executable code and configure physical cloud/server topologies.</td>
        <td>
          &bull; <strong>Deployment Diagrams:</strong> Map software components to hardware nodes, network topologies, and execution environments.
        </td>
      </tr>
    </tbody>
  </table>

  <h4 class="answer-heading">3. The Bidirectional Traceability Advantage</h4>
  <p>The symbiotic relationship between UML and OOAD creates <strong>bidirectional traceability</strong>. Forward engineering translates detailed UML class and component specifications directly into boilerplate code (e.g., C++, Java, C# classes, and SQL DDL tables). Reverse engineering parses existing source code repositories to reconstruct UML models, enabling software architects to analyze architectural drift and perform code audits on legacy software systems.</p>

  <h4 class="answer-heading">4. Seamless Iterative Evolution in the Unified Process (UP)</h4>
  <p>In classical waterfall engineering, moving from analysis to design requires a disruptive paradigm shift (e.g., translating DFD bubbles into hierarchical Structure Charts). Under the Unified Process driven by UML, the transition is smooth and additive:</p>
  <ul>
    <li>An <em>Analysis Class</em> (identifying domain nouns like <code>Customer</code> and <code>Policy</code>) is not discarded; rather, it is directly enriched during the <em>Design Phase</em> by adding method visibility (<code>private</code>/<code>public</code>), concrete parameter types, exception specifications, and container mappings.</li>
    <li>Dynamic behavioral scenarios captured in early Use Case Narratives are systematically refined into System Sequence Diagrams, which in turn specify the exact public method signatures required in detailed Class Diagrams.</li>
  </ul>
</div>
        """
    })

    # U1-L15
    questions.append({
        "id": "U1-L15",
        "unit": "1",
        "year": "2025-26",
        "year_display": "[2025-26]",
        "title": "Explain how a hospital management system can be designed using object-oriented modeling. Highlight advantages over structured modeling.",
        "content": """
<div class="answer-section">
  <h4 class="answer-heading">1. System Overview: Hospital Management System (HMS)</h4>
  <p>A modern <strong>Hospital Management System (HMS)</strong> manages patient admissions, inpatient ward allocations, doctor scheduling, diagnostic test prescriptions, surgery workflows, and patient billing. Designing an HMS requires managing high domain complexity, strict patient data privacy (HIPAA compliance), and zero tolerance for data corruption.</p>

  <h4 class="answer-heading">2. Object-Oriented Class Design and Architectural Roles</h4>
  <ul>
    <li><strong><code>Person</code> (Abstract Base Class):</strong> Encapsulates common human demographic attributes: <code>id</code>, <code>name</code>, <code>contactInfo</code>, <code>dateOfBirth</code>.</li>
    <li><strong><code>Patient</code> (Specialization):</strong> Inherits from <code>Person</code>; encapsulates <code>medicalHistory</code>, <code>assignedDoctor</code>, active admissions, and prescription lists.</li>
    <li><strong><code>Doctor</code> (Specialization):</strong> Inherits from <code>Person</code>; encapsulates <code>specialization</code>, <code>licenseNumber</code>, schedule slots, and consultation history.</li>
    <li><strong><code>Appointment</code>:</strong> Connects a <code>Patient</code> and a <code>Doctor</code> at a specific <code>dateTime</code>, tracking states (<code>Scheduled</code>, <code>InProgress</code>, <code>Completed</code>, <code>Cancelled</code>).</li>
    <li><strong><code>MedicalRecord</code>:</strong> Encapsulates clinical diagnoses, laboratory test results, and attending physician notes.</li>
    <li><strong><code>Bill</code>:</strong> Aggregates consultation fees, pharmaceutical items, and room charges, providing an encapsulated method <code>calculateTotal()</code>.</li>
  </ul>

  <h4 class="answer-heading">3. High-Contrast UML Class Diagram: Hospital Management System</h4>
  <div class="diagram-container">
    <svg viewBox="0 0 680 360" width="100%" height="360" xmlns="http://www.w3.org/2000/svg">
      <rect x="0" y="0" width="680" height="360" fill="#ffffff" stroke="#d0d7de" stroke-width="1"/>

      <!-- Base Class Person -->
      <rect x="250" y="20" width="180" height="90" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <rect x="250" y="20" width="180" height="25" fill="#f6f8fa" stroke="#1f2328" stroke-width="1"/>
      <text x="340" y="37" font-family="monospace" font-size="12" font-style="italic" font-weight="bold" fill="#0969da" text-anchor="middle">&laquo;abstract&raquo; Person</text>
      <text x="260" y="60" font-family="monospace" font-size="10" fill="#cf222e">- id : String</text>
      <text x="260" y="75" font-family="monospace" font-size="10" fill="#cf222e">- name : String</text>
      <text x="260" y="90" font-family="monospace" font-size="10" fill="#cf222e">- contact : String</text>

      <!-- Derived Patient -->
      <rect x="60" y="160" width="190" height="90" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <rect x="60" y="160" width="190" height="25" fill="#f6f8fa" stroke="#1f2328" stroke-width="1"/>
      <text x="155" y="177" font-family="monospace" font-size="12" font-weight="bold" fill="#0969da" text-anchor="middle">Patient</text>
      <text x="70" y="200" font-family="monospace" font-size="10" fill="#cf222e">- bloodGroup : String</text>
      <text x="70" y="215" font-family="monospace" font-size="10" fill="#1a7f37">+ admit() : void</text>
      <text x="70" y="230" font-family="monospace" font-size="10" fill="#1a7f37">+ discharge() : void</text>

      <!-- Derived Doctor -->
      <rect x="430" y="160" width="190" height="90" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      <rect x="430" y="160" width="190" height="25" fill="#f6f8fa" stroke="#1f2328" stroke-width="1"/>
      <text x="525" y="177" font-family="monospace" font-size="12" font-weight="bold" fill="#0969da" text-anchor="middle">Doctor</text>
      <text x="440" y="200" font-family="monospace" font-size="10" fill="#cf222e">- specialty : String</text>
      <text x="440" y="215" font-family="monospace" font-size="10" fill="#1a7f37">+ prescribe() : void</text>
      <text x="440" y="230" font-family="monospace" font-size="10" fill="#1a7f37">+ conductExam() : void</text>

      <!-- Inheritance Arrows -->
      <!-- Patient to Person -->
      <line x1="155" y1="160" x2="310" y2="110" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="310,110 300,118 316,122" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>
      
      <!-- Doctor to Person -->
      <line x1="525" y1="160" x2="370" y2="110" stroke="#1f2328" stroke-width="1.5"/>
      <polygon points="370,110 364,122 380,118" fill="#ffffff" stroke="#1f2328" stroke-width="1.5"/>

      <!-- Association Class Appointment -->
      <rect x="250" y="270" width="180" height="75" fill="#ffffff" stroke="#0969da" stroke-width="1.5"/>
      <rect x="250" y="270" width="180" height="22" fill="#f6f8fa" stroke="#0969da" stroke-width="1"/>
      <text x="340" y="286" font-family="monospace" font-size="11" font-weight="bold" fill="#0969da" text-anchor="middle">Appointment</text>
      <text x="260" y="306" font-family="monospace" font-size="9" fill="#1f2328">- appointmentTime : DateTime</text>
      <text x="260" y="322" font-family="monospace" font-size="9" fill="#1f2328">- status : StatusEnum</text>

      <!-- Association Lines between Patient and Doctor via Appointment -->
      <line x1="250" y1="205" x2="430" y2="205" stroke="#1f2328" stroke-width="1.5"/>
      <text x="260" y="198" font-family="monospace" font-size="10" fill="#1f2328">1</text>
      <text x="415" y="198" font-family="monospace" font-size="10" fill="#1f2328">0..*</text>
      <line x1="340" y1="205" x2="340" y2="270" stroke="#0969da" stroke-width="1.5" stroke-dasharray="3,3"/>
    </svg>
    <span class="diagram-caption">Figure U1-L15: Object-Oriented Class Model for Hospital Management System</span>
  </div>

  <h4 class="answer-heading">4. Concrete Advantages of OO Modeling Over Structured Modeling</h4>
  <ul>
    <li><strong>Encapsulated Patient Privacy:</strong> In structured modeling, a patient record struct is passed to multiple procedures (billing, pathology, radiology), exposing full medical histories. In OO modeling, <code>MedicalRecord</code> access is strictly guarded; billing only receives monetary values without accessing diagnostic notes.</li>
    <li><strong>Polymorphic Treatment &amp; Specialization:</strong> Introducing specialized patient workflows (e.g., <code>InPatient</code> with bed allocations vs. <code>OutPatient</code> with same-day consultation) is handled via inheritance without rewriting existing scheduling algorithms.</li>
    <li><strong>State Invariant Protection:</strong> Hospital beds cannot be double-booked; state transitions (from <code>Vacant</code> to <code>Occupied</code>) are atomic and validated inside the <code>Bed</code> class.</li>
  </ul>

  <h4 class="answer-heading">5. Comparative Architectural Summary: Hospital System Modeling</h4>
  <table class="exam-table">
    <thead>
      <tr>
        <th style="width: 25%;">Evaluation Metric</th>
        <th style="width: 37%;">Structured Approach (DFD / SA/SD)</th>
        <th style="width: 38%;">Object-Oriented Modeling (UML)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Data Security & Privacy</strong></td>
        <td>Vulnerable: Patient records pass through multiple detached functions, exposing medical records to administrative routines.</td>
        <td>Guaranteed: <code>MedicalRecord</code> access is strictly restricted behind role-based encapsulation barriers.</td>
      </tr>
      <tr>
        <td><strong>Extensibility</strong></td>
        <td>Modifying patient records to support telemedicine or insurance co-pays breaks all procedural subroutines.</td>
        <td>Extensible: Subclassing <code>Consultation</code> or <code>Bill</code> incorporates new services with zero changes to existing clinical workflows.</td>
      </tr>
      <tr>
        <td><strong>Concurrency & Invariants</strong></td>
        <td>Race conditions occur when parallel billing and admission routines update flat database files.</td>
        <td>Thread-safe encapsulation ensures atomic state changes (e.g., bed allocation, room locking).</td>
      </tr>
    </tbody>
  </table>
</div>
        """
    })

    return questions

if __name__ == "__main__":
    qs = get_unit1_questions()
    print(f"Generated {len(qs)} questions for Unit 1.")
    import re
    for q in qs:
        clean = re.sub(r'<[^>]+>', ' ', q['content'])
        words = len(clean.split())
        print(f"{q['id']}: {words} words | has_svg={'<svg' in q['content']} | has_code={'<code' in q['content']}")


# -*- coding: utf-8 -*-
"""
Enrichment data for Unit 2 questions to guarantee 400-650+ words per question.
"""

def get_unit2_enhancements():
    enhancements = {}

    # U2-L02
    enhancements["U2-L02"] = """
  <h4 class="answer-heading">5. Traceability Across the Unified Approach Workflow</h4>
  <p>In the Unified Approach, use cases provide the architectural baseline ensuring end-to-end traceability across all engineering artifacts:</p>
  <ul>
    <li><strong>Use Case Realization:</strong> Each use case is systematically realized through one or more UML Collaboration or Sequence Diagrams that allocate responsibilities to Boundary, Control, and Entity classes.</li>
    <li><strong>Test Case Derivation:</strong> Primary use case execution paths directly formulate happy-path functional test suites; alternate scenarios and exception branches formulate boundary-value and failure test vectors.</li>
    <li><strong>Verification and Validation:</strong> Design review boards inspect whether every customer requirement documented in the use case model is mapped to at least one operation in the domain class model.</li>
  </ul>
"""

    # U2-L03
    enhancements["U2-L03"] = """
  <h4 class="answer-heading">4. Advanced Statechart Concepts: Composite States &amp; History Mechanisms</h4>
  <p>In complex industrial control systems, statechart diagrams manage combinatorial state explosion using advanced structuring mechanisms:</p>
  <ul>
    <li><strong>Composite States (Hierarchical States):</strong> A state that contains nested sub-states. For example, the <code>OPERATIONAL</code> state can encapsulate nested sub-states <code>COINS_HELD</code> and <code>DISPENSING</code>. An event triggering a transition out of the composite state (such as <code>emergencyPowerOff</code>) automatically aborts all active sub-states without requiring individual transition arrows from each sub-state.</li>
    <li><strong>Orthogonal Regions (Concurrency):</strong> Models independent parallel behaviors within a single object (e.g., a ticket vending machine simultaneously managing hardware temperature telemetry while processing currency insertion).</li>
    <li><strong>History Pseudo-States (<code>H</code> / <code>H*</code>):</strong> Remembers the most recently active sub-state within a composite state before an interrupt occurred, allowing the system to resume execution exactly where it left off rather than resetting to the initial state.</li>
  </ul>
"""

    # U2-L04
    enhancements["U2-L04"] = """
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
"""

    # U2-L05
    enhancements["U2-L05"] = """
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
"""

    # U2-L06
    enhancements["U2-L06"] = """
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
"""

    # U2-L07
    enhancements["U2-L07"] = """
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
"""

    # U2-L08
    enhancements["U2-L08"] = """
  <h4 class="answer-heading">4. Architectural Rules Governing &laquo;include&raquo; vs. &laquo;extend&raquo;</h4>
  <ul>
    <li><strong>Include Semantics (Mandatory Factoring):</strong> Used when a common chunk of behavior is shared across multiple use cases (e.g., both <code>Transfer Funds</code> and <code>View Balance</code> &laquo;include&raquo; <code>Authenticate User</code>). The base use case is functionally incomplete without the included behavior.</li>
    <li><strong>Extend Semantics (Conditional Extension):</strong> Used to model optional, exceptional, or auxiliary functionality that executes only when a specific boolean condition holds at an extension point (e.g., triggering a fraud investigation if an order exceeds $10,000). The base use case is completely functional on its own without the extending use case.</li>
    <li><strong>Actor Generalization:</strong> An actor can inherit from another actor (e.g., <code>Administrator</code> inherits from <code>Customer</code>), inheriting all associated use case interactions while gaining specialized administrative capabilities.</li>
  </ul>
"""

    # U2-L09
    enhancements["U2-L09"] = """
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
"""

    # U2-L10
    enhancements["U2-L10"] = """
  <h4 class="answer-heading">4. Step-by-Step Message Trace &amp; Business Rules</h4>
  <ol>
    <li><code>1: bookRoom(dates, roomType)</code>: The Guest initiates the booking request via the web frontend.</li>
    <li><code>2: checkAndLock(dates, roomType)</code>: The controller verifies room availability in the inventory database and places a temporary 10-minute hold on the selected room.</li>
    <li><code>3: chargeCard(paymentInfo, amount)</code>: The controller requests credit card authorization from the payment gateway. If successful, payment confirmation token is returned.</li>
    <li><code>4: sendVoucher(reservationDetails)</code>: The controller triggers the email service to dispatch a confirmed booking voucher and invoice to the guest's email address.</li>
  </ol>
  <p>This layout clearly demonstrates the <strong>Controller Pattern</strong> (GRASP), where <code>ReservationController</code> acts as the central coordinator delegating tasks to domain entities and infrastructure services.</p>
"""

    # U2-L11
    enhancements["U2-L11"] = """
  <h4 class="answer-heading">5. Structural Hierarchy of Architectural Artifacts</h4>
  <p>Architectural modeling enforces a multi-tiered hierarchy of abstraction:</p>
  <ul>
    <li><strong>Subsystem Decomposition:</strong> High-level functional modules (e.g., <code>BillingSubsystem</code>, <code>InventorySubsystem</code>) organized into cohesive packages.</li>
    <li><strong>Component Packaging:</strong> Translating subsystem designs into physical software artifacts (JAR files, dynamic libraries, Docker containers) with strict interface contracts.</li>
    <li><strong>Node Allocation:</strong> Mapping software components to physical hardware topologies, specifying cloud regions, Kubernetes pods, and network protocols (gRPC, TLS, REST) to satisfy non-functional performance and disaster recovery requirements.</li>
  </ul>
"""

    # U2-L12
    enhancements["U2-L12"] = """
  <h4 class="answer-heading">4. Why Both Diagrams Are Essential in System Verification</h4>
  <p>Neither diagram is sufficient on its own during complex system engineering:</p>
  <ul>
    <li><strong>Class Diagrams</strong> define the static taxonomy, type safety constraints, and possible relationship structures across the entire application domain. However, they cannot illustrate specific runtime graph configurations, dynamic object linking, or memory aliasing bugs.</li>
    <li><strong>Object Diagrams</strong> serve as empirical "test cases" for class models. Software architects draw object diagrams to simulate complex edge cases (e.g., circular references, recursive tree structures, or orphan objects) to verify whether the proposed class model legally permits or incorrectly prevents specific runtime configurations.</li>
  </ul>
"""

    # U2-L13
    enhancements["U2-L13"] = """
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

    std::cout << "Due Day: Day " << loan.getDueDate() << "\\n";
    std::cout << "Derived Late Fee: $" << loan.calculateLateFine(currentDay) << "\\n";
    return 0;
}</code></pre>
"""

    # U2-L14
    enhancements["U2-L14"] = """
  <h4 class="answer-heading">4. Asynchronous NLP Pipelines &amp; Timeout Recovery</h4>
  <p>In production customer service platforms, chatbot interactions require disciplined timing management:</p>
  <ul>
    <li><strong>Immediate Acknowledgment:</strong> To ensure optimal user experience, the system pushes a typing indicator or acknowledgment within 50ms, preventing user abandonment.</li>
    <li><strong>Asynchronous Intent Classification:</strong> Natural language processing (tokenization, intent classification, entity extraction) runs on detached GPU worker nodes. The gateway manages asynchronous polling or websocket streams to receive results.</li>
    <li><strong>Circuit-Breaker &amp; Human Fallback:</strong> If the NLP pipeline latency exceeds the hard timeout threshold (2000ms) or confidence falls below 0.65, the gateway gracefully routes the user session to an active human customer service representative.</li>
  </ul>
"""

    # U2-L16
    enhancements["U2-L16"] = """
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
"""

    # U2-L17
    enhancements["U2-L17"] = """
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
        std::cout << "[Video Stream] Buffering 1080p H.264 video chunks.\\n";
    }
};

class InteractiveQuiz : public CourseMaterial {
public:
    void renderContent() override {
        std::cout << "[Quiz Engine] Initializing timed multi-choice assessment.\\n";
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
"""

    # U2-L18
    enhancements["U2-L18"] = """
  <h4 class="answer-heading">4. Detailed Concurrency &amp; Message Semantics</h4>
  <ul>
    <li><strong>Lifeline Activation Bars:</strong> Thin rectangles placed over a lifeline indicate that the object is actively executing code, holding a CPU thread, or waiting on synchronous nested invocations.</li>
    <li><strong>Asynchronous Message Queuing:</strong> Non-blocking arrows model producer-consumer architectures where messages are placed onto distributed message brokers (Apache Kafka, RabbitMQ) without stalling the sender.</li>
    <li><strong>Interaction Frames:</strong> Sequence diagrams structure complex logic using operator frames: <code>alt</code> (conditional alternative choices), <code>opt</code> (optional branch), <code>loop</code> (repetition), and <code>par</code> (concurrent parallel message streams).</li>
  </ul>
"""

    # U2-L19
    enhancements["U2-L19"] = """
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
"""

    # U2-L20
    enhancements["U2-L20"] = """
  <h4 class="answer-heading">5. Industrial Significance in Enterprise Cloud Deployment</h4>
  <p>In modern microservices and cloud engineering, architectural modeling is essential for:</p>
  <ul>
    <li><strong>CI/CD Build Automation:</strong> Component diagrams define build order dependencies and interface compatibility tests between independently versioned microservices.</li>
    <li><strong>Kubernetes / Infrastructure Topology:</strong> Deployment diagrams document pod allocations, ingress load balancers, multi-region database replication paths, and VPC network firewalls.</li>
    <li><strong>Capacity Planning &amp; Sizing:</strong> Modeling physical nodes allows infrastructure engineers to provision CPU cores, RAM limits, and network throughput to satisfy service level agreements (SLAs).</li>
  </ul>
"""

    return enhancements


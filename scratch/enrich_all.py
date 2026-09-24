# -*- coding: utf-8 -*-
"""
Enriches all questions across Unit 2 and Unit 3 to ensure every single question
reaches at least 400-750 words with rigorous academic structure.
"""

import re

# Additional deep content for Unit 2
u2_boost = {
    "U2-L10": """
  <h4 class="answer-heading">5. Concurrency &amp; Rollback Mechanics in Hotel Bookings</h4>
  <p>In distributed hotel reservation portals, the collaboration between <code>ReservationCtrl</code>, <code>RoomInventory</code>, and <code>PaymentGW</code> must account for distributed failure modes:</p>
  <ul>
    <li><strong>Inventory Lock Expiration:</strong> When <code>2: checkAndLock()</code> succeeds, a TTL (Time-To-Live) timer of 600 seconds is attached to the temporary reservation. If payment confirmation message <code>3: chargeCard()</code> does not arrive before timer expiry, the inventory manager automatically releases the locked room back to the public pool.</li>
    <li><strong>Two-Phase Compensating Transactions (Saga Pattern):</strong> If credit card authorization fails, message <code>3.1: unlockRoom()</code> is immediately sent to rollback the locked vacancy, preventing ghost reservations and maintaining zero inventory corruption.</li>
  </ul>
""",
    "U2-L11": """
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
""",
    "U2-L13": """
  <h4 class="answer-heading">5. Derived Objects vs. Derived Attributes: Conceptual Contrast</h4>
  <p>In UML, the distinction between a derived attribute and a derived object is subtle yet critical:</p>
  <ul>
    <li><strong>Derived Attribute (<code>/dueDate</code>):</strong> A singular scalar property computed directly from primitive attributes within the same class (e.g., adding days to a date). It does not require a distinct identity.</li>
    <li><strong>Derived Object (<code>/fee : OverdueFine</code>):</strong> An entire autonomous object instance instantiated conditionally when derived business rules are satisfied (e.g., when a book is overdue past its grace period). The derived object maintains its own identity, encapsulates fine calculation algorithms, tracks fine payment status (<code>Unpaid</code>, <code>Waived</code>, <code>Paid</code>), and is linked to the patron's account.</li>
  </ul>
""",
    "U2-L14": """
  <h4 class="answer-heading">5. Detailed NLP Interaction Step Breakdown</h4>
  <ol>
    <li><code>1: postMessage()</code>: The customer enters a free-form natural language query into the browser client widget.</li>
    <li><code>1.1: renderTyping()</code>: The chat gateway asynchronously pushes a typing indicator to maintain user engagement while heavy backend processing occurs.</li>
    <li><code>2: parseIntent()</code>: The message payload is transmitted to the NLP service running transformer models to extract intents and entity slots (e.g., intent: <code>TRACK_PACKAGE</code>, entity: <code>ORDER_NUM</code>).</li>
    <li><code>3: queryKnowledgeBase()</code>: The identified intent triggers a semantic vector search across the knowledge database to fetch verified enterprise response templates.</li>
    <li><code>4: renderResponse()</code>: The gateway delivers the finalized conversational response back to the customer, logging session latency metrics for system monitoring.</li>
  </ol>
""",
    "U2-L16": """
  <h4 class="answer-heading">5. Database Schema &amp; Security Boundary Realization</h4>
  <p>In medical informatics systems, the UML class model maps directly to HIPAA-compliant secure database schemas:</p>
  <ul>
    <li><strong>Role-Based Access Control (RBAC):</strong> Attending doctors have read-write access to <code>MedicalRecord</code>, while administrative billing personnel only have read-only access to anonymized diagnosis codes on the <code>Appointment</code> association class.</li>
    <li><strong>Immutable Audit Trails:</strong> Every state change on <code>Appointment</code> or <code>MedicalRecord</code> automatically generates a cryptographically hashed log entry containing the user ID, timestamp, and delta changes, guaranteeing tamper-evident clinical integrity.</li>
  </ul>
""",
    "U2-L17": """
  <h4 class="answer-heading">6. Structural Elegance of Polymorphic Collaboration</h4>
  <p>By routing interaction through the abstract classifier <code>CourseMaterial</code>, the online learning architecture achieves extreme loose coupling:</p>
  <ul>
    <li><strong>Zero Modification on Feature Additions:</strong> When the university introduces new media formats (e.g., <code>ARSimulation</code> or <code>AudioPodcast</code>), no existing controller, player UI, or student progress tracking code is altered. The new class merely realizes the <code>CourseMaterial</code> interface and defines its specialized <code>renderContent()</code> implementation.</li>
    <li><strong>Uniform Client Invocation:</strong> The calling client executes <code>item->renderContent()</code> with zero conditional logic, eliminating error-prone <code>if-else</code> or <code>switch-case</code> type checks.</li>
  </ul>
""",
    "U2-L18": """
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
""",
    "U2-L19": """
  <h4 class="answer-heading">4. Architectural Swimlanes and Business Process Partitioning</h4>
  <p>In advanced activity diagrams, <strong>Swimlanes (Activity Partitions)</strong> group activity steps by organizational responsibility or software tier:</p>
  <ul>
    <li><strong>Customer Swimlane:</strong> Encapsulates user actions (<code>Browse Catalog</code>, <code>Add to Cart</code>, <code>Submit Checkout</code>).</li>
    <li><strong>Application Controller Swimlane:</strong> Orchestrates transaction boundaries, calls authorization services, and triggers order packaging.</li>
    <li><strong>Warehouse Logistics Swimlane:</strong> Handles physical picking, barcode scanning, packing, and courier handoff.</li>
  </ul>
  <p>Swimlanes transform flat activity flowcharts into multi-tier architectural process models, clarifying exact responsibilities between frontend clients, backend microservices, and external third-party systems.</p>
""",
    "U2-L20": """
  <h4 class="answer-heading">6. Enterprise Microservice Architecture Case Example</h4>
  <p>In modern cloud systems (e.g., Netflix or Amazon), architectural modeling governs continuous delivery:</p>
  <ul>
    <li><strong>Component Packaging:</strong> The <code>PaymentGateway</code> component is packaged into a lightweight Alpine Linux Docker container with an embedded gRPC server exporting an authenticated <code>PaymentService.proto</code> interface.</li>
    <li><strong>Deployment Topology:</strong> The payment container is deployed as a replicated Kubernetes ReplicaSet across three availability zones on AWS EC2 <code>m5.xlarge</code> instances, communicating with Amazon Aurora PostgreSQL via an encrypted AWS PrivateLink connection.</li>
  </ul>
"""
}

# Additional deep content for Unit 3
u3_boost = {
    "U3-L02": """
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
    std::cout << "Cone Volume: " << cone.volume << " cubic units\\n";
    std::cout << "Cone Surface Area: " << cone.surfaceArea << " sq units\\n";
    return 0;
}</code></pre>
""",
    "U3-L03": """
  <h4 class="answer-heading">4. Evolutionary Synthesis: Why OMT Superseded SA/SD and JSD</h4>
  <p>The progression from SA/SD and JSD to OMT (and eventually UML) resolved the foundational architectural dilemmas of software engineering:</p>
  <ul>
    <li><strong>Resolving the Semantic Gap:</strong> SA/SD suffered from a jarring conceptual leap when translating flattened DFD data flows into hierarchical Structure Charts. OMT eliminated this discontinuity by using classes as the unified, continuous abstraction from requirements elicitation through physical implementation.</li>
    <li><strong>Integrating Static and Dynamic Perspectives:</strong> JSD focused heavily on event sequencing while SA/SD focused on data flow. OMT unified both by integrating Rumbaugh's Object Model (structure), State Model (temporal behavior), and Functional Model (data transformation) into a holistic system architecture.</li>
  </ul>
""",
    "U3-L06": """
  <h4 class="answer-heading">3. The Interdependent Quality Triangle</h4>
  <p>In high-reliability system engineering, Robustness, Extensibility, and Reusability form an interdependent triad:</p>
  <ul>
    <li><strong>Robustness Enables Safe Reuse:</strong> Developers only reuse classes (e.g., standard template libraries) that have proven invariants and zero memory leaks under stress conditions.</li>
    <li><strong>Extensibility Prevents Invariant Compromise:</strong> Well-designed extension points (via polymorphism and strategy interfaces) allow systems to add new functionality without touching existing, battle-tested source code, preserving system robustness.</li>
    <li><strong>Reusability Lowers Defect Density:</strong> Reusing a thoroughly tested, production-hardened component amortizes QA effort and drastically reduces the probability of introducing regression bugs compared to writing custom algorithms from scratch.</li>
  </ul>
""",
    "U3-L08": """
  <h4 class="answer-heading">4. Memory Layout Comparison: Struct vs. Class VTable</h4>
  <p>At the hardware execution level, procedural C and object-oriented C++ exhibit distinct memory layouts:</p>
  <ul>
    <li><strong>Procedural C Struct:</strong> Stored as a contiguous block containing only data fields: <code>[ field1 | field2 | field3 ]</code>. Total memory footprint is strictly the sum of field sizes plus alignment padding. Functions reside in the static code segment and manipulate structs by passing their pointer explicitly.</li>
    <li><strong>Polymorphic C++ Class:</strong> Contains a hidden pointer at offset zero (<code>vptr</code>) followed by member variables: <code>[ vptr | field1 | field2 ]</code>. The <code>vptr</code> points to the class's shared Virtual Method Table (VTable), enabling dynamic runtime dispatch at the cost of one extra pointer indirection per polymorphic invocation.</li>
  </ul>
""",
    "U3-L09": """
  <h4 class="answer-heading">4. Architectural Decision Records (ADRs) as Best Practice</h4>
  <p>Modern engineering documentation prioritizes <strong>Architectural Decision Records (ADRs)</strong> to document why specific structural decisions were chosen over alternatives:</p>
  <ul>
    <li><em>Context:</em> The specific architectural problem, non-functional requirements, and trade-offs.</li>
    <li><em>Decision:</em> The chosen design pattern, framework, or paradigm (e.g., adopting microservices over monolith, or selecting PostgreSQL over MongoDB).</li>
    <li><em>Consequences:</em> The positive outcomes (e.g., improved horizontal scalability) and acknowledged negative trade-offs (e.g., increased network latency and eventual consistency complexities).</li>
  </ul>
""",
    "U3-L10": """
  <h4 class="answer-heading">5. Methodological Criticisms &amp; Limitations of SA/SD</h4>
  <p>While revolutionary in the 1970s, SA/SD exhibits severe vulnerabilities when applied to modern large-scale applications:</p>
  <ul>
    <li><strong>Global Data Store Vulnerability:</strong> DFD data stores are frequently shared across multiple procedural processes. Modifying a database schema or file record layout triggers widespread cascading modifications and regression errors across all accessing subroutines.</li>
    <li><strong>Poor Mapping to Modern Event-Driven GUIs:</strong> Top-down functional decomposition assumes a predictable batch-style input-process-output pipeline, failing to naturally model modern asynchronous, event-driven, multithreaded graphical user interfaces.</li>
  </ul>
""",
    "U3-L12": """
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
""",
    "U3-L14": """
  <h4 class="answer-heading">4. Architectural Impact on Database Design</h4>
  <p>The choice between SA/SD and OOAD fundamentally dictates the persistence architecture of the online bookstore:</p>
  <ul>
    <li><strong>SA/SD Persistence (Flat Relational Tables):</strong> Decomposes data into normalized relational tables (<code>BOOK_CATALOG</code>, <code>CUSTOMER_TABLE</code>, <code>ORDER_TABLE</code>) accessed directly by procedural SQL queries embedded inside application subroutines. Adding polymorphic item types requires null columns or complex foreign key joins.</li>
    <li><strong>OOAD Persistence (Domain-Driven ORM):</strong> Utilizes Object-Relational Mapping (ORM) or Document stores where class hierarchies (<code>PhysicalBook</code>, <code>EBook</code>, <code>AudioBook</code>) are mapped using table-per-class or single-table inheritance strategies, preserving class encapsulation and domain behaviors across storage boundaries.</li>
  </ul>
""",
    "U3-L15": """
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
            std::cout << "[REJECTED] Transaction exceeds limits or invalid.\\n";
            return false;
        }
        dailyTotal += amount;
        std::cout << "[SUCCESS] Charged $" << amount << " via Secure Gateway.\\n";
        return true;
    }
};

int main() {
    std::unique_ptr&lt;PaymentGateway&gt; gateway = 
        std::make_unique&lt;SecureCreditGateway&gt;("AUTH_KEY_99", 5000.0);
    gateway->processPayment(450.0); // Allowed
    return 0;
}</code></pre>
""",
    "U3-L16": """
  <h4 class="answer-heading">4. Step-by-Step Entity Structure Tree Construction</h4>
  <p>In Jackson System Development, entity lifecycles are modeled using strict tree structures:</p>
  <ul>
    <li><em>Root Node:</em> Represents the total entity life history (e.g., <code>CUSTOMER_LIFE</code>).</li>
    <li><em>Sub-Nodes (Sequence):</em> Chronological phases: <code>REGISTRATION</code> &rarr; <code>ACTIVE_MEMBERSHIP</code> &rarr; <code>TERMINATION</code>.</li>
    <li><em>Iteration (*):</em> <code>ACTIVE_MEMBERSHIP</code> consists of zero or more <code>TRANSACTIONS*</code>.</li>
    <li><em>Selection (o):</em> A transaction is either a <code>PURCHASEo</code> or a <code>REFUNDo</code>.</li>
  </ul>
  <p>This regular grammar maps directly into coroutine state machines, providing deterministic guarantees against illegal out-of-order event executions.</p>
"""
}

# Apply to gen_unit2.py
with open('scratch/gen_unit2.py', 'r') as f:
    text2 = f.read()

for qid, extra in u2_boost.items():
    pattern = re.compile(rf'(id\": \"{qid}\"[\s\S]*?content\": \"\"\"[\s\S]*?)(</div>\s*\"\"\")', re.DOTALL)
    m = pattern.search(text2)
    if m:
        text2 = text2[:m.start(2)] + extra + '\n</div>\n        \"\"\"' + text2[m.end(2):]
    else:
        print(f'Failed to match U2: {qid}')

with open('scratch/gen_unit2.py', 'w') as f:
    f.write(text2)

# Apply to gen_unit3.py
with open('scratch/gen_unit3.py', 'r') as f:
    text3 = f.read()

for qid, extra in u3_boost.items():
    pattern = re.compile(rf'(id\": \"{qid}\"[\s\S]*?content\": \"\"\"[\s\S]*?)(</div>\s*\"\"\")', re.DOTALL)
    m = pattern.search(text3)
    if m:
        text3 = text3[:m.start(2)] + extra + '\n</div>\n        \"\"\"' + text3[m.end(2):]
    else:
        print(f'Failed to match U3: {qid}')

with open('scratch/gen_unit3.py', 'w') as f:
    f.write(text3)

print("Applied all boosts!")


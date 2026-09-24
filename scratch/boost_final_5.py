# -*- coding: utf-8 -*-
import re

extra_u2_l17 = """
  <h4 class="answer-heading">7. Sequence vs. Collaboration View of Polymorphism</h4>
  <p>While a Sequence Diagram shows polymorphism along vertical time lifelines with execution activation bars, the Collaboration Diagram uniquely highlights <strong>structural link reuse</strong>. The caller interacts across a single association link regardless of whether the runtime instance is a video stream, interactive quiz, or PDF document. This visually demonstrates the <strong>Liskov Substitution Principle (LSP)</strong>: objects of a superclass shall be replaceable with objects of its subclasses without breaking application logic.</p>
"""

extra_u2_l19 = """
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
"""

extra_u2_l20 = """
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
"""

extra_u3_l15 = """
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
"""

extra_u3_l16 = """
  <h4 class="answer-heading">5. Walkthrough of an ATM System under SA/SD vs. JSD</h4>
  <ul>
    <li><strong>Under SA/SD (Functional Pipeline):</strong> The ATM is modeled as a set of functional transforms: <code>Validate Card</code> &rarr; <code>Verify PIN</code> &rarr; <code>Check Balance</code> &rarr; <code>Dispense Cash</code> &rarr; <code>Print Receipt</code>. Passive account records flow between these processes. If a new transaction type (e.g., mobile top-up) is added, the central structure chart and DFD bubbles must be redesigned.</li>
    <li><strong>Under JSD (Entity Life History):</strong> The ATM is modeled around real-world entities: <code>CUSTOMER</code> and <code>ATM_TERMINAL</code>. The lifecycle of <code>CUSTOMER</code> is modeled as an Entity Structure Diagram: <code>INSERT_CARD</code> &rarr; <code>ENTER_PIN</code> &rarr; <code>TRANSACTION*</code> &rarr; <code>EJECT_CARD</code>. Each transaction is a selection between <code>WITHDRAWALo</code>, <code>DEPOSSTo</code>, or <code>BALANCE_INQUIRYo</code>. JSD preserves the natural chronological order of customer behavior, making it immune to functional requirement mutations.</li>
  </ul>
"""

# Update gen_unit2.py
with open('scratch/gen_unit2.py', 'r') as f:
    t2 = f.read()

for qid, extra in [("U2-L17", extra_u2_l17), ("U2-L19", extra_u2_l19), ("U2-L20", extra_u2_l20)]:
    pattern = re.compile(rf'(id\": \"{qid}\"[\s\S]*?content\": \"\"\"[\s\S]*?)(</div>\s*\"\"\")', re.DOTALL)
    m = pattern.search(t2)
    if m:
        t2 = t2[:m.start(2)] + extra + '\n</div>\n        \"\"\"' + t2[m.end(2):]

with open('scratch/gen_unit2.py', 'w') as f:
    f.write(t2)

# Update gen_unit3.py
with open('scratch/gen_unit3.py', 'r') as f:
    t3 = f.read()

for qid, extra in [("U3-L15", extra_u3_l15), ("U3-L16", extra_u3_l16)]:
    pattern = re.compile(rf'(id\": \"{qid}\"[\s\S]*?content\": \"\"\"[\s\S]*?)(</div>\s*\"\"\")', re.DOTALL)
    m = pattern.search(t3)
    if m:
        t3 = t3[:m.start(2)] + extra + '\n</div>\n        \"\"\"' + t3[m.end(2):]

with open('scratch/gen_unit3.py', 'w') as f:
    f.write(t3)

print("Boosted final 5 questions!")


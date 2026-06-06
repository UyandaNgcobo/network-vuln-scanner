# Automated Network Vulnerability Scanner

A concurrent, low-overhead network vulnerability scanner built in Python. This tool maps local networks, identifies open ports using custom socket implementations, and cross-references active service banners against known vulnerability datasets.

## 🏗 System Architecture & SOLID Principles
This project was architected with clean code principles to ensure modularity:
* **Single Responsibility:** Network discovery, port probing, and reporting are handled by isolated modules.
* **Liskov Substitution:** The core execution engine can hot-swap scanning strategies (e.g., standard TCP Connect vs. half-open SYN scans) without modifying the orchestrator.
* **Concurrency:** Utilizes Python's native concurrency models to scan hundreds of ports simultaneously, minimizing network bottlenecks.

## 🚀 Development Phases
- [ ] Phase 1: ICMP Host Discovery
- [ ] Phase 2: Concurrent TCP Port Scanning
- [ ] Phase 3: Service Fingerprinting & Banner Grabbing
- [ ] Phase 4: Vulnerability Database Matching
- [ ] Phase 5: Automated Audit Reporting

## 🛠 Tech Stack
* **Language:** Python
* **Key Libraries:** `socket`, `asyncio` (or `concurrent.futures`)
# Defense Surveillance System (DSS)

The Defense Surveillance System (DSS) is a modular, real-time video surveillance platform inspired by defense, perimeter security, and critical infrastructure monitoring systems.

The project is designed to demonstrate how real-world surveillance software is architected, integrated, and performance-evaluated under operational constraints.

---

## Project Goals

- Build a **real-time surveillance pipeline** with measurable performance
- Demonstrate **defense-style system decomposition**
- Integrate AI components in a **controlled, auditable manner**
- Emphasize **correctness, stability, and observability** over UI polish

---

## System Architecture

Video Source
↓
Video Ingestion Module
↓
Object Detection Engine
↓
Object Tracking Engine (In Progress)
↓
Threat Evaluation Engine (Planned)
↓
Event Logging & Operator View (Planned)

Each module is isolated, testable, and designed to fail safely without collapsing the system.

---

## Current Capabilities

### Phase 1 — Video Ingestion

- File-based video ingestion
- Frame-by-frame processing
- Average FPS measurement
- Graceful end-of-stream handling
- Clean resource management

### Phase 2 — Object Detection

- Per-frame YOLOv8 object detection
- CPU-based inference
- Inference latency measurement (ms)
- Real-time bounding box visualization
- Performance degradation analysis

### Phase 3 — Object Tracking (DeepSORT)

- Persistent object IDs across frames
- Stateful multi-object tracking
- Robust handling of brief occlusions
- Separation of detection and tracking logic
- Real-time visualization of tracked identities

---

## Performance Observations

- Baseline ingestion FPS: ~30 FPS
- Detection-only FPS (CPU): ~7–8 FPS
- Detection + Tracking FPS (CPU): slightly lower, expected
- Inference latency measured per frame

These metrics reflect real-world trade-offs between accuracy and throughput in surveillance systems.

---

## Tech Stack

- **Language:** Python
- **Computer Vision:** OpenCV
- **AI Model:** YOLOv8 (Ultralytics)
- **Backend (planned):** FastAPI
- **Storage (planned):** SQLite
- **Platform:** Windows 10
- **Version Control:** Git (branch-based development)

Model weights are treated as external dependencies and are not committed to the repository.

---

## Development Discipline

- Phase-based development
- Performance baselines preserved
- Feature isolation via Git branches
- No binary artifacts committed
- Reproducible runtime behavior

---

## Roadmap

- Phase 4: Threat rule engine (zone intrusion, loitering)
- Phase 5: Event logging & audit trail
- Phase 6: Operator dashboard & system controls

---

## Disclaimer

This project is for educational and demonstration purposes only.  
It does not represent a deployable military or defense system.

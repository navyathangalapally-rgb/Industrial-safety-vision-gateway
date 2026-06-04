# Smart Industrial Safety Gateway & Edge AI Vision Hub 🚀

An intelligent, multi-threaded cyber-physical safety system that fuses real-time Edge AI Computer Vision with an ESP32 microcontroller using FreeRTOS concurrency. 

The system utilizes advanced eye-state classification analytics to monitor operator fatigue in high-risk environments, dynamically driving localized physical and vocal escalation indicators while ensuring full fault-tolerant hardware emergency overrides.

---

## ⚡ Core System Architecture

The computation load is distributed across a decoupled architecture over a private local network to optimize processing efficiency and guarantee real-time safety response:

1. **Edge AI Vision Hub (Python / OpenCV):** Runs frame-by-frame facial and ocular classification models on an isolated core while hosting a localized HTTP REST API Gateway to expose the safety state.
2. **Industrial Control Unit (ESP32 / FreeRTOS):** A multi-threaded embedded node that concurrently queries the web gateway via a Wi-Fi bridge, updates warning indicators (LEDs/Buzzers), and monitors hardware safety interrupts.

   

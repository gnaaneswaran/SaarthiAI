# SaarthiAI – Intelligent Rural Citizen Support Agent

![SaarthiAI Logo](assets/logo.png)

SaarthiAI is an AI-powered, multilingual, voice-enabled virtual assistant that helps rural citizens access timely, reliable, and personalized information across domains such as government schemes, agriculture, healthcare, education, disaster alerts, and legal aid.

## Problem Statement

Millions of people in rural India face barriers to accessing public services due to language limitations, low digital literacy, lack of awareness, and poor connectivity. Traditional solutions like CSCs, mobile apps, and helplines fall short due to complexity, inaccessibility, or lack of personalization.

## Solution Overview

SaarthiAI bridges the last-mile information gap through:

- Voice-first and multilingual interfaces (Tamil, Hindi, Bengali, etc.)
- LLM-powered contextual responses using user profile and location
- Access via low-bandwidth channels: WhatsApp, IVR, and lightweight mobile apps
- Hyperlocal awareness: Nearby services, localized schemes, weather alerts
- Unified support across multiple public service domains

## Key Features

1. Personalized Assistance Based on User Profile  
   Responds differently to farmers, students, or elderly users based on region and needs.

2. Multilingual, Voice-Enabled Interface  
   Available in regional languages with speech-to-text and TTS support for illiterate users.

3. Access to Multiple Public Services  
   One-stop assistant for schemes, healthcare, education, farming, legal aid, and more.

4. Low-Bandwidth Channels  
   Works on WhatsApp, IVR, and basic smartphones with limited internet.

5. Hyperlocal, Real-Time Information  
   Uses geolocation and public APIs to provide local scheme eligibility, alerts, and directions.

## Tech Stack

Layer | Technology
------|-----------
NLP/AI | Vertex AI (Gemini), LangChain, Dialogflow CX
Backend | Firebase (Firestore, Auth), Cloud Functions
Interfaces | WhatsApp API, IVR (Twilio), Android Lite App
Voice | Google STT and TTS APIs
Location | Google Maps, Geolocation APIs
Data | Government and Public APIs for schemes, weather, agriculture
Hosting | Firebase, Google Cloud Platform (GCP)

## Folder Structure


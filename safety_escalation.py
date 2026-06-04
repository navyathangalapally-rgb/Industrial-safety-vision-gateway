import time
import pyttsx3
import winsound
import edge_vision_hub.web_gateway as gateway

speaker = pyttsx3.init()
speaker.setProperty('rate', 150)

last_voice_alert_time = 0
VOICE_REPEAT_INTERVAL = 3.0

def process_safety_tier(elapsed, active_worker, current_time):
    global last_voice_alert_time
    
    # Tier 3: Critical E-Stop
    if elapsed >= 5.0:
        gateway.current_active_tier = "TIER_2"
        status_text = "TIER 3: CRITICAL! EMERGENCY STOP COMMENCING"
        if current_time - last_voice_alert_time > VOICE_REPEAT_INTERVAL:
            speaker.say("Attention! Critical mood!")
            speaker.runAndWait()
            winsound.Beep(2000, 400)
            last_voice_alert_time = current_time
        return status_text, (0, 0, 255)

    # Tier 2: Floor Manager Warning
    elif elapsed >= 3.5:
        gateway.current_active_tier = "TIER_2"
        status_text = "TIER 2: WARNING! ALERTING FLOOR MANAGER"
        if current_time - last_voice_alert_time > VOICE_REPEAT_INTERVAL:
            speaker.say("Warning! Operator unresponsive!")
            speaker.runAndWait()
            last_voice_alert_time = current_time
        return status_text, (0, 140, 255)

    # Tier 1: Operator Drowsiness Alert
    elif elapsed >= 1.5:
        gateway.current_active_tier = "TIER_1"
        status_text = f"TIER 1: ATTENTION! WAKE UP {active_worker.upper()}!"
        if current_time - last_voice_alert_time > VOICE_REPEAT_INTERVAL:
            speaker.say("Navya, please wake up!")
            speaker.runAndWait()
            last_voice_alert_time = current_time
        return status_text, (0, 255, 255)
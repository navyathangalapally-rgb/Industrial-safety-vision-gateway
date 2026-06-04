#ifndef SAFETY_TIERS_H
#define SAFETY_TIERS_H

#include "hardware_config.h"

extern volatile int current_safety_tier;
extern volatile float current_temperature;

inline void handle_safety_execution() {
    // 1. Critical Hardware Overheat Switch Override
    if (current_temperature > 50.0) {
        printf("[OVERRIDE] CRITICAL HARDWARE EMERGENCY DETECTED!\n");
        gpio_set_level(LED_GREEN, 0); gpio_set_level(LED_YELLOW, 0); gpio_set_level(LED_RED, 1);
        gpio_set_level(BUZZER, 1); vTaskDelay(pdMS_TO_TICKS(100));
        gpio_set_level(BUZZER, 0); vTaskDelay(pdMS_TO_TICKS(100));
        return;
    }

    // 2. Standard Telemetry Operations
    switch(current_safety_tier) {
        case 0: // Normal Operation
            gpio_set_level(LED_GREEN, 1); gpio_set_level(LED_YELLOW, 0); gpio_set_level(LED_RED, 0); gpio_set_level(BUZZER, 0);
            vTaskDelay(pdMS_TO_TICKS(100)); break;
            
        case 1: // Yellow Warning Flash
            gpio_set_level(LED_GREEN, 0); gpio_set_level(LED_RED, 0); gpio_set_level(BUZZER, 0);
            gpio_set_level(LED_YELLOW, 1); vTaskDelay(pdMS_TO_TICKS(200));
            gpio_set_level(LED_YELLOW, 0); vTaskDelay(pdMS_TO_TICKS(200)); break;
            
        case 2: // Red Alarm Lockout
            gpio_set_level(LED_GREEN, 0); gpio_set_level(LED_YELLOW, 0); gpio_set_level(LED_RED, 1);
            gpio_set_level(BUZZER, 1); vTaskDelay(pdMS_TO_TICKS(150));
            gpio_set_level(BUZZER, 0); vTaskDelay(pdMS_TO_TICKS(150)); break;
    }
}

#endif
#ifndef HARDWARE_CONFIG_H
#define HARDWARE_CONFIG_H

#include <driver/gpio.h>

#define LED_GREEN     ((gpio_num_t)12)
#define LED_YELLOW    ((gpio_num_t)14)
#define LED_RED       ((gpio_num_t)27)
#define BUZZER        ((gpio_num_t)26)
#define SWITCH_PIN    ((gpio_num_t)5)

inline void init_hardware_pins() {
    gpio_reset_pin(LED_GREEN);  gpio_set_direction(LED_GREEN, GPIO_MODE_OUTPUT);
    gpio_reset_pin(LED_YELLOW); gpio_set_direction(LED_YELLOW, GPIO_MODE_OUTPUT);
    gpio_reset_pin(LED_RED);    gpio_set_direction(LED_RED, GPIO_MODE_OUTPUT);
    gpio_reset_pin(BUZZER);     gpio_set_direction(BUZZER, GPIO_MODE_OUTPUT);
    
    gpio_reset_pin(SWITCH_PIN);
    gpio_set_direction(SWITCH_PIN, GPIO_MODE_INPUT);
    gpio_set_pull_mode(SWITCH_PIN, GPIO_PULLUP_ONLY);
}

#endif
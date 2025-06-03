CREATE DATABASE IF NOT EXISTS wifi_repeater_helper;
USE wifi_repeater_helper;

CREATE TABLE IF NOT EXISTS repeater_setups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(255),
    channel INT,
    signal_strength INT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- SPDX-FileCopyrightText: 2025 Thomas Vincent
-- SPDX-License-Identifier: MIT
-- MySQL initialization script for WordPress Enterprise testing
-- This script sets up the test database with proper permissions

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS wordpress_test CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Grant privileges to test user
GRANT ALL PRIVILEGES ON wordpress_test.* TO 'wp_test_user'@'%';
FLUSH PRIVILEGES;

-- Create additional test database for multi-site testing
CREATE DATABASE IF NOT EXISTS wordpress_test_multisite CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
GRANT ALL PRIVILEGES ON wordpress_test_multisite.* TO 'wp_test_user'@'%';
FLUSH PRIVILEGES;

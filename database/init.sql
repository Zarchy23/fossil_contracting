-- PostgreSQL Database Initialization Script for Fossil Contracting
-- Run this script after creating the database

-- Create database (if not already created)
-- CREATE DATABASE fossil_db;
-- CREATE USER fossil_user WITH PASSWORD 'Fossil@2025Secure!';
-- ALTER ROLE fossil_user SET client_encoding TO 'utf8';
-- ALTER ROLE fossil_user SET default_transaction_isolation TO 'read committed';
-- ALTER ROLE fossil_user SET timezone TO 'UTC';
-- GRANT ALL PRIVILEGES ON DATABASE fossil_db TO fossil_user;

-- Sample data insertion (after Django migrations)
-- This script can be run after Django creates the tables

INSERT INTO api_companystat (label, value, icon, suffix, "order") VALUES
('Years Experience', '25', '🏆', '+', 1),
('Projects Completed', '500', '📊', '+', 2),
('ZBCA & CIFOZ', 'Category A', '⭐', '', 3),
('Safety Commitment', '100%', '🛡️', '', 4)
ON CONFLICT DO NOTHING;

INSERT INTO api_project (name, location, value_usd, completion_percentage, client, description, status, is_featured, start_date, created_at) VALUES
('Trabablas Interchange', 'Harare, Zimbabwe', 88.00, 85, 'Ministry of Transport', 'Construction of 15 bridges, Harare Drive Missing Link, Amalinda Road', 'ONGOING', true, '2023-01-01', NOW()),
('Harare City Bypass', 'Harare, Zimbabwe', 125.00, 72, 'RDC', 'Complete road rehabilitation including drainage and surfacing', 'ONGOING', true, '2022-06-15', NOW()),
('Dams Construction Program', 'Matabeleland Region', 215.00, 45, 'Ministry of Water Resources', 'Multiple dam construction and rehabilitation projects', 'ONGOING', true, '2023-03-01', NOW()),
('Chrome Mining Operations', 'Serpentine District', 45.00, 90, 'Private Mining Company', 'Opencast chrome mining with full rehabilitation', 'COMPLETED', false, '2021-01-01', NOW()),
('Industrial Park Development', 'Chitungwiza', 78.50, 60, 'Industrial Development Corp', 'Civil works and infrastructure for 50-hectare industrial park', 'ONGOING', false, '2023-02-01', NOW())
ON CONFLICT DO NOTHING;

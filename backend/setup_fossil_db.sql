-- PostgreSQL Setup Script for Fossil Contracting
-- Run this with: psql -U postgres -f setup_fossil_db.sql

-- Create fossil_user role if it doesn't exist
DO
$do$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'fossil_user') THEN
    CREATE ROLE fossil_user WITH LOGIN PASSWORD 'fossil_password';
    ALTER ROLE fossil_user CREATEDB;
  END IF;
END
$do$;

-- Create fossil_contracting database
CREATE DATABASE fossil_contracting OWNER fossil_user;

-- Grant all privileges on fossil_contracting to fossil_user
GRANT ALL PRIVILEGES ON DATABASE fossil_contracting TO fossil_user;

-- Show setup confirmation
\l
\du

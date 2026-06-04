# Hobby Con Architecture

## Current Architecture

Vendor
↓
hobby con Website
↓
API Gateway
↓
CreateVendorBooking Lambda
↓
DynamoDB (VendorBookings)

Organizer Export
↓
API Gateway
↓
ExportVendorBookings Lambda
↓
DynamoDB (VendorBookings)
↓
CSV Download

## AWS Services Used

* AWS Lambda
* Amazon API Gateway
* Amazon DynamoDB

## Purpose

The application provides a serverless platform for hobby convention organizers to collect vendor applications and export vendor data.

## Current Features

* Multi-step vendor application workflow
* Serverless booking processing
* DynamoDB data storage
* Protected CSV export

## Planned Features

* Stripe payment processing
* Email notifications
* Multiple convention support
* Vendor table assignment
* Organizer authentication

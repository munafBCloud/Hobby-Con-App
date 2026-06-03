# Hobby Convention Vendor Booking Platform

## Overview

 a serverless web application designed to help hobby convention organizers collect vendor applications and manage vendor booking data.

The platform allows vendors to:

* Select a table package
* Submit business information
* Reserve vendor space
* Receive booking confirmation

Organizer data is stored in AWS and can be exported as a CSV file for event planning and vendor management.

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### AWS Services

* AWS Lambda
* Amazon API Gateway
* Amazon DynamoDB

---

## Current Features

### Vendor Booking Workflow

1. Select table package
2. Enter vendor information
3. Review booking details
4. Submit application

### Serverless Backend

Bookings are processed through:

API Gateway → Lambda → DynamoDB

### Booking Export

Organizers can export vendor data as a CSV file through a protected export endpoint.

---

## Architecture

Vendor Website
↓
API Gateway
↓
CreateVendorBooking Lambda
↓
DynamoDB

CSV Export
↓
API Gateway
↓
ExportVendorBookings Lambda
↓
DynamoDB

---

## Future Enhancements

* Stripe payment processing
* Email confirmations
* Multiple event support
* Vendor approval workflow
* Organizer authentication
* Table assignment management

---

## Project Goal

This project was built as a hope for a solution for local vendors to automate and streamline event activites.

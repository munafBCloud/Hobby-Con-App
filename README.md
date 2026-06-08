# Hobby Convention Vendor Booking Platform

## Overview

A serverless web application designed to help hobby convention organizers collect vendor applications and manage vendor booking data.

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
* Docker
* Nginx

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
Docker Container (Nginx)
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

## Docker Deployment

### Overview

The Connect & Collect frontend was containerized using Docker and Nginx to create a portable deployment package.

This allows the application to be deployed consistently across:

* Ubuntu Linux
* Windows (via Docker Desktop)
* Virtual Machines
* AWS EC2
* AWS ECS

### Dockerfile

```dockerfile
FROM nginx:latest

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
```

### Build Process

Build the Docker image:

```bash
docker build -t bookingapp-image .
```

Run the container:

```bash
docker run -d -p 8080:80 --name bookingapp-container bookingapp-image
```

Verify the container is running:

```bash
docker ps
```

### Container Architecture

Connect & Collect Frontend
↓
Docker Image (bookingapp-image)
↓
Docker Container (bookingapp-container)
↓
Nginx Web Server
↓
Browser

### Skills Demonstrated

* Docker image creation
* Docker container deployment
* Nginx web hosting
* Linux administration
* Container networking
* Port mapping
* Frontend containerization
* AWS serverless integration

### Lessons Learned

* Built a custom Docker image from a Dockerfile
* Packaged a web application into a reusable container
* Deployed and tested containers on Ubuntu Linux
* Accessed containerized services from a Windows host machine
* Integrated a Dockerized frontend with a serverless AWS backend

---

## Future Enhancements

* Stripe payment processing
* Email confirmations
* Multiple event support
* Vendor approval workflow
* Organizer authentication
* Table assignment management
* Docker deployment to AWS ECS
* CI/CD pipeline integration

---

## Project Goal

This project was built as a proof-of-concept solution for local convention organizers to automate vendor registration, streamline booking management, and reduce manual administrative work.

The project also serves as a hands-on cloud engineering lab demonstrating serverless application development, AWS services integration, Docker containerization, and modern deployment practices.


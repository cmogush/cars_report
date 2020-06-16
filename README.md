# cars_report
Automatically Generate a PDF and send it by Email

Scenario:
	You work for a company that sells second hand cars. Management wants to get a summary of the amounts of vehicles that have been sold at the end of every month. The company already has a web service which serves sales data at the end of every month but management wants an email to be sent out with an attached PDF so that data is more easily readable.

Overview:
Write a script that summarizes and processes sales data into different categories
Generate a PDF using Python
Automatically send a PDF by email

emails.py  # send emails
reports.py  # generate PDF files
cars.py  # uses reports and emails to create a report and then send it by email

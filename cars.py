#!/usr/bin/env python3  # shebang

import email.message  # used for constructing emails
import mimetypes  # used for attachments
import os.path  # used for os directory management
import smtplib  # simple mail transfer protocol lib, used for sending emails

def generate(sender, recipient, subject, body, attachment_path):  # generate the email
  """Creates an email with an attachment."""
  # Basic Email formatting
  message = email.message.EmailMessage()  # create message object
  message["From"] = sender  # set From to sender
  message["To"] = recipient  # set To to recipient
  message["Subject"] = subject  # set Subject to subject
  message.set_content(body)  # set the message body to body

  # Process the attachment and add it to the email
  attachment_filename = os.path.basename(attachment_path)  # set attachment file
  mime_type, _ = mimetypes.guess_type(attachment_path)  # automatically guess the mimetype
  mime_type, mime_subtype = mime_type.split('/', 1)  # split and set the mimetype / subtype

  with open(attachment_path, 'rb') as ap:  # open the attachment
    message.add_attachment(ap.read(),  # read in the attachment
                          maintype=mime_type,   # set the mimetype
                          subtype=mime_subtype,   # set the mime subtype
                          filename=attachment_filename)  # give the attachment filename

  return message  # returns the finished message

def send(message):  # send the message
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')   # create the smtp object (assumes server configured)
  mail_server.send_message(message)  # send the message
  mail_server.quit()  # close the connection
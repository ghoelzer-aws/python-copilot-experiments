# Create program to read email from Gmail account and perform a sentiment analysis on the email.
import imaplib
import email
import email.message
import email.utils
import re
import datetime
import sys
import os
#    import pandas as pd
#    import numpy as np
#    import matplotlib.pyplot as plt
#    from matplotlib.backends.backend_pdf import PdfPages
from email.parser import Parser
from email.header import decode_header
from email.utils import parsedate_tz, mktime_tz, parsedate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.encoders import encode_base64
from email.utils import make_msgid
from email.utils import formatdate
from email.utils import formataddr
from email.utils import getaddresses
from email.utils import parseaddr


def main():

    # Create a connection to the Gmail server
    print("\n*** Starting Email Sentiment Analyzer *** \n")
    print("\n* Connecting to Gmail * \n")

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('greg.hoelzer@gmail.com', 'ppyaqlzrpmpmyiez')
    mail.select('inbox')
    result, data = mail.uid('search', None, "ALL")
    inbox_item_list = data[0].split()
    latest_email_uid = inbox_item_list[-1]
    result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_string(raw_email.decode('utf-8'))
    email_subject = email_message['subject']
    email_from = email_message['from']
    email_date = email_message['date']
#    email_body = get_body(email_message)
    email_body_plain = email_message.get_payload()

    # Define the date format
    date_format = '%a, %d %b %Y %H:%M:%S %z'
    date_format_2 = '%d/%b/%Y'

    # Parse the email date
    email_date_parsed = datetime.datetime.strptime(email_date, date_format)
    email_date_parsed = email_date_parsed.strftime(date_format_2)

    # Print parsed email subject and date
    print('Email subject: ' + email_subject)
    print('Email date: ' + email_date_parsed)


    # Evaluate the sentiment of the email    

    # Create a dataframe to store the data
    
    # Connect to AWS S3

# =============================================================================
if __name__ == "__main__":
  main()
 




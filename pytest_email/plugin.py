import pytest
import time
import os
import smtplib
import math
import datetime
import platform

from _pytest.runner import TestReport
from _pytest.terminal import TerminalReporter
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def pytest_addoption(parser):
    group = parser.getgroup('email')
    group.addoption(
        '--email_uname',
        action='store',
        dest='email_uname',
        default=None,
        help='Email id or username'
    )
    group.addoption(
        '--email_pwd',
        action='store',
        dest='email_pwd',
        default=None,
        help='Email password'
    )
    group.addoption(
        '--email_to',
        action='store',
        dest='email_to',
        default=None,
        help='Email recipients'
    )

    group.addoption(
        '--email_send',
        action='store',
        dest='email_send',
        default="True",
        help='Sends email when --email_send is True'
    )

    group.addoption(
        '--email_subject',
        action='store',
        dest='email_subject',
        default="Pytes Execution Result",
        help='Subject of email'
    )

    group.addoption(
        '--email_org',
        action='store',
        dest='email_org',
        default="Pytest Email",
        help='Your organization name'
    )

    group.addoption(
        '--email_smtp',
        action='store',
        dest='email_smtp',
        default="smtp.gmail.com:587",
        help='Email server smtp'
    )

execution_date = "Today"

def pytest_sessionstart(session):
    global execution_date
    execution_date = datetime.datetime.now().strftime("%b %d %Y, %H:%M")

@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    duration = time.time() - terminalreporter._sessionstarttime
    yield

    passed_tests = len(terminalreporter.stats.get('passed', ""))
    failed_tests = len(terminalreporter.stats.get('failed', ""))
    skipped_tests = len(terminalreporter.stats.get('skipped', ""))
    error_tests = len(terminalreporter.stats.get('error', ""))
    xfailed_tests = len(terminalreporter.stats.get('xfailed', ""))
    xpassed_tests = len(terminalreporter.stats.get('xpassed', ""))

    total_tests = passed_tests + failed_tests + skipped_tests + error_tests + xfailed_tests + xpassed_tests

    if config.option.email_send == "True":

        send_email(str(config.option.email_subject),str(config.option.email_smtp),
        str(config.option.email_uname),str(config.option.email_pwd),
        str(config.option.email_to),str(total_tests),
        str(passed_tests),str(failed_tests), str(skipped_tests),str(error_tests),
        str(xpassed_tests), str(xfailed_tests), str(round(passed_tests*100.0/total_tests,2)),
        str(execution_date),str(round(duration,2)), str(config.option.email_org))

def send_email(subject, smtp, from_user, pwd, to,
 total, passed, failed, skipped, error, xpassed, xfailed,
  percentage, exe_date, elapsed_time, company_name):

    server = smtplib.SMTP(smtp)

    msg = MIMEMultipart()
    msg['Subject'] = subject

    msg['From'] = from_user
    msg['To'] = to
    to_addrs = [to]
    msg.add_header('Content-Type', 'text/html')

    email_content = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <title>Automation Status</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0 " />
        <style>
            .rf-box {
                max-width: 60%%;
                margin: auto;
                padding: 30px;
                border: 3px solid #eee;
                box-shadow: 0 0 10px rgba(0, 0, 0, .15);
                font-size: 16px;
                line-height: 28px;
                font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
                color: #555;
            }
            
            .rf-box table {
                width: 100%%;
                line-height: inherit;
                text-align: left;
            }
            
            .rf-box table td {
                padding: 5px;
                vertical-align: top;
                width: 50%%;
                text-align: center;
            }
            
            .rf-box table tr.heading td {
                background: #eee;
                border-bottom: 1px solid #ddd;
                font-weight: bold;
                text-align: left;
            }
            
            .rf-box table tr.item td {
                border-bottom: 1px solid #eee;
            }
        </style>
    </head>
    <body>
        <div class="rf-box">
            <table cellpadding="0" cellspacing="0">
                <tr class="top">
                    <td colspan="2">
                        <table>
                            <tr>
                                <td></td>
                                <td style="text-align:middle">
                                    <h1>%s</h1>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            <p style="padding-left:20px">
                Hi Team,<br>
                Following are the last build execution result.
            </p>
            <table style="width:80%%;padding-left:20px">
                <tr class="heading">
                    <td>Test Status</td>
                    <td></td>
                </tr>
                <tr class="item">
                    <td>Total</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>Pass</td>
                    <td style="color:green">%s</td>
                </tr>
                <tr class="item">
                    <td>Fail</td>
                    <td style="color:red">%s</td>
                </tr>
                <tr class="item">
                    <td>Skip</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>Error</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>xPassed</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>xFailed</td>
                    <td>%s</td>
                </tr>
            </table>
            <br>
            <table style="width:80%%;padding-left:20px">
                <tr class="heading">
                    <td>Other Info:</td>
                    <td></td>
                </tr>
                <tr class="item">
                    <td>Pass Percentage (%%)</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>Executed Date</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>Machine</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>OS</td>
                    <td>%s</td>
                </tr>
                <tr class="item">
                    <td>Duration(s)</td>
                    <td>%s</td>
                </tr>
            </table>
            <table>
                <tr>
                    <td style="text-align:center;color: #999999; font-size: 11px">
                        <p>Best viewed in web!</p>
                    </td>
                </tr>
            </table>
        </div>
    </body>
    </html>
    """ % (company_name, total, passed, failed, skipped,
        error, xpassed, xfailed, percentage, exe_date, platform.uname()[1], platform.uname()[0], elapsed_time)

    msg.attach(MIMEText(email_content, 'html'))

    server.starttls()
    server.login(msg['From'], pwd)
    server.sendmail(from_user, to_addrs, msg.as_string())
# pytest-email


Plugin to send email after execution with results.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)]()
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]()
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)]()

---

### How it works:

 - Get execution details using  `pytest_terminal_summary()`
 - Build html email template
 - Send's email for respective recipients

---

### How to use in project:

1. Install `pytest-email`
   
   > Case 1: Using `setup.py` (clone repo and run command in root)
   ```
   python setup.py install
   ```

   > Case 2: Install from git (changes in master)
   ```
   pip install git+https://github.com/adiralashiva8/pytest-email
   ```

2. Execute test's normally using options

    ```
    pytest --email_uname="test@gmail.com" --email_pwd="XXXXX" --email_to="test1@gmail.com,test2@gmail.com"
    ```

    > By default email will be sent, users can restrict send email by using following command 
    ```
    pytest --email_send=False
    ```

    Email options:
    ```
    -> --email_uname - Email user name or id
    -> --email_pwd - Email user password
    -> --email_to - Recipients email ids
    -> --email_smtp - Email server smtp
    -> --email_subject - Email subject
    -> --email_org - Organization name to include in email
    -> --email_send - Send email based on input
    ```

---

*Sample Report*

<img src="pytest_email.jpg" alt="pytest_email.jpg">

---

### What kind of information is shared?

Following test counts:
- Total
- Passed
- Failed
- Skipped
- Error
- XPassed
- XFailed
- Duration

Future: Failed test information

---

*Thanks for using pytest-email!*

If you have any questions / suggestions / comments on this, please feel free to reach me at

 - Email: <a href="mailto:adiralashiva8@gmail.com?Subject=Pytest%20Email" target="_blank">`adiralashiva8@gmail.com`</a> 
 - LinkedIn: <a href="https://www.linkedin.com/in/shivaprasadadirala/" target="_blank">`shivaprasadadirala`</a>
 - Twitter: <a href="https://twitter.com/ShivaAdirala" target="_blank">`@ShivaAdirala`</a>

---

*Credits*

 - [Pytest-dev](https://github.com/pytest-dev)
 - [Stackoverflow](https://stackoverflow.com/questions/tagged/pytest)

---

 :star: repo if you like it

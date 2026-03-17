# Pythonize Everything 🐍
## Project Overview
A collection of Python-based automation scripts designed to eliminate "toil" by streamlining daily digital workflows—from system maintenance and file organization to automated communications.

## Core Workflows
**Automated Backup System (auto_back_up.py):**

Implements directory synchronization with intelligent versioning.

Features conditional Gzip compression based on configurable file-size thresholds.

Tech: argparse, shutil, gzip, os.

**Intelligent File Organizer (organizer.py):**

Automates directory cleanup by mapping file extensions to dynamically created categorized folders.

Tech: glob, os.

**WhatsApp Automation Utility (whatsapp.py):**

Programmatic interaction with WhatsApp Web to send personalized text messages and media attachments (images/documents) to multiple targets.

Tech: Selenium WebDriver, Chrome/Firefox drivers.

**Email Management Suite (email_delete.py):**

Batch processes IMAP server inboxes to search, filter, and permanently purge emails based on sender, subject, or date.

Tech: imaplib, email.

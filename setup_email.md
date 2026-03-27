# SMTP Email Setup Guide

## Step 1: Choose Email Provider

### Gmail (Recommended)
1. Enable 2-factor authentication
2. Go to Google Account settings
3. Security → App passwords
4. Generate new app password
5. Use app password (not regular password)

### Other Providers
- **Outlook**: smtp-mail.outlook.com:587
- **Yahoo**: smtp.mail.yahoo.com:587
- **Custom**: Your provider's SMTP settings

## Step 2: Set Environment Variables

### Option A: Temporary (Current Session)
```bash
set EMAIL_HOST=smtp.gmail.com
set EMAIL_PORT=587
set EMAIL_USE_TLS=True
set EMAIL_HOST_USER=your_email@gmail.com
set EMAIL_HOST_PASSWORD=your_app_password
```

### Option B: Using .env File
Edit `.env` file with your credentials:
```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

## Step 3: Restart Server
```bash
python manage.py runserver
```

## Step 4: Test
1. Open http://127.0.0.1:8000
2. Submit contact form
3. Check both email inboxes

## Features
- ✅ Real email sending via any SMTP server
- ✅ Fallback to console if no credentials
- ✅ Admin notifications to satyabratasuar163@gmail.com
- ✅ Auto-replies to users
- ✅ Works with Gmail, Outlook, Yahoo, etc.

## Gmail Setup Important Notes
- Use App Password, not regular password
- Enable "Less secure app access" if needed
- Make sure 2FA is enabled

# Vercel Deployment Guide

## Prerequisites
1. Install Vercel CLI: `npm i -g vercel`
2. Create Vercel account at https://vercel.com

## Step 1: Initialize Vercel
```bash
vercel login
vercel
```

## Step 2: Configure Environment Variables
In Vercel dashboard, add these environment variables:
- `SECRET_KEY`: Generate a new Django secret key
- `ENVIRONMENT`: `production`
- `EMAIL_HOST`: `smtp.gmail.com` (or your SMTP)
- `EMAIL_PORT`: `587`
- `EMAIL_USE_TLS`: `True`
- `EMAIL_HOST_USER`: `your_email@gmail.com`
- `EMAIL_HOST_PASSWORD`: `your_app_password`
- `DEFAULT_FROM_EMAIL`: `your_email@gmail.com`

## Step 3: Deploy
```bash
vercel --prod
```

## Files Created
- `vercel.json`: Vercel configuration
- `api/index.py`: WSGI entry point
- `.vercelignore`: Files to exclude
- Updated `requirements.txt`: Added python-dotenv

## Features
- ✅ Static files served by Vercel
- ✅ Django WSGI application
- ✅ Environment variable support
- ✅ Production-ready settings
- ✅ Email functionality

## Post-Deployment
1. Test your portfolio on the Vercel URL
2. Submit contact form to verify email sending
3. Configure custom domain if needed

## Notes
- Database: Uses SQLite (file-based) - works on Vercel
- Static files: Automatically handled by Vercel
- Email: SMTP configuration required
- SSL: Automatically provided by Vercel

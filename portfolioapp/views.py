from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
    return render(request, "index.html")


@csrf_exempt
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        print(f"Contact Form Data: name={name}, email={email}, phone={phone}, message={message}")

        # 📩 Email to YOU (Admin)
        admin_message = f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
"""
        
        try:
            result = send_mail(
                subject=f"New Message from {name or 'Anonymous'}",
                message=admin_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            print(f"Admin email sent result: {result}")
        except Exception as e:
            print(f"Error sending admin email: {e}")

        # 🤖 Auto-reply (ONLY if user email exists)
        if email:
            user_message = f"""
Hi {name or 'there'},

Thanks for reaching out!
I've received your message and will get back to you soon.

Regards,
Satyabrata
"""
            
            try:
                result = send_mail(
                    subject="Thanks for contacting me",
                    message=user_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False,
                )
                print(f"User email sent result: {result}")
            except Exception as e:
                print(f"Error sending user email: {e}")

        return redirect(reverse("home"))

    return redirect(reverse("home"))

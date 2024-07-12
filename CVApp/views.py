from django.shortcuts import render 
from django.views import View
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import send_mail



# Create your views here.

class home(View):
    def get( self, request):
        return render(request , 'base.html')
    

    def post(self,request):
        
        if request.method == 'POST':
            yourname=request.POST.get("yourname")
            youremail=request.POST.get("youremail")
            yourcontact=request.POST.get("yourcontact")
            subject=request.POST.get("subject")
            msg=request.POST.get("msg")


            try:

                mess='Email ID - ' + str(youremail) + '\n' +'Name - ' + str(yourname) + '\n' + 'Contact - ' +str(yourcontact) + '\n' + '\n' + '\n' +str(msg) 

                send_mail(
                    subject,
                    mess,
                    youremail,
                    ["yadnesh.jaynath.patil@gmail.com"],
                    fail_silently=False,
                )


                def send_revert_email(subject, message, recipient_list):
                    """
                    Function to send a revert email.
                    
                    Args:
                        subject (str): Subject of the email.
                        message (str): Body of the email.
                        recipient_list (list): List of recipient email addresses.
                    """
                    sender_email = "yadnesh.jaynath.patil@gmail.com"  # Your email address
                    send_mail(subject, message, sender_email, recipient_list)

                # revert on mail:
                revert_subject = "Re: Regarding Your Inquiry"
                revert_message = "Dear Sir/Madam, \n\nThank you for your inquiry. We have received your message and will revert to you shortly.\n\nBest regards,\nYadnesh Patil\ncodeFolio"
                revert_recipient_list = [youremail]  # List of recipient email addresses
                send_revert_email(revert_subject,revert_message, revert_recipient_list)



            except:
                pass
            return render(request, 'base.html')
        return render(request , 'base.html')






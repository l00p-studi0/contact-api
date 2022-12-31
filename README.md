# contact-api
Contact Form API

Description:
The Contact Form API allows users to send messages to the website owner or administrator via a web-based form.

Endpoints:
POST /index/

Parameters:
- Fullname (required): The Fullname of the user submitting the form.
- Email (required): The email address of the user submitting the form.
- Phone (required): The Phone number from the user.
- Comment (optional): The Comment or message  of the user submitting the form.

Response:
If the form submission is successful, the API will return a JSON response with the following structure:
{
    "status": "success",
    "message": "Thank you for your message. We will get back to you as soon as possible."
}


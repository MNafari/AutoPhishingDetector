import pandas as pd
import random

# List of phishing and non-phishing email messages
phishing_samples = [
    "Your account has been suspended! Click here to reactivate it.",
    "We've detected unusual activity on your email account. Verify now!",
    "Your Netflix subscription has been canceled. Click below to renew.",
    "Reset your banking password now! Unauthorized login detected.",
    "Your PayPal transaction failed! Please update your payment information.",
    "Urgent: Verify your PayPal account immediately to avoid suspension.",
    "You have won a $1000 gift card! Claim now by clicking the link.",
    "Your Amazon order has been delayed. Click here to check status.",
    "Your email has been flagged for suspicious activity. Confirm your identity.",
    "Security alert: Someone tried to access your account. Change your password now!",
    "Warning: Your credit card information has been leaked. Act fast!",
    "Exclusive deal for you! Click now to claim your discount.",
    "We need you to confirm your banking details immediately.",
    "Last chance! Your coupon expires in 24 hours. Click here.",
    "Attention: Unusual transactions detected in your bank account.",
    "Your mobile service will be disconnected unless you verify your payment."
]

non_phishing_samples = [
    "Hey, are you available for the project discussion tomorrow?",
    "Reminder: Your car service appointment is on Monday at 10 AM.",
    "Your order has been shipped! You can track your delivery here.",
    "Please find the attached invoice for your purchase.",
    "Can you review the project proposal before our call?",
    "Looking forward to our meeting next week. Let me know if you're available.",
    "Thanks for your response! I appreciate your input.",
    "Your package is on the way! Expected delivery: Friday.",
    "Reminder: Your subscription will expire in 3 days. Renew now.",
    "Invoice for your recent purchase is attached. Please review.",
    "Just checking in! Hope you’re doing well.",
    "Meeting rescheduled to next Monday. Let me know if that works.",
    "Your payment has been successfully processed.",
    "Invitation: Join us for a networking event this Saturday.",
    "Welcome to our community! We are excited to have you here.",
    "Thank you for your purchase! Your receipt is attached."
]

# Generate 500 phishing and 500 non-phishing samples
num_samples = 500
phishing_data = random.choices(phishing_samples, k=num_samples)
non_phishing_data = random.choices(non_phishing_samples, k=num_samples)

# Create dataset
data = {
    "message": phishing_data + non_phishing_data,
    "label": [1] * num_samples + [0] * num_samples  # 1 = Phishing, 0 = Safe
}

df = pd.DataFrame(data)

# Save dataset
dataset_path = "data/expanded_phishing_dataset.csv"
df.to_csv(dataset_path, index=False)

print(f"✅ Dataset created successfully! Saved at: {dataset_path}")


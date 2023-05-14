import reports
import os
import datetime
import emails


def process_text():
    full_content = []
    for file in os.listdir('supplier-data/descriptions'):
        with open(f'supplier-data/descriptions/{file}', 'r') as f:
            full_content.append(f'name: {f.readline()}<br/>')
            full_content.append(f'title: {f.readline()}<br/>')
        full_content.append('<br/>')
    return full_content


if __name__ == "__main__":
    current_date = datetime.date.today().strftime('%B %d,%Y')
    title = f"Processed Update on {current_date}"
    body = "<br/>".join(process_text())
    reports.generate_report('processed.pdf', title, body)

    sender = "automation@example.com"
    receiver = "student-04-f8b5971d4011@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = " All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)

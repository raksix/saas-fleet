import { Resend } from "resend";

const resend = new Resend(process.env.RESEND_API_KEY);

export async function sendEmail({ to, subject, html }: { to: string; subject: string; html: string }) {
  if (!process.env.RESEND_API_KEY) {
    console.log(`[email] to=${to} subject=${subject}`);
    return { id: "dev" };
  }
  return resend.emails.send({
    from: process.env.NEXT_PUBLIC_APP_URL ? `${process.env.NEXT_PUBLIC_APP_URL} <noreply@${process.env.NEXT_PUBLIC_APP_URL}>` : "noreply@example.com",
    to,
    subject,
    html,
  });
}

export function InvoiceEmail({ amount, invoiceUrl }: { amount: number; invoiceUrl: string }) {
  return {
    subject: `Invoice — $${(amount / 100).toFixed(2)}`,
    html: `
      <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto;">
        <h1>Thanks for your payment</h1>
        <p>We received your payment of $${(amount / 100).toFixed(2)}.</p>
        <p><a href="${invoiceUrl}" style="display:inline-block;background:#000;color:#fff;padding:10px 20px;border-radius:6px;text-decoration:none">View Invoice</a></p>
      </div>
    `,
  };
}

export function WelcomeEmail({ name }: { name: string }) {
  return {
    subject: "Welcome to Warehousehub Labs",
    html: `
      <div style="font-family: sans-serif; max-width: 600px; margin: 0 auto;">
        <h1>Welcome aboard, ${name}!</h1>
        <p>Thanks for signing up. Here's how to get the most out of your new account:</p>
        <ol>
          <li>Connect your data source</li>
          <li>Invite your team</li>
          <li>Set up integrations</li>
        </ol>
        <p>If you have any questions, just reply to this email.</p>
      </div>
    `,
  };
}

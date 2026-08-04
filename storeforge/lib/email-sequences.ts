// Drip email sequences for lifecycle marketing
export const SEQUENCES = {
  welcome: [
    { day: 0, template: "welcome", subject: "Welcome aboard 🎉" },
    { day: 1, template: "getting-started", subject: "Quick start guide (3 min)" },
    { day: 3, template: "feature-spotlight", subject: "Hidden gem: bulk actions" },
    { day: 7, template: "social-proof", subject: "How Sarah saved 10 hrs/week" },
    { day: 14, template: "upgrade-prompt", subject: "Ready for more?" },
  ],
  upgrade: [
    { day: 0, template: "upgrade-thanks", subject: "Welcome to Pro!" },
    { day: 2, template: "pro-tips", subject: "5 pro tips to get you started" },
    { day: 7, template: "advanced-features", subject: "Unlock advanced reporting" },
    { day: 30, template: "team-invite", subject: "Get your whole team on board" },
  ],
  churn_prevention: [
    { day: 0, template: "we-miss-you", subject: "We noticed you've been away" },
    { day: 3, template: "feedback-request", subject: "Quick question (30 sec)" },
    { day: 7, template: "discount-offer", subject: "30% off to stay with us" },
    { day: 14, template: "win-back", subject: "We've made improvements" },
  ],
};

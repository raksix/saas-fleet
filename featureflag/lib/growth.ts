// Growth hacking utilities
export async function trackReferral(userId: string, source: string) {
  // Track referral source for analytics
  await fetch("/api/track", {
    method: "POST",
    body: JSON.stringify({ event: "referral", userId, source }),
  });
}

export async function shareAchievement(achievement: string, channel: string) {
  // Viral loop: share milestones
  await fetch("/api/track", {
    method: "POST",
    body: JSON.stringify({ event: "share", achievement, channel }),
  });
}

export function generateReferralCode(userId: string): string {
  return `${userId.slice(0, 4)}-${Math.random().toString(36).slice(2, 6)}`.toUpperCase();
}

export const VIRAL_LOOPS = {
  milestone_share: "Share when you hit a milestone",
  team_invite_bonus: "Get 1 month free per invite",
  public_profiles: "Public profile boosts SEO",
  embed_widget: "Embed widgets drive backlinks",
};

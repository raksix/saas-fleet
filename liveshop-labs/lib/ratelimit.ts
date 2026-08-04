// Simple in-memory rate limiter. For production use Redis-backed.
const buckets = new Map<string, { count: number; resetAt: number }>();

export function rateLimit(key: string, limit: number, windowMs: number) {
  const now = Date.now();
  const bucket = buckets.get(key);
  if (!bucket || bucket.resetAt < now) {
    buckets.set(key, { count: 1, resetAt: now + windowMs });
    return { ok: true, remaining: limit - 1 };
  }
  bucket.count++;
  if (bucket.count > limit) return { ok: false, remaining: 0 };
  return { ok: true, remaining: limit - bucket.count };
}

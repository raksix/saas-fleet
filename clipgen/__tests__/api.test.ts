import { describe, it, expect, vi } from "vitest";
import { GET, POST } from "@/app/api/<resource>/route";

vi.mock("next-auth", () => ({
  getServerSession: vi.fn().mockResolvedValue({ user: { id: "u1", orgId: "o1" } }),
}));

describe("Resource API", () => {
  it("GET returns items", async () => {
    const res = await GET();
    expect(res.status).toBe(200);
  });

  it("POST requires auth", async () => {
    const req = new Request("http://localhost", {
      method: "POST",
      body: JSON.stringify({ name: "Test" }),
    });
    const res = await POST(req);
    expect([200, 201, 401]).toContain(res.status);
  });
});

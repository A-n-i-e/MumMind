// package.json should have "type": "module"
import express from "express";

const app = express();
app.use(express.json());

// 1️⃣ Verification route
app.get("/webhook", (req, res) => {
  const verifyToken = "my_verify_token"; // your chosen token

  const mode = req.query["hub.mode"];
  const token = req.query["hub.verify_token"];
  const challenge = req.query["hub.challenge"];

  if (mode === "subscribe" && token === verifyToken) {
    console.log("✅ Webhook verified!");
    res.status(200).send(challenge); // send challenge back
  } else {
    res.sendStatus(403); // not verified
  }
});

// 2️⃣ Message receiving route
app.post("/webhook", (req, res) => {
  console.log("📩 Message received:", JSON.stringify(req.body, null, 2));
  res.sendStatus(200); // Always respond 200 to Meta
});

app.listen(3000, () => {
  console.log("🚀 Server running on port 3000");
});

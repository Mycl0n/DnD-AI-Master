export type ChatMessage = {
  author: "PLAYER" | "DM" | "SYSTEM";
  text: string;
  playerId?: string;
  playerName?: string;
};


import React, { useState } from "react";
import { Sparkles } from "lucide-react";
import { askAssistant } from "../api";

const exampleQuestions = [
  "Recommend breakfast items",
  "Which products are low in stock?",
  "Show me dairy products",
  "Suggest highly rated snacks"
];

export default function AssistantPanel() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();

    if (!question.trim()) return;

    setIsLoading(true);
    setAnswer("");

    try {
      const result = await askAssistant(question);
      setAnswer(`${result.answer}\n\nAssistant mode: ${result.mode}`);
    } catch (error) {
      setAnswer(error.message);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <section className="assistant-panel">
      <div className="assistant-icon"><Sparkles /></div>
      <h2>Ask SwiftCart AI</h2>
      <p>Get product recommendations, find items and spot inventory risks.</p>

      <div className="suggestions">
        {exampleQuestions.map((example) => (
          <button key={example} onClick={() => setQuestion(example)}>
            {example}
          </button>
        ))}
      </div>

      <form onSubmit={handleSubmit} className="assistant-form">
        <input
          value={question}
          onChange={(event) => setQuestion(event.target.value)}
          placeholder="Ask about products, stock or shopping..."
        />
        <button disabled={isLoading}>
          {isLoading ? "Thinking..." : "Ask AI"}
        </button>
      </form>

      {answer && (
        <div className="assistant-answer">
          <strong><Sparkles size={16} /> SwiftCart AI response</strong>
          <p>{answer}</p>
        </div>
      )}
    </section>
  );
}

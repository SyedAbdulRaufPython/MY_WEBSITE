# # my_code_ai.py
# import re
# import numpy as np
# from datasets import load_dataset

# # 1. Load dataset (you can increase dataset size later)
# print("Loading dataset...")
# dataset = load_dataset("codeparrot/codeparrot-clean-train", split="train[:2000]")
# code_texts = dataset["content"]

# # 2. Tokenize code
# def tokenize_code(code):
#     return re.findall(r"[A-Za-z_]+|\d+|==|<=|>=|[^\s]", code)

# all_tokens = []
# for code in code_texts:
#     all_tokens.extend(tokenize_code(code))

# # 3. Build vocabulary
# vocab = sorted(set(all_tokens))
# stoi = {t: i for i, t in enumerate(vocab)}
# itos = {i: t for t, i in stoi.items()}
# vocab_size = len(vocab)
# print(f"Vocabulary size: {vocab_size}")

# # 4. Convert to IDs
# data_ids = [stoi[t] for t in all_tokens]

# # 5. Training data (bigram: predict next token from current token)
# xs = np.array(data_ids[:-1])
# ys = np.array(data_ids[1:])

# # One-hot encoding
# x_onehot = np.eye(vocab_size)[xs]
# y_onehot = np.eye(vocab_size)[ys]

# # 6. Initialize model weights
# W = np.random.randn(vocab_size, vocab_size) / vocab_size
# lr = 0.1

# # 7. Training loop
# print("Training...")
# for epoch in range(300):
#     logits = x_onehot @ W
#     probs = np.exp(logits) / np.sum(np.exp(logits), axis=1, keepdims=True)
#     loss = -np.mean(np.sum(y_onehot * np.log(probs + 1e-9), axis=1))

#     grad = x_onehot.T @ (probs - y_onehot) / len(xs)
#     W -= lr * grad

#     if epoch % 50 == 0:
#         print(f"Epoch {epoch}, Loss: {loss:.4f}")

# print("Training complete!")

# # 8. Generation function
# def generate(start_token, length=30):
#     if start_token not in stoi:
#         print("Token not in vocabulary, using 'def' instead.")
#         start_token = "def"
#     idx = stoi[start_token]
#     out = [start_token]
#     for _ in range(length):
#         logits = W[idx]
#         probs = np.exp(logits) / np.sum(np.exp(logits))
#         idx = np.random.choice(range(vocab_size), p=probs)
#         out.append(itos[idx])
#     return " ".join(out)

# # 9. Chat interface
# print("\n--- Code AI Chat ---")
# print("Type 'exit' to quit.\n")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit"]:
#         break
#     print("AI:", generate(user_input, length=30))

import tiktoken

def main():
    tokenizer = tiktoken.encoding_for_model("gpt-4")
    text = "Прогнозирование маркетинговых KPI"
    tokens = tokenizer.encode(text)
    print(tokens)
    print(f"Количество токенов: {len(tokens)}")


if __name__ == "__main__":
    main()

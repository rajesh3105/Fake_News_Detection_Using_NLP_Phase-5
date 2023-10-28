# Tokenize text
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
X_train_tokens = tokenizer.texts_to_sequences(X_train)
X_test_tokens = tokenizer.texts_to_sequences(X_test)
# print(f"Total tokens: {len(tokenizer.word_index)}")
# Calculate total tokens
total_tokens = sum([len(tokens) for tokens in X_train_tokens])
print("Total Tokens:", total_tokens)
maxlen = 20
X_train_pad = pad_sequences(X_train_tokens, maxlen=maxlen, padding='post')
X_test_pad = pad_sequences(X_test_tokens, maxlen=maxlen, padding='post')
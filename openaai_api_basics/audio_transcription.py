client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# TRANSCRIPTION

# Open the openai-audio.mp3 file
audio_file = open("openai-audio.mp3", "rb")

# Create a transcript from the audio file
response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# Extract and print the transcript text
print(response.text)



# TRANSLATION from lang to another



audio_file = open("non_english_audio.m4a", "rb")
prompt = "The transcript is about AI trends and ChatGPT."
response = client.audio.translations.create(model="whisper-1",
                                            file=audio_file,
                                            prompt=prompt)
print(response.text)

## ADDING PROMPT for model to help it better understand context


# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Write an appropriate prompt to help the model
prompt = "Audio relates to a recent World Bank report"

# Create a translation from the audio file
response = client.audio.translations.create(model="whisper-1",
                                            file=audio_file,
                                            prompt=prompt)

print(response.text)


##


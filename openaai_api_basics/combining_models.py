

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

audio_file = open("meeting_recording.mp4", "rb")

audio_response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

transcript = audio_response.text
prompt = "Extract the attendee names from the start of this meeting transcript: " + transcript

chat_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)
print(chat_response.choices[0].message.content)


## ANOTHER EXAMPLE

# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# Create a request to the API to identify the language spoken
chat_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": audio_response.text}
    ]
)
print(chat_response.choices[0].message.content)



## 





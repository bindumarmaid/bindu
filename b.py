import speech_recognition as sr
# record audio
r=sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_thershold=True
	print("say spmething!!")
	audio=r.listen(source)
try:
	print("you said:"+ r.recognize_google(audio))
except sr.UnknownValuerError:
	print("Google speech Recognition could not understand audio")
except sr.RequestedError as e:
	print("could not request results from Google speech Recognition service;{0}".format(e))

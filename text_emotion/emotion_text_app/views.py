from django.shortcuts import render
from django.http import HttpResponse
from emotion_text_app.models import EmotionLog
from model.infer import predict


def text_form_view(request):
    if request.method == 'POST':
        # Get the text data from the request
        text = request.POST['text']

        prediction = predict(text)
        # Create a context dictionary to pass to the template
        context = {
            'text': text,
            'predicted_label': prediction
        }
        EmotionLog.objects.create(input_text=text, emotion=prediction)
        # Render the template with the processed text
        return render(request, 'predicted_emotion.html', context)
    return render(request, 'text_form.html')


def predicted_emotion_view(request):
    return render(request,'predicted_emotion.html')
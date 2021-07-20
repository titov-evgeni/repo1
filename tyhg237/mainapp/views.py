import json
from django.shortcuts import redirect, render
from .forms import InputForm
from .models import InputModel


def base(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            for count in range(len(request.POST) - 1):
                input_name = 'name' + str(count) if count else 'name'
                input_value = request.POST[input_name]
                if input_value:
                    field = json.dumps(input_name)
                    user_input = json.dumps(input_value, ensure_ascii=False)
                    InputModel.objects.create(field=field,
                                              user_input=user_input)
                count += 1
        return redirect('/output/')
    else:
        form = InputForm()
    return render(request, 'base.html', {'form': form})


def output(request):
    data = list(InputModel.objects.all().values('id', 'field', 'user_input'))
    return render(request, 'output.html', {'json_list': data})
